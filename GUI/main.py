from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel
from fractions import Fraction
from mainwindow import Ui_MainWindow
from Simplex_tableau import Simplex
import sys


# Para mostrar el tableau
class TableModel(QAbstractTableModel):
    def __init__(self, data, header_data):
        super(TableModel, self).__init__()
        self._data = data
        self.header_data = header_data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header_data[col])
        return QVariant()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.Simplex: Simplex = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Iniciar atributos
        self.ui.stackedWidget.setCurrentIndex(0)
        self.n_variables = 0
        self.n_restricciones = 0
        self.z_values = []
        self.A_values = []
        self.b_values = []
        self.ui.boton.hide()

        # Connexions
        self.ui.btn_aceptar_1.clicked.connect(self.btn_aceptar_1_clicked)
        self.ui.btn_aceptar_2.clicked.connect(self.btn_aceptar_2_clicked)
        # self.ui.btn_aceptar_3.clicked.connect(self.btn_aceptar_3_clicked)

    """ Slots """
    def btn_aceptar_1_clicked(self):
        self.n_variables = self.ui.spinVariables.value()
        self.n_restricciones = self.ui.spinRestricciones.value()
        self.add_objective_function()
        self.add_restrictions()
        self.ui.stackedWidget.setCurrentIndex(1)

    def btn_aceptar_2_clicked(self):
        z = []
        for i in range(0, len(self.z_values)):
            z.append(self.z_values[i].value())
        print(z)

        A = []
        for x in range(0, len(self.A_values)):
            aux = []
            for y in range(0, len(self.A_values[x])):
                aux.append(self.A_values[x][y].value())
            A.append(aux)
        print(A)

        b = []
        for j in range(0, len(self.b_values)):
            b.append(self.b_values[j].value())
        print(b)

        self.Simplex = Simplex(self.n_variables, self.n_restricciones, z, A, b, self.n_restricciones)
        self.realizar_simplex()

        self.ui.stackedWidget.setCurrentIndex(2)

    """def btn_aceptar_3_clicked(self):
        self.n_variables = 0
        self.n_restricciones = 0
        self.z_values = []
        self.A_values = []
        self.b_values = []"""

    """ Methods """

    # Agregar los inputs de la f.o. necesarios a la ui
    def add_objective_function(self):
        label_z = QLabel('Z = ')
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout = QHBoxLayout()
        layout.addSpacerItem(spacer)
        layout.addWidget(label_z)
        for i in range(0, self.n_variables):
            input_n = QDoubleSpinBox()
            input_n.setMinimum(-999.99)
            input_n.setMaximum(999.99)
            input_n.setDecimals(3)
            label_n = QLabel('')
            if i == self.n_variables - 1:
                label_n.setText(f' x{i + 1}')
            else:
                label_n.setText(f' x{i + 1} + ')
            layout.addWidget(input_n)
            layout.addWidget(label_n)
            self.z_values.append(input_n)
        layout.addSpacerItem(spacer)
        self.ui.lay.insertRow(0, layout)

    # Agregar los inputs de las restricciones a la ui
    def add_restrictions(self):
        label_restriccion = QLabel('Sujeto a: ')
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout = QHBoxLayout()
        layout.addSpacerItem(spacer)
        layout.addWidget(label_restriccion)
        layout.addSpacerItem(spacer)
        self.ui.lay.insertRow(1, layout)

        row_idx = 2
        for i in range(0, self.n_restricciones):
            layout_r = QHBoxLayout()
            layout_r.addSpacerItem(spacer)
            linea = []
            for j in range(0, self.n_variables):
                input_n = QDoubleSpinBox()
                input_n.setMinimum(-999.99)
                input_n.setMaximum(999.99)
                input_n.setDecimals(3)
                label_n = QLabel('')
                linea.append(input_n)
                if j == self.n_variables - 1:
                    label_n.setText(f' x{j + 1} ≤ ')
                    input_b = QDoubleSpinBox()
                    input_b.setMinimum(-999.99)
                    input_b.setMaximum(999.99)
                    input_b.setDecimals(3)
                    layout_r.addWidget(input_n)
                    layout_r.addWidget(label_n)
                    layout_r.addWidget(input_b)
                    self.b_values.append(input_b)
                else:
                    label_n.setText(f' x{j + 1} + ')
                    layout_r.addWidget(input_n)
                    layout_r.addWidget(label_n)
            layout_r.addSpacerItem(spacer)
            self.ui.lay.insertRow(row_idx, layout_r)
            self.A_values.append(linea)
            row_idx += 1

    # Agregar el tableau actual a la ui
    def print_tableau(self):
        h_data = self.Simplex.tags_x
        data = []
        r_objetivo = [' ']

        # RO
        for i in range(0, len(self.Simplex.c)):
            r_objetivo.append(str(Fraction(self.Simplex.c[i])))
        r_objetivo.append(str(Fraction(self.Simplex.b[0])))
        data.append(r_objetivo)

        # R1 to Rn
        for x in range(0, len(self.Simplex.A)):
            linea = [self.Simplex.tags_y[x]]
            for y in range(0, len(self.Simplex.A[x])):
                linea.append(str(Fraction(self.Simplex.A[x][y])))
            linea.append(str(Fraction(self.Simplex.b[x + 1])))
            data.append(linea)

        # print(h_data)
        # print(data)
        model = TableModel(data, h_data)
        table = QTableView()
        table.setMinimumHeight(250)
        table.setModel(model)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        return table

    def realizar_simplex(self):
        es_optimo = False
        no_es_acotada = False
        es_degenerada = False
        iteracion = 0

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        while es_optimo is False:
            if iteracion == 0:
                label = QLabel('Tableau inicial')
                layout = QHBoxLayout()
                layout.addSpacerItem(spacer)
                layout.addWidget(label)
                layout.addSpacerItem(spacer)
                self.ui.lay_res.addRow(layout)
            else:
                label_space = QLabel(' ')
                lay_space = QHBoxLayout()
                lay_space.addWidget(label_space)
                self.ui.lay_res.addRow(lay_space)

                label_i = QLabel(f'Iteración {iteracion}')
                layout_i = QHBoxLayout()
                layout_i.addSpacerItem(spacer)
                layout_i.addWidget(label_i)
                layout_i.addSpacerItem(spacer)
                self.ui.lay_res.addRow(layout_i)

            lay_tableau = QHBoxLayout()
            # lay_tableau.addSpacerItem(spacer)
            lay_tableau.addWidget(self.print_tableau())
            # lay_tableau.addSpacerItem(spacer)
            self.ui.lay_res.addRow(lay_tableau)

            if self.Simplex.calcular_columna_pivote():
                if self.Simplex.calcular_pivote():
                    string = f'Entra {self.Simplex.tags_x[self.Simplex.pivot_c + 1]}' \
                             f'y sale {self.Simplex.tags_y[self.Simplex.pivot_r]}'
                    label_entra = QLabel(string)
                    lay_pivot = QHBoxLayout()
                    lay_pivot.addSpacerItem(spacer)
                    lay_pivot.addWidget(label_entra)
                    lay_pivot.addSpacerItem(spacer)
                    self.ui.lay_res.addRow(lay_pivot)

                    self.Simplex.tags_y[self.Simplex.pivot_r] = self.Simplex.tags_x[self.Simplex.pivot_c + 1]
                    self.Simplex.calcular_renglon_pivote()
                    self.Simplex.calcular_nuevo_ro()
                    if self.Simplex.calcular_reng_restantes():
                        es_degenerada = True
                        # es_optimo = True
                else:
                    es_optimo = True
                    no_es_acotada = True
            else:
                es_optimo = True

            iteracion += 1

        if no_es_acotada:
            str_res = 'La solución no está acotada.'
            label_res = QLabel(str_res)
            lay_res = QHBoxLayout()
            lay_res.addSpacerItem(spacer)
            lay_res.addWidget(label_res)
            lay_res.addSpacerItem(spacer)
            self.ui.lay_res.addRow(lay_res)
        elif es_degenerada:
            # self.print_tableau()
            print('La solución es temporalmente degenerada.')
            str_res = f'El óptimo es z = {Fraction(self.Simplex.b[0])}'
            label_res = QLabel(str_res)
            lay_res = QHBoxLayout()
            lay_res.addSpacerItem(spacer)
            lay_res.addWidget(label_res)
            lay_res.addSpacerItem(spacer)
            self.ui.lay_res.addRow(lay_res)
            for i in range(0, len(self.Simplex.tags_y)):
                print(f'{self.Simplex.tags_y[i]} = {Fraction(self.Simplex.b[i + 1])}')
        else:
            str_res = f'El óptimo es z = {Fraction(self.Simplex.b[0])}'
            label_res = QLabel(str_res)
            lay_res = QHBoxLayout()
            lay_res.addSpacerItem(spacer)
            lay_res.addWidget(label_res)
            lay_res.addSpacerItem(spacer)
            self.ui.lay_res.addRow(lay_res)
            for i in range(0, len(self.Simplex.tags_y)):
                print(f'{self.Simplex.tags_y[i]} = {Fraction(self.Simplex.b[i + 1])}')

        label_space = QLabel(' ')
        lay_space = QHBoxLayout()
        lay_space.addWidget(label_space)
        self.ui.lay_res.addRow(lay_space)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainWindow()
    main_app.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

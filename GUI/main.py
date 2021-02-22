from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
from Simplex_tableau import Simplex
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Iniciar atributos
        self.ui.stackedWidget.setCurrentIndex(0)
        self.n_variables = 0
        self.n_restricciones = 0
        self.z_values = []
        self.A_values = []
        self.b_values = []

        # Connexions
        self.ui.btn_aceptar_1.clicked.connect(self.btn_aceptar_1_clicked)
        self.ui.btn_aceptar_2.clicked.connect(self.btn_aceptar_2_clicked)

    # Slots
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

        S = Simplex(self.n_variables, self.n_restricciones, z, A, b, self.n_restricciones)
        lineas = S.realizar_simplex_gui()

        for k in range(0, len(lineas)):
            self.ui.textEdit.append(lineas[k])

        self.ui.stackedWidget.setCurrentIndex(2)

    # Methods
    def add_objective_function(self):
        label_z = QLabel('Z = ')
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout = QHBoxLayout()
        layout.addSpacerItem(spacer)
        layout.addWidget(label_z)
        for i in range(0, self.n_variables):
            input_n = QSpinBox()
            input_n.setMinimum(-10)
            input_n.setMaximum(10)
            label_n = QLabel('')
            if i == self.n_variables-1:
                label_n.setText(f' x{i+1}')
            else:
                label_n.setText(f' x{i+1} + ')
            layout.addWidget(input_n)
            layout.addWidget(label_n)
            self.z_values.append(input_n)
        layout.addSpacerItem(spacer)
        self.ui.scrollLayout.addRow(layout)

    def add_restrictions(self):
        label_restriccion = QLabel('Sujeto a: ')
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout = QHBoxLayout()
        layout.addSpacerItem(spacer)
        layout.addWidget(label_restriccion)
        layout.addSpacerItem(spacer)
        self.ui.scrollLayout.addRow(layout)

        for i in range(0, self.n_restricciones):
            layout_r = QHBoxLayout()
            layout_r.addSpacerItem(spacer)
            linea = []
            for j in range(0, self.n_variables):
                input_n = QSpinBox()
                input_n.setMinimum(-10)
                input_n.setMaximum(10)
                label_n = QLabel('')
                linea.append(input_n)
                if j == self.n_variables - 1:
                    label_n.setText(f' x{j + 1} ≤ ')
                    input_b = QSpinBox()
                    input_b.setMinimum(-99)
                    input_b.setMaximum(99)
                    layout_r.addWidget(input_n)
                    layout_r.addWidget(label_n)
                    layout_r.addWidget(input_b)
                    self.b_values.append(input_b)
                else:
                    label_n.setText(f' x{j + 1} + ')
                    layout_r.addWidget(input_n)
                    layout_r.addWidget(label_n)
            layout_r.addSpacerItem(spacer)
            self.ui.scrollLayout.addRow(layout_r)
            self.A_values.append(linea)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainWindow()
    main_app.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

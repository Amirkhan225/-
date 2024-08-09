from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton
from random import randint
app=QApplication([])
main_win=QWidget()
main_win.show()
main_win.setWindowTitle('Кости')
main_win.move(900, 70)
main_win.resize(400,200)
app.exec()
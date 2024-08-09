<<<<<<< HEAD
=======
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton
from instr import *

class Main_Win(Qwidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        def set_appear(self):
            self.setWindowTitle(txt_title)
            self.resize(win_width,win_height)
            self.move(win_x,win_y)
        def initUI(self):
            self.hello_text=QLabel(txt_hello)
            self.instruction=Qlabel(txt_instruction)
            self.button=QPushButton(txt_next)
            self.layout=QVBoxLayout()
            self.layout.addWidget(self.hello_text)
            self.layout.addWidget(self.instruction)
            self.layout.addWidget(self.button)
        def connects(self):
            self.btn_next.clicked.connect(self.next_click)
        def next_click(self):
            self.hide()
            self.tw=WinTwo
app=QApplication([])
mw=Main_Win()
app.exec_()
>>>>>>> b50d0e42e29463c7c774c673a42b07e89083d020

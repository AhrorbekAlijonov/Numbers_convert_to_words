import sys
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget
)

from function import num_to_uzbek_convert

class Convert(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(400,300)
        self.__init()
        self.setStyleSheet("background-color: #4D3C77")
        
    def convert(self):
        try:
            self.number = self.edit_display.text() 
            self.number = int(self.number)
            num_in_letter = num_to_uzbek_convert(int(self.number))
            self.show_result.addItem(str(num_in_letter))
        except:
            self.show_result.addItem("Iltimos faqat butun son kiriting !!!")
            
    def __init(self):
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.edit_display = QLineEdit()
        self.edit_display.setPlaceholderText("Enter number ... ")
        
        
        self.btn_exit = QPushButton("Exit")
        self.btn_exit.setStyleSheet("background-color: white; color: #4D3C55")
        self.btn_exit.clicked.connect(self.close)
        
        
        self.btn_convert = QPushButton("Convert")
        self.btn_convert.setStyleSheet("background-color: white;")
        self.btn_convert.clicked.connect(self.convert)

        self.show_result = QListWidget()
        self.show_result.setStyleSheet("background-color: white")

        self.h_box.addWidget(self.edit_display)
        self.edit_display.setStyleSheet("background-color: white")
        self.h_box.addWidget(self.btn_convert)
        
        
        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.show_result)
        self.v_box.addWidget(self.btn_exit)
        
        self.setLayout(self.v_box)
        
        self.show()


app = QApplication(sys.argv)
num = Convert()
app.exec_()
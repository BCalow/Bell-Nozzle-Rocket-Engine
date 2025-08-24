#import initialVariablesCalculations
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QGridLayout
from PyQt6.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt6.QtCore import Qt
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rocket Engine Initial Variables")
        #self.showMaximized()

        self.M = QLineEdit()
        self.M.setValidator(QIntValidator())
        self.M.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.M.setMaximumWidth(50)

        layout = QGridLayout()
        layout.addWidget("Molar Mass", 0, 1)
        layout.addWidget(self.M, 1, 0)
        layout.addWidget("Kg/mol", 2, 0)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        print("Clicked!")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
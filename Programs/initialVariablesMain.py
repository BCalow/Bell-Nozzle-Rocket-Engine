#import initialVariablesCalculations
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rocket Engine Initial Variables")
        self.showMaximized()


    def the_button_was_clicked(self):
        print("Clicked!")



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
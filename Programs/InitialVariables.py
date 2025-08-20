import sys
from PySide6.QtWidgets import QApplication, QPushButton


def function():
    print("The 'function' has been called!")

app = QApplication()
button = QPushButton("Call function")
button.clicked.connect(function)
button.show()
sys.exit(app.exec())

#Input Variables
m_p = 10#Total Available Propellant Mass (kg)
dt = 20#Total Burn Time (S)
A_e = 0.1#Exit Area (M^2)
gamma = 1.31#Ratio of Specific heats
M_m = 24#Sum of Molar Mass of Gasses
T_c = 3000#Chamber Temperature (k)

#Approximate Guesses
epsilon = 5#Area Ratio Approximate Guess
Ma_e = 3#Mach Exit Approximate Guess

#Building MatPlotLib Window
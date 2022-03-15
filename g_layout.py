# Filename: g_layout.py
# Grid Layout Example

###################################################################################

import sys

from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QGridLayout')

# Grid Layout where the second and third arguments are the row and column placements
layout = QGridLayout()
layout.addWidget(QPushButton('Uno'), 0, 0)
layout.addWidget(QPushButton('Dos'), 0, 1)
layout.addWidget(QPushButton('Tres'), 0, 2)
layout.addWidget(QPushButton('Cuatro'), 1, 0)
layout.addWidget(QPushButton('Cinco'), 1, 1)
layout.addWidget(QPushButton('Sies'), 1, 2)
layout.addWidget(QPushButton('Siete'), 2, 0)
# The fourth and fifth arguments are for row space
# In this example we are spanning 1 space vertically and 2 spaces horizontally
layout.addWidget(QPushButton('Ocho y Nueve'), 2, 1, 1, 2)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())





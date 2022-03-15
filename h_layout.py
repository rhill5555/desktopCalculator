# FileName: h_layout.py
# Horizontal Layout example with PyQt5

###################################################################################

import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget

# Create app instance
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QHBoxLayout')

# Creates a QHBOxLayout object
# This is a layout manager
# For a column of widgets use QVBoxLayout
layout=QHBoxLayout()

# Add three buttons all in a row
layout.addWidget(QPushButton('Bitch'))
layout.addWidget(QPushButton('Ass'))
layout.addWidget(QPushButton('Motherfucker'))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())


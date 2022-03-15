# FileName: hello.py
# Simple Hello World example with PyQt5

# Step 1: Import QApplication and all required widgets from PyQt5.QtWidgets
# Step 2: Create an Instance of QApplication
# Step 3: Create an instance of your application's GUI
# Step 4: Show your application's GUI
# Step 5: Run your Application's event loop (or main loop)

###################################################################################
# Step 1: Imports

# Allows handling of exit status of the application
import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget

###################################################################################
# Step 2: Create an instance of QApplication

# pass sys.argv because object deals with common command line arguments
app = QApplication(sys.argv)

###################################################################################
# Step 3: Create instance of application's GUI
# Based on QWidget, base class of all user interface objects in PyQt
# To avoid memory leaks make sure any QWidget object has a parent with the exception of the top level window

# Instance of QWidget provides all feather needed to create app's window
window = QWidget()
window.setWindowTitle('PyQt5 App')
# Define size and placement
window.setGeometry(100, 100, 280, 80)
# place at specific coordinates
window.move(60, 15)
helloMsg = QLabel('<h1>Hello Bitches!</h1>', parent=window)
helloMsg.move(60, 15)

#################################################################################
# Step 4: Show your application's GUI
window.show()

# Step 5: Run your application's event loop
sys.exit(app.exec())

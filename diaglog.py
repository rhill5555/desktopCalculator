# Filename: dialog.py
# Dialog-Style application

##################################################################################

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QVBoxLayout

class Dialog(QDialog):
    #Dialog.
    def __init__(self, parent=None):
        #Initializer
        super().__init__(parent)
        self.setWindowTitle('QDialog')

        dlgLayout = QVBoxLayout()

        formLayout = QFormLayout()
        formLayout.addRow('Name:', QLineEdit())
        formLayout.addRow('Salary:', QLineEdit())
        formLayout.addRow('Dick Length:', QLineEdit())
        formLayout.addRow('Dick Circumference:', QLineEdit())

        dlgLayout.addLayout(formLayout)

        btns = QDialogButtonBox(
                            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())


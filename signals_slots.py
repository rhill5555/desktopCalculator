# FileName: signals_slots.py
# Signals and Slots Examples

# PyQT Widgets act as event-catchers
# In response to events widgets emit a signal
# A signal is a message that announces a change in state
# In order for a signal to trigger an action the signal needs to be connected to a slot
# A slot is a function or method that will perform an action when the connecting signal is emitted

# If the signal is not connected to a slot the signal is ignored
# A signal can be connected to 1+ slots or another singal
# A slot may be connected to 1+ signals
# Widgets have their own sets of predefined signals

# widget.signal.connect(slot_function)

#############################################################################
import functools
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QPushButton, QVBoxLayout

def greeting(who=None):
    # Slot function
    if msg.text():
        msg.setText('')
    else:
        #msg.setText('Hello Bitches!')
        # If you need to add two arguments use functools.partial
        msg.setText(f'Hello {who}')

# Initialize App
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and Slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
# Connect click to greeting()
#btn.clicked.connect(greeting)
btn.clicked.connect(functools.partial(greeting, 'Bitches!'))

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())

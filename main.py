import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel('Hello from PyQt!')
label.show()
sys.exit(app.exec_())

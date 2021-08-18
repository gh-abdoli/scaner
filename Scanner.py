import sys
from PyQt4 import QtCore, QtGui
from MyClassForm import *

def Main():
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QMainWindow()
    ui = MyForm(Form)
    Form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Main()

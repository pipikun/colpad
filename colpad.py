from colpad_ui import Ui_MainWindow
import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtGui as qg

def main_entry():
    app = qw.QApplication(sys.argv)
    w   = qw.QMainWindow()
    ui  = Ui_MainWindow()
    ui.setupUi(w)
    w.setWindowTitle("colpad v0.0.1")
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_entry()

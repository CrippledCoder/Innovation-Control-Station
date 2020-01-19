from VRAppUI import *
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

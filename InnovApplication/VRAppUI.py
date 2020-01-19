import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QLabel, QSpacerItem, QComboBox, \
    QVBoxLayout, QHBoxLayout, QMessageBox, QLineEdit, QAction
from PyQt5 import QtWidgets, Qt, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
import sys
import hashlib, binascii, os

class Login(QWidget):
    """
        The Login client for the admin panel.

        This will take in the user input, processes it with the saved password file that
        is in the same file and then will compare the input. Password file was created
        so that a password would not need to be hardcoded into the system.

        On success of password -> admin panel
        On close of window -> main panel

        functions:
            initUI(self): This starts the specific window
            closeEvent(self): Handles the exiting of the window
            checkPassword(self): Handles what happens to the windows after
                the user submits a password
            hash_password(self, password): Hashes a password filed. Also used
                in the admin panel.
            verify_password(self, stored_password, provided_password): Handles
                the comparison of passwords from the user and the supplied file
    """
    switch_window = QtCore.pyqtSignal(str, QWidget)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(500, 120)
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    # Good example of how to use the window close
    def closeEvent(self, event):
        try:
            self.switch_window.emit("h", self)
            event.accept()
        except:
            event.ignore()



    def check_password(self):
        msg = QMessageBox()
        enteredpass = str(self.lineEdit_password.text())
        with open("login.txt","r") as file:
            savedpass = file.read()

        if self.verify_password(savedpass, enteredpass):
            msg.setText('Success')
            msg.exec_()
            self.switch_window.emit("a", self)
        else:
            msg.setText('Incorrect Password')
            msg.exec_()

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password


class VRAppUI(QWidget):
    """
        The main window for the overall client.

        This is where the user can access all the subsystem he or she would like
        to use for the flight simulator. This window cannot be exited out of but
        will be closed on window shutdown.

        attr:
            title (str): The title of the window top bar
            width (int): The width of the window in pixels
            height (int): the height of the window in pixels

        functions:
            initUI(self): Loads the main window and handles the design of the window
            freePlayClick(self): Handles the signal if Free Fly is clicked
            missionsClick(self): Handles the signal if missions is clicked
            customClick(self): Handles the signal if custom is clicked
            adminClick(self): Handles the signal if admin is clicked
            vSpacer(self, size): A simple function to add a vertical spacer
            hSpacer(self, size): A simple function to ad a horizontal spacer
    """

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__()
        self.title = "Texan VR"
        self.width = 1500
        self.height = 1000
        self.initUI()

    def initUI(self):
        # DESIGN SECTION
        grid_layout = QGridLayout()  # outermost layout
        self.setLayout(grid_layout)

        # halves
        rightLayout = QGridLayout()
        rightBottomLayout = QGridLayout()
        rightTopLayoutOuter = QVBoxLayout()
        rightTopTopLayout = QHBoxLayout()
        rightTopBottomLayout = QHBoxLayout()

        # Label Maker
        leftLabel = QLabel("")
        rightTopSqLabel = QLabel("Squadron")
        rightTopFlightLabel = QLabel("Flight")

        # Button Maker
        freeFlyButton = QPushButton("Free Fly")
        missionsButton = QPushButton("Missions")
        customButton = QPushButton("Custom")
        adminButton = QPushButton("Admin")

        # Combo Container Maker
        # Squadron
        comboSquadron = QComboBox(self)
        comboSquadron.addItem("37th FTS")
        comboSquadron.addItem("41st FTS")

        # Flight
        comboFlight = QComboBox(self)
        comboFlight.addItem("A Flight")
        comboFlight.addItem("B Flight")
        comboFlight.addItem("C Flight")
        comboFlight.addItem("D Flight")
        comboFlight.addItem("F Flight")
        comboFlight.addItem("V Flight")
        comboFlight.addItem("W Flight")
        comboFlight.addItem("X Flight")
        comboFlight.addItem("Y Flight")
        comboFlight.addItem("Z Flight")

        # STYLE SHEET AREA
        # Button Styling
        buttonStyle = '''QPushButton {
                                        box-shadow: 3px 4px 0px 0px #1564ad;
                                        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.05 #79bbff, stop:1 #378de5);
                                        border-radius:10px;
                                        border:1px solid #337bc4;
                                        display:inline-block;
                                        cursor:pointer;
                                        color:#ffffff;
                                        font-family:Arial;
                                        font-size:40px;
                                        font-weight:bold;
                                        padding:12px 44px;
                                        text-decoration:none;
                                        text-shadow:0px 1px 0px #528ecc;
                                        height: 80px;
                                        }
                            QPushButton:hover {
                                        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.05 #378de5, stop:1 #79bbff);
                                        background-color:#378de5;
                                        }
                             QPushButton:active {
                                            position:relative;
                                            top:1px;
                                        }
                                        '''
        freeFlyButton.setStyleSheet(buttonStyle)
        missionsButton.setStyleSheet(buttonStyle)
        customButton.setStyleSheet(buttonStyle)
        adminButton.setStyleSheet(buttonStyle)

        # Label Styling
        leftLabel.setText('''<p>
                                <font size="15"><b>Welcome to Texan VR <br>Control Center!</b></font>
                             </p>
                             <br>
                             <p>
                             <font size="4">
                                <br>
                                <i>Free Fly:</i>  Starts at 13R at Columbus
                                <br>
                                <br>
                                <i>Missions:</i> Select a pre-planned mission
                                <br>
                                <br>
                                <i>Custom:</i> Select the parameters that fit your training
                                <br>
                                <br>
                                <i>Admin:</i> For VR Admin use
                            </font>
                             </p>
                            ''')
        rightTopSqLabel.setStyleSheet("font-weight: bold;")
        rightTopFlightLabel.setStyleSheet("font-weight: bold;")
        self.setStyleSheet("background-color: #72A0C1;")  # widget background

        # Alignments set
        leftLabel.setAlignment(Qt.AlignCenter)
        rightTopSqLabel.setAlignment(Qt.AlignRight)
        rightTopFlightLabel.setAlignment(Qt.AlignRight)

        # ORGANIZING THE LAYOUTS
        # Main Grid
        grid_layout.addWidget(leftLabel, 0, 0)
        grid_layout.addLayout(rightLayout, 0, 1)

        # upper right quadrant
        rightLayout.addLayout(rightTopLayoutOuter, 0, 0)  # used a vertical layout
        rightTopLayoutOuter.addItem(self.vSpacer(200))
        rightTopLayoutOuter.addLayout(rightTopTopLayout)
        rightTopLayoutOuter.addLayout(rightTopBottomLayout)
        rightTopTopLayout.addWidget(rightTopSqLabel)
        rightTopTopLayout.addWidget(comboSquadron)
        rightTopTopLayout.addItem(self.hSpacer(200))
        rightTopBottomLayout.addWidget(rightTopFlightLabel)
        rightTopBottomLayout.addWidget(comboFlight)
        rightTopBottomLayout.addItem(self.hSpacer(200))

        # space out the right
        rightLayout.addItem(self.vSpacer(200), 1, 0)

        # bottom right quadrant
        rightLayout.addLayout(rightBottomLayout, 2, 0)  # big grid
        rightBottomLayout.addWidget(freeFlyButton, 0, 0)
        rightBottomLayout.addWidget(missionsButton, 0, 1)
        rightBottomLayout.addWidget(customButton, 1, 0)
        rightBottomLayout.addWidget(adminButton, 1, 1)

        grid_layout.setRowStretch(1, 0)
        # example if a spacer is needed
        # grid_layout.addItem(self.vSpacer(100), 3, 0)

        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        # BUTTON ACTION SECTION
        freeFlyButton.clicked.connect(self.freePlayClick)
        missionsButton.clicked.connect(self.missionsClick)
        customButton.clicked.connect(self.customClick)
        adminButton.clicked.connect(self.adminClick)

    @pyqtSlot()
    def freePlayClick(self):
        self.switch_window.emit("f")

    def missionsClick(self):
        print('Launching Missions...')

    def customClick(self):
        print('Launching Custom...')

    def adminClick(self):
        self.switch_window.emit("l")

    def vSpacer(self, size):
        return QSpacerItem(0, size, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

    def hSpacer(self, size):
        return QSpacerItem(size, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

class Controller:

    # need this for every class
    def __init__(self):
        pass

    # this connects to the main function and gets the program going
    def start(self):
        self.main = VRAppUI()
        self.main.switch_window.connect(self.which)
        self.main.show()

    # when a button is selected, this decides which of the windows will open
    def which(self, text, oldWin=None):
        if text == "f":
            pass
        if text == "m":
            pass
        if text == "c":
            pass
        if text == "l":
            self.login = Login()
            self.main.setEnabled(False)
            self.login.switch_window.connect(self.which)
            self.login.show()
        if text == "a":
            oldWin.close()
            self.main.setEnabled(True)
        if text == "h":
            self.home(oldWin)

    # when that respective window is closed, this returns the screen back to the main screen
    def home(self, window):
        self.main.setEnabled(True)
        window.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



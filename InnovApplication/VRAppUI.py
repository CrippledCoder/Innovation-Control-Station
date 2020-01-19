import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QLabel, QSpacerItem, QComboBox, \
    QVBoxLayout, QHBoxLayout, QMessageBox, QLineEdit, QAction
from PyQt5 import QtWidgets, Qt, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
import sys
import hashlib, binascii, os
from PyQt5 import QtWidgets
from styleSheet import *

'''
def closeEvent(self, event):
    msg = QMessageBox.question(self, "Close Admin", "Are you sure you want to close without saving?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No )
    if msg == QMessageBox.Yes:
        self.switchWindow.emit("h", self)
        event.accept()
    else:
        event.ignore()
'''

def vSpacer(size):
    return QSpacerItem(0, size, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

def hSpacer(size):
    return QSpacerItem(size, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

class Login(QWidget):
    """
        The Login client for the admin panel.

        This will take in the user input, processes it with the saved password file that
        is in the same file and then will compare the input. Password file was created
        so that a password would not need to be hardcoded into the system.

        On success of password -> admin panel
        On close of window -> main panel

        attr:
            lineEdit_password (QLineEdit): Sets attr of password container

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
    switchWindow = QtCore.pyqtSignal(str, QWidget)

    def __init__(self):
        super().__init__()
        self.passwordContainer = QLineEdit()
        self.setWindowTitle('Login Form')
        self.resize(500, 200)
        self.initUI()

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint);

        layout = QVBoxLayout()
        self.setLayout(layout)
        inputLayout = QHBoxLayout()
        buttonLayout = QHBoxLayout()

        labelPassword = QLabel('<font size="3"> Password </font>')
        self.passwordContainer.setPlaceholderText('Please enter password')
        self.passwordContainer.setStyleSheet("font: 25px;")

        inputLayout.addWidget(self.passwordContainer)

        buttonLogin = QPushButton('Login')
        buttonLayout.addWidget(buttonLogin)
        buttonLogin.clicked.connect(self.checkPassword)

        buttonCancel = QPushButton('Cancel')
        buttonLayout.addWidget(buttonCancel)
        buttonCancel.clicked.connect(self.goBack)

        buttonLogin.setStyleSheet(passButtonStyle)
        buttonCancel.setStyleSheet(cancelButtonStyle)

        layout.addLayout(inputLayout)
        layout.addLayout(buttonLayout)

    # Good example of how to use the window close
    def goBack(self):
        self.switchWindow.emit("h", self)

    def checkPassword(self):
        msg = QMessageBox()
        msg.setWindowTitle('Status')
        enteredPass = str(self.passwordContainer.text())
        with open("login.txt", "r") as file:
            savedPass = file.read()

        if self.verify_password(savedPass, enteredPass):
            self.switchWindow.emit("a", self)
        else:
            msg.setText('Incorrect Password')
            msg.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            msg.exec_()

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


class passChange(QWidget):
    """
        The password change client for the admin of the application

        This will take in the user input, check the previous pass and save a new password.

        attr:
            prevPasswordContainer (QLineEdit()): Takes in the previous password
            newPasswordContainer (QLineEdit()): Takes in the new password

        functions:
            initUI(self): This starts the specific window
            checkPassword(self): Handles what happens to the windows after
                the user submits a password
            hash_password(self, password): Hashes the new password and files it
            verify_password(self, stored_password, provided_password): Handles
                the comparison of old passwords from the user and the supplied file
    """
    switchWindow = QtCore.pyqtSignal(str, QWidget)

    def __init__(self):
        super().__init__()
        self.prevPasswordContainer = QLineEdit()
        self.newPasswordContainer = QLineEdit()
        self.resize(500, 200)
        self.initUI()

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint);

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        inputLayout = QHBoxLayout()
        buttonLayout = QHBoxLayout()

        self.prevPasswordContainer.setPlaceholderText('Previous password')
        self.prevPasswordContainer.setStyleSheet("font: 25px;")
        self.newPasswordContainer.setPlaceholderText('New password')
        self.newPasswordContainer.setStyleSheet("font: 25px;")

        inputLayout.addWidget(self.prevPasswordContainer)
        inputLayout.addWidget(self.newPasswordContainer)

        buttonChange = QPushButton('Change')
        buttonLayout.addWidget(buttonChange)
        buttonChange.clicked.connect(self.checkPassword)

        buttonCancel = QPushButton('Cancel')
        buttonLayout.addWidget(buttonCancel)
        buttonCancel.clicked.connect(self.close)

        buttonChange.setStyleSheet(passButtonStyle)
        buttonCancel.setStyleSheet(cancelButtonStyle)

        self.layout.addLayout(inputLayout)
        self.layout.addLayout(buttonLayout)

    def checkPassword(self):
        msg = QMessageBox()
        msg.setWindowTitle('Status')
        enteredPass = str(self.prevPasswordContainer.text())
        with open("login.txt", "r") as file:
            savedPass = file.read()

        if self.verify_password(savedPass, enteredPass):
            self.hash_password(self.newPasswordContainer.text())
            msg.setText('Password Changed!')
            msg.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            msg.exec_()
            self.close()
        else:
            msg.setText('Incorrect Previous Password')
            msg.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            msg.exec_()

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        with open("login.txt", "w") as file:
            file.write((salt + pwdhash).decode('ascii'))

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

class fileCopy(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Admin Panel"
        self.width = 1500
        self.height = 1000
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setLayout(layout)

class AdminPanel(QWidget):
    """

    """
    switchWindow = QtCore.pyqtSignal(str, QWidget)

    def __init__(self):
        super().__init__()
        self.title = "Admin Panel"
        self.width = 700
        self.height = 500
        self.move(200, 200)
        self.initUI()

    def initUI(self):
        # DESIGN SECTION
        # !!!!!!
        # CHANGE LOGIN BACK
        # !!!!!!!
        layout = QGridLayout()
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setLayout(layout)


        # Button Maker
        appStartButton = QPushButton("Start Up App Select")
        fileCopyButton = QPushButton("File Copier")
        passChangeButton = QPushButton("Change Password")
        profileLoader = QPushButton("Profile Loader")

        # Button Styler
        appStartButton.setStyleSheet(adminButtonStyle)
        fileCopyButton.setStyleSheet(adminButtonStyle)
        passChangeButton.setStyleSheet(adminButtonStyle)
        profileLoader.setStyleSheet(adminButtonStyle)

        # Button Organizer
        layout.addWidget(appStartButton, 0, 0)
        layout.addWidget(fileCopyButton, 0, 1)
        layout.addWidget(passChangeButton, 1, 0)
        layout.addWidget(profileLoader, 1, 1)

        appStartButton.clicked.connect(self.appStarter)
        fileCopyButton.clicked.connect(self.fileCopy)
        passChangeButton.clicked.connect(self.passChange)
        profileLoader.clicked.connect(self.profileLoad)

    @pyqtSlot()
    def appStarter(self):
        pass

    def fileCopy(self):
        self.fCopy = fileCopy()
        self.fCopy.show()

    def passChange(self):
        self.pChange = passChange()
        self.pChange.show()

    def profileLoad(self):
        pass

    def closeEvent(self, event):
        self.switchWindow.emit("h", self)
        event.accept()


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
    """

    switchWindow = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.title = "Texan VR"
        self.width = 1500
        self.height = 1000
        self.initUI()

    def initUI(self):
        # DESIGN SECTION
        grid_layout = QGridLayout()  # outermost layout
        self.setLayout(grid_layout)
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        # halves
        rightLayout = QGridLayout()
        rightBottomLayout = QGridLayout()
        rightTopLayoutOuter = QVBoxLayout()
        rightTopTopLayout = QHBoxLayout()
        rightTopBottomLayout = QHBoxLayout()

        # Label Maker
        leftLabel = QLabel("")
        rightTopSqLabel = QLabel("             Squadron")
        rightTopFlightLabel = QLabel("                   Flight")

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
        rightTopSqLabel.setStyleSheet("font: 30px; font-weight: bold;")
        rightTopFlightLabel.setStyleSheet("font: 30px; font-weight: bold;")
        self.setStyleSheet("background: #72A0C1;")  # widget background

        comboFlight.setStyleSheet("font: 30px; background: white;")
        comboSquadron.setStyleSheet("font: 30px; background: white;")

        # Alignments set
        leftLabel.setAlignment(Qt.AlignCenter)
        rightTopSqLabel.setAlignment(Qt.AlignVCenter)
        rightTopFlightLabel.setAlignment(Qt.AlignVCenter)

        # ORGANIZING THE LAYOUTS
        # Main Grid
        grid_layout.addWidget(leftLabel, 0, 0)
        grid_layout.addLayout(rightLayout, 0, 1)

        # upper right quadrant
        rightLayout.addLayout(rightTopLayoutOuter, 0, 0)  # used a vertical layout
        rightTopLayoutOuter.addItem(vSpacer(200))
        rightTopLayoutOuter.addLayout(rightTopTopLayout)
        rightTopTopLayout.addItem(vSpacer(200))
        rightTopLayoutOuter.addLayout(rightTopBottomLayout)
        rightTopTopLayout.addWidget(rightTopSqLabel)
        rightTopTopLayout.addWidget(comboSquadron)
        rightTopTopLayout.addItem(hSpacer(200))
        rightTopBottomLayout.addWidget(rightTopFlightLabel)
        rightTopBottomLayout.addWidget(comboFlight)
        rightTopBottomLayout.addItem(hSpacer(200))

        # space out the right
        rightLayout.addItem(vSpacer(200), 1, 0)

        # bottom right quadrant
        rightLayout.addLayout(rightBottomLayout, 2, 0)  # big grid
        rightBottomLayout.addWidget(freeFlyButton, 0, 0)
        rightBottomLayout.addWidget(missionsButton, 0, 1)
        rightBottomLayout.addWidget(customButton, 1, 0)
        rightBottomLayout.addWidget(adminButton, 1, 1)

        grid_layout.setRowStretch(1, 0)

        # BUTTON ACTION SECTION
        freeFlyButton.clicked.connect(self.freePlayClick)
        missionsButton.clicked.connect(self.missionsClick)
        customButton.clicked.connect(self.customClick)
        adminButton.clicked.connect(self.adminClick)

    @pyqtSlot()
    def freePlayClick(self):
        self.switchWindow.emit("f")

    def missionsClick(self):
        self.switchWindow.emit("m")

    def customClick(self):
        self.switchWindow.emit("c")

    def adminClick(self):
        self.switchWindow.emit("l")



class Controller:
    """
        This controls the opening and closing of windows and main selections
        of where the user would like to be.

        attr:
            main(QWidget): Opens the first instance of the main window

        functions:
            start(self): Starts the controller at the point in which the program
                is loaded
            which(self, text, oldWin=None): The main controller. Decides which windows
                open and close next based on signals from the previous classes
            home(self, window): Takes the user from a sub window back to the disabled
                main window and re-enables it
    """

    # need this for every class
    def __init__(self):
        self.main = VRAppUI()
        self.start()

    # this connects to the main function and gets the program going
    def start(self):
        self.main.switchWindow.connect(self.which)
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
            self.login.switchWindow.connect(self.which)
            self.login.show()
        if text == "a":
            self.admin = AdminPanel()
            oldWin.close()
            self.main.hide()
            self.admin.switchWindow.connect(self.which)
            self.admin.show()
        if text == "h":
            self.home(oldWin)

    # when that respective window is closed, this returns the screen back to the main screen
    def home(self, window):
        self.main.setEnabled(True)
        window.close()
        self.main.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

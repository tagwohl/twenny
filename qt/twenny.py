import sys
import time
from datetime import datetime
from PyQt5 import QtWidgets, QtGui, QtCore

class Twenny(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        super().__init__(icon, parent)
        self.INTERVAL_TIME = 1200
        self.UPDATE_TIME = 1000

        self.nextCall = int(datetime.now().timestamp()) + self.INTERVAL_TIME

        self.initializeTimer(parent)
        self.createMenu(parent)

    def initializeTimer(self, parent):
        self._timer = QtCore.QTimer(parent, timeout=self.ticker, interval=self.UPDATE_TIME)
        self._timer.start()

    def createMenu(self, parent):
        menu = QtWidgets.QMenu(parent)

        remainingTime = menu.addAction("Remaining time: 20:00")

        # Create Exit menu action
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(self.exit)

        self.setContextMenu(menu)
        self._menu_items = {"remainingTime": remainingTime, "exit": exitAction}

    def updateRemainingTime(self, currentTime):
        diffTime = self.nextCall - currentTime
        minutes = diffTime // 60
        seconds = diffTime % 60

        remainingTime = self._menu_items["remainingTime"]
        remainingTime.setText("Remaining time: {:02d}:{:02d}".format(minutes, seconds))

    def ticker(self):
        currentTime = int(datetime.now().timestamp())

        if currentTime <= self.nextCall:
            self.updateRemainingTime(currentTime)
        else:
            self.showMessage("Twenny", "It's time, look away for 20 seconds!", QtGui.QIcon("icon.ico"))
            time.sleep(20)
            self.showMessage("Twenny", "You can continue working now!", QtGui.QIcon("icon.ico"))
            self.nextCall = int(datetime.now().timestamp()) + self.INTERVAL_TIME

    def exit(self):
        self._timer.stop()
        QtCore.QCoreApplication.exit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    trayIcon = Twenny(QtGui.QIcon("icon.ico"), widget)
    trayIcon.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

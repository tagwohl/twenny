from win10toast import ToastNotifier
import time
from Windows import constants

starttime = time.time()
toaster = ToastNotifier()


def start():
    toaster.show_toast("twenny", "It's time, look away for 20 seconds!", icon_path="icon.ico", duration=constants.LOOK_AWAY_DURATION)
    toaster.show_toast("twenny", "You can continue working now!", icon_path="icon.ico", duration=constants.CONTINUE_DURATION)
    

while True:
    time.sleep(constants.SHOW_EVERY - ((time.time() - starttime) % constants.SHOW_EVERY))
    start()

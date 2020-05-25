from win10toast import ToastNotifier
import time

starttime = time.time()
toaster = ToastNotifier()

def start():
    toaster.show_toast("twenny", "It's time, look away for 20 seconds!", icon_path="icon.ico", duration=20)
    toaster.show_toast("twenny", "You can continue working now!", icon_path="icon.ico", duration=5)
    

while True:
    start()
    time.sleep(1200 - ((time.time() - starttime) % 1200.0))

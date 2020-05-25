import os
import time
starttime = time.time()
def start():
    path=os.path.dirname(os.path.abspath(__file__))
    os.system("notify-send -i "+path+"/icon.png -u normal 'Tweeny' \"It's time, look away for 20 seconds!\"")
    time.sleep(20)
    
    os.system("notify-send -i "+path+"/icon.png -u normal 'Tweeny' 'You can continue working now'")

while True:
    start()
    time.sleep(1200 - ((time.time() - starttime) % 1200.0))
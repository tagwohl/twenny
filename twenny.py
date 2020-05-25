import rumps
import time

class twenny(object):
    def __init__(self):
        self.app = rumps.App("twenny")
        self.timer = rumps.Timer(self.ticker, 1)
        self.interval = 1200
        self.bau_menu()
        self.start_knopf = rumps.MenuItem(title="Start Timer", callback=self.start_timer)
        self.stopuhr = rumps.MenuItem(title="20:00")
        self.app.menu = [self.stopuhr, self.start_knopf]

    def bau_menu(self):
        self.timer.count = 0
        self.app.title = "👁️"

    def ticker(self, zaehler):
        time_left = zaehler.end - zaehler.count
        mins = time_left // 60 if time_left >= 0 else time_left // 60 + 1
        secs = time_left % 60 if time_left >= 0 else (-1 * time_left) % 60
        if mins == 0 and time_left < 0:
            rumps.notification(title="twenny", subtitle="It's time, look away for 20 seconds!", message='')
            self.timer.count = 0
            time.sleep(20)
            rumps.notification(title="twenny", subtitle="You can continue working now!", message='')
            ticker()
        else:
            self.start_knopf.set_callback(None)
            self.stopuhr.title = '{:2d}:{:02d}'.format(mins, secs)
        zaehler.count += 1


    def start_timer(self, zaehler):
            self.timer.count = 0
            self.timer.end = self.interval
            self.timer.start()


    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = twenny()
    app.run()

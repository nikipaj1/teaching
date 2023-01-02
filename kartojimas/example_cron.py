import time
import datetime

class Analizatiorius:
    def __init__(self, analizuoti=True):
        self.analizuoti = analizuoti

    def analizuoti(self):
        # sudedingos analizes funkcijos
        # running time 1.5 minutes
        return "analizuoju"

    def analizuoti_be_sustojimo(self, laukimo_laikas = 5):
        # while True:
        #     self.analizuoti()
        #     time.sleep(5 * 60)

        # 16:01 -> 16:05 16:10 ...
        while True:
            if datetime.datetime.now().minute % 5 == 0:
                self.analizuoti()
            else:
                time.sleep(5)


        # 16:04:29 -> 16:04:59 -> 16:05:29

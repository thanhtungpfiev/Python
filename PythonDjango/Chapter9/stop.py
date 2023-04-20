# Created by Admin at 5/22/2022
import threading
from time import sleep


class Fibo(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._running = True

    def stop(self):
        self._running = False

    def run(self) -> None:
        a, b = 0, 1
        while self._running:
            print(a, end=' ')
            a, b = b, a + b
            sleep(0.07)
        print()


fibo = Fibo()
fibo.start()
sleep(1)
fibo.stop()
fibo.join()
print('All done')

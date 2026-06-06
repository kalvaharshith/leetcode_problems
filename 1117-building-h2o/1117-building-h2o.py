from threading import Semaphore, Barrier
class H2O:
    def __init__(self):
        self.h = Semaphore(2)
        self.o = Semaphore(1)
        self.barrier = Barrier(3)
    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.acquire()
        self.barrier.wait()
        releaseHydrogen()
        self.h.release()
    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.acquire()
        self.barrier.wait()
        releaseOxygen()
        self.o.release()
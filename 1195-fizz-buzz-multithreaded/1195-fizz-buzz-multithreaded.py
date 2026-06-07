from threading import Condition
from typing import Callable

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.curr = 1
        self.cv = Condition()

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.curr <= self.n and (
                    self.curr % 3 != 0 or self.curr % 5 == 0
                ):
                    self.cv.wait()

                if self.curr > self.n:
                    self.cv.notify_all()
                    return

                printFizz()
                self.curr += 1
                self.cv.notify_all()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.curr <= self.n and (
                    self.curr % 5 != 0 or self.curr % 3 == 0
                ):
                    self.cv.wait()

                if self.curr > self.n:
                    self.cv.notify_all()
                    return

                printBuzz()
                self.curr += 1
                self.cv.notify_all()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.curr <= self.n and (
                    self.curr % 15 != 0
                ):
                    self.cv.wait()

                if self.curr > self.n:
                    self.cv.notify_all()
                    return

                printFizzBuzz()
                self.curr += 1
                self.cv.notify_all()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.cv:
                while self.curr <= self.n and (
                    self.curr % 3 == 0 or self.curr % 5 == 0
                ):
                    self.cv.wait()

                if self.curr > self.n:
                    self.cv.notify_all()
                    return

                printNumber(self.curr)
                self.curr += 1
                self.cv.notify_all()
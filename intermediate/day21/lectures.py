# Class Inheritance
class Animal:

    def __init__(self) -> None:
        self.num_eyes = 2

    def breath(self):
        print("Inhale, exhale.")


class Fish(Animal):

    def __init__(self) -> None:
        super().__init__()

    def swim(self):
        print("Moving in water.")

    def breath(self):
        super().breath()
        print("Doing this underwater.")


nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)

from classA import A

class C(A):
    def __init__(self, d=100, c=1):
        super().__init__(d,c)

    def write(self):
        print("class c")

    def (self):
        print(f"-> d = {self.d} \n-> c = {self.c}")

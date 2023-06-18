from classA import 

class B(A):
    def __init__(self,d,c):
        super().__init__(d,c)

    def sub(self):
        print(f"{self.d/self.c} class B")

    def minus(self):
        print(f"{self.d-self.c} class B")


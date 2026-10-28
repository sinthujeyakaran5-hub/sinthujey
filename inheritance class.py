## single inheritance

class Dad:
    def house(self):
        print("pink")

class Son(Dad):
    def shop(self):
        print("blue")

S=Son()
S.house()
S.shop()

## multi level inheritance

class Grandfather:
    def house(self):
        print("pink")

class Father(Grandfather):
    def shop(self):
        print("blue")

class Son(Father):
    def car(self):
        print("red")

S=Son()
S.house()
S.shop()
S.car()

## multiple inheritance

class Father:
    def shop(self):
        print("blue")

class Mother:
    def car(self):
        print("red")

class Son(Father, Mother):
    def house(self):
        print("pink")

S=Son()
S.shop()
S.car()
S.house()

## hirarchical inheritance

class Father:
    def shop(self):
        print("blue")

class Son(Father):
    def house(self):
        print("pink")

class Daughter(Father):
    def car(self):
        print("red")

S=Son()
S.shop()
S.house()

D=Daughter()
D.shop()
D.car()

## hybrid inheritance

class Father:

    def shop(self):
        print("blue")

class Mother:
    def car(self):
        print("red")

class Son(Father, Mother):
    def house(self):
        print("pink")

class Daughter(Father, Mother):
    def bike(self):
        print("green")

S=Son()
S.shop()
S.car()
S.house()

D=Daughter()
D.shop()
D.car()
D.bike()


from dataclasses import dataclass

x = 100
@dataclass
class OOP:
    x = 30
    def foo(self):
        x = self.x
        print("OOP 출력: "+str(x))

x = 10
def foo():
    global x
    x = x +20
    print("FP 출력: "+str(x))

x = 100
def menu_3():
    x=10
    def B():
        nonlocal x
        x=20
    B()
    print(x)

x= 100
def menu_4():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()

x = 1
def menu_5():
    x = 10
    def B():
        x = 20
        def C():
            global x
            x = x+ 30
            print(x)
        C()
    B()

x = 100
def menu_6():
    a = 3
    b = 5
    t = 0
    def mul_add(x):
        nonlocal t
        t =  t + (a * x + b)
        print("클로저 1 결과: "+str(t))

    def mul_add_2(x):
        nonlocal t
        t = t + (a * x - b)
        print("클로저 2 결과: " + str(t))

    return {"덧셈1":mul_add,"덧셈2":mul_add_2}


x = 100
def menu_7():
    a = 3
    b = 5
    return lambda x: a*x + b

total = 100
def menu_8():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a*x + b
        print(total)
    return mul_add




if __name__ == '__main__':
    while True:
        menu = ["종료","oop","fp global", "nonlocal", "f in f nonlocal",'f in f global','closure','closure lamda', 'closure nonlocal']
        print("*"*100)
        for i,j in enumerate(menu):
            print(f'{i}.{j}')
        choice = int(input("menu : "))
        print("*"*100)
        if choice == 0:
            print('종료')
            break
        elif choice == 1:
            print('oop')
            oop = OOP()
            oop.foo()
        elif choice == 2:
            print('fp global')
            foo()
        elif choice == 3:
            print('nonlocal')
            menu_3()
        elif choice == 4:
            print('f in f nonlocal')
            menu_4()
        elif choice == 5:
            print('f in f global')
            menu_5()
        elif choice == 6:
            print('closure')
            c = menu_6()
            print("클로저1: " + str(c["덧셈1"](2)))  # 예상치 11
            print("클로저2: " + str(c["덧셈2"](2)))  # 예상치 1
        elif choice == 7:
            print('closure lamda')
            c = menu_7()
            print(c(1),c(2),c(3),c(4),c(5))
        elif choice == 8:
            print('closure nonlocal')
            c = menu_8()
            c(1)
            c(2)
            c(3)
        else: print(' wrong menu ')

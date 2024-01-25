class calculator:
    def __init__(self):
        self.num1=0
        self.num2=0
        self.choice=0

    def input1(self):
        self.num1=int(input("\nEnter first number :- "))
        self.num2=int(input("\nEnter second number :- "))

    def menu(self):
        while(self.choice!=6):
            print("\n\n|===== CALCULATOR MENU =====|")
            print("\n1.ADDITION\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.MODULUS\n6.EXIT")
            self.choice=int(input("\nEnter your choice (1 to 6) :-"))
            match(self.choice):
                case 1:
                    self.input1()
                    print(f"\nThe Addition of two numbers {self.num1} and {self.num2} is {self.num1 + self.num2} .....")
                    exit
                case 2:
                    self.input1()
                    print(f"\nThe Substraction of two numbers {self.num1} and {self.num2} is {self.num1 - self.num2} .....")
                    exit
                case 3:
                    self.input1()
                    print(f"The Multiplication of two numbers {self.num1} and {self.num2} is {self.num1 * self.num2} .....")
                    exit
                case 4:
                    self.input1()
                    print(f"The Division of two numbers {self.num1} and {self.num2} is {self.num1 / self.num2} .....")
                    exit
                case 5:
                    self.input1()
                    print(f"The Modulus of two numbers {self.num1} and {self.num2} is {self.num1 % self.num2} .....")
                    exit
                case 6:
                    print("\n!!! Exiting from Calculator !!!")
                    print("\n\n!______ EXITED ______!\n")
                    exit
                case _:
                    print("\n!!_____ INVALID CHOICE _____!!\n")
                    exit

cobj=calculator()
cobj.menu()







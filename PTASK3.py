import random

class generator:
    def __init__(self):
        self.len1=0
        self.choice=0
        self.password=""

    def simple(self):
        div=(self.len1)//2
        for i in range(1,self.len1+1):
            if(len(self.password)<div):
                self.password += chr(random.randint(ord('a'), ord('z')))
            else:
                self.pass2=random.randint(0,9)
                self.password +=str(self.pass2)

        print(f"\nYour {self.len1} digit Simple password is {self.password} .....")
        self.password=""

    def medium(self):
        
        for i in range(1,self.len1+1):
            if(len(self.password)<self.len1-3):
                self.password += chr(random.randint(ord('a'), ord('z')))
            
            elif(len(self.password)==self.len1-3):
                 self.password += chr(random.randint(ord('#'), ord('&')))
            
            else:
                self.pass2=random.randint(0,9)
                self.password +=str(self.pass2)

        print(f"\nYour {self.len1} digit Medium password is {self.password} ..... ")
        self.password=""

    def complex(self):
        
        self.password=chr(random.randint(ord('A'), ord('Z')))
        # self.password+=chr(random.randint(ord('A'), ord('Z')))
        for i in range(3,self.len1+1):
            if(len(self.password)<self.len1-3):
                self.password += chr(random.randint(ord('a'), ord('z')))
            
            elif(len(self.password)<=self.len1-3):
                 self.password += chr(random.randint(ord('#'), ord('&')))
            
            else:
                self.pass2=random.randint(0,9)
                self.password +=str(self.pass2)

        print(f"\nYour {self.len1} digit Complex password is {self.password} ..... ")
        self.password=""

    def passgen(self):
        self.len1=int(input("\nEnter the length for the password (greater than 4) :- "))
        if(self.len1<4):
            print("\n!!___ Password length must be greater than or equal to 4 ___!!\n")
        else:
            while(self.choice!=4):
                print("\n|----- Different Complexity Levels -----|")
                print("\n1.Simple\n2.Medium\n3.Complex\n4.Exit")
                self.choice=int(input("\nEnter your choice (1 to 4) :- "))
                match(self.choice):
                    case 1:
                        self.simple()
                        exit  
                    case 2:
                        self.medium()
                        exit
                    case 3:
                        self.complex()
                        exit
                    case 4:
                        print("\n!!__ Exiting from password generator __!!")
                        print("\n\n!!!_____ EXITED _____!!!")
                        exit
                    case _:
                        print("\n!!_____ Invalid Choice _____!!\n")
                        exit
gobj=generator()
gobj.passgen()
    
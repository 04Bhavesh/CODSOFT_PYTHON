import random

class Game:
    def __init__(self):
        self.random = 0
        self.choice = 0
        self.count1=0
        self.count2=0
        self.choice2=0

    def rock(self):
        self.random = random.randint(1, 3)

        if self.choice == 1:
            print("\nUser Choice is ""ROCK"" ", end="and ")
        elif self.choice == 2:
            print("\nUser Choice is ""PAPER"" ", end="and ")
        elif self.choice == 3:
            print("\nUser Choice is ""SCISSOR"" ", end="and ")

        if self.random == 2:
            print("Computer Choice is ""PAPER"" ")
        elif self.random == 3:
            print("Computer Choice is ""SCISSOR"" ")
        elif self.random == 1:
            print("Computer Choice is ""ROCK"" ")

        if self.random == 1:
            if self.random == self.choice:
                print("\n!!!___ Match Tie ___!!!")
            elif self.choice == 3:
                self.count1+=1
                print("\n!!!___ Computer wins ___!!!")
            else:
                self.count2+=1
                print("\n!!!___ User Wins ___!!!")
        elif self.random == 3:
            if self.random == self.choice:
                print("\n!!!__ Match Tie __!!!")
            elif self.choice == 2:
                self.count1+=1
                print("\n!!!__ Computer wins __!!!")
            else:
                self.count2+=1
                print("\n!!!__ User Wins __!!!")
        elif self.random == 2:
            if self.random == self.choice:
                print("\n!!!__ Match Tie __!!!")
            elif self.choice == 1:
                self.count1+=1
                print("\n!!!__ Computer wins __!!!")
            else:
                self.count2+=1
                print("\n!!!__ User Wins __!!!")
        else:
            pass


    def menu(self):
        
            print("\n\n|------ GAME MENU ------|")
            print("\n1.ROCK\n2.PAPER\n3.SCISSOR")
            self.choice = int(input("\nEnter your Choice (1 to 3) :- "))
            match self.choice:
                case 1:
                    self.rock()
                    exit
                case 2:
                    self.rock()
                    exit
                case 3:
                    self.rock()
                    exit
                # case 4:
                #     print("\n!___ EXITING FROM THE GAME ___!")
                #     print("\n\n!!!___ EXITED ___!!!")
                #     exit
                case _:
                    print("\n!!!___ Invalid Choice ___!!!\n")
                    exit

    def again(self):
        while(self.choice2!=3):
            print("\n|--- Do You Want to Play Again ? ---|")
            print("\n1.Yes\n2.Show Result\n3.No")
            self.choice2=int(input("\nEnter your choice (1 to 3):- "))
            match(self.choice2):
                case 1:
                    self.menu()
                    exit
                case 2:
                    print(f"\n|----- Final Score :- You wins = {self.count2} and Computer wins = {self.count1} -----|")
                    exit
                case 3:
                    print("\n!___ EXITING FROM THE GAME ___!")
                    print("\n\n!!!___ EXITED ___!!!")
                    exit
                case _:
                    print("\n!!!___ Invalid Choice ___!!!\n")
                    exit


gobj = Game()
gobj.menu()
gobj.again()

class ToDO:
    
    def __init__(self):
      self.list1=[]
      self.choice=0
      # self.file1=open("Tasks.txt",'w')
      # self.file1.close()
      self.task1=""

    def fetch(self):
      file1=open("Tasks.txt",'r')
      while(True):
         line=file1.readline().strip()
         
         if not line:
            break
         self.list1.append(line)

    def add(self):
       self.task1=str(input("\nEnter your new Task :- "))
       self.list1.append(self.task1)
       #print(f"\nYour Task {self.task1} is going to add!!!")
       
       print(f"\n !!!Your Task {self.task1} has been added Successfully !!!")

    def show(self):
         print("|-------- TASKS --------|")
         for i in range(0,len(self.list1)):
             print(f"{i+1}. {self.list1[i]}")

    def delete(self,element):
       
       print(f"\n!!! Your Selected Task is going to delete !!!")
       
       self.list1.remove(self.element)
       print(f"\n!!! Your Selected Task has been deleted !!!")

    def update(self):
        print("\n|----- Your Scheduled Tasks -----|")
        for i in range(0,len(self.list1)):
            print(f"{i+1}. {self.list1[i]}")
        self.index2=int(input("\nWhich task no. you have to change or update: "))
        
        if(self.index2>len(self.list1) or self.index2<0):
            print("!!!__ Please enter the valid index no. or task no. __!!!")

        else:
         self.newtask=str(input("\nWhat is your new updated task :- "))
         self.oldtask=self.list1[self.index2-1]
         self.list1.remove(self.oldtask)
         print(f"\n!!! Your Task {self.newtask} is under updating process !!! ")
         self.list1.insert(self.index2-1,self.newtask)
         print(f"\n!!! Your Task {self.newtask} has been updated !!! ")

    def save(self):
       print("\n!!! Your all tasks has been under saving process !!!")
       
       file1=open("Tasks.txt",'w')
       file1.write("")
       file1.close()
       file=open("Tasks.txt",'a')
       for i in range(0,len(self.list1)):
          file.write(self.list1[i])
          file.write("\n")

       print("\n!!! Your all Tasks has been saved Succesfully !!!") 
       file.close()
    def menu(self):
       while(self.choice!=5):
            print("\n|===== TO-DO LIST MENU =====|")
            print("\n1.Show Tasks\n2.Add Task\n3.Update Task\n4.Delete Task\n5.Save and Exit")
            self.choice=int(input("\nEnter your Choice (1 to 5) :- "))

            match(self.choice):
               case 1:
                  self.show()
                  exit
               case 2:
                 
                  self.add()
                  exit
               case 3:
                  self.update()
                  exit
               case 4:
                  print("\n|----- Your Scheduled Tasks -----|")
                  for i in range(0,len(self.list1)):
                     print(f"{i+1}. {self.list1[i]}")
                  self.index=int(input("\nEnter which task no. you have to Delete :- "))
                  if(self.index>len(self.list1) or self.index<0):
                     print("!!!__ Please enter the valid index no. or task no. __!!!")

                  else:
                     self.element=self.list1[self.index-1]
                     self.delete(self.element)
                  exit
               case 5:
                  self.save()
                  exit
               case _:
                  print("!!__ INVALID CHOICE __!!")
                  exit
T=ToDO()
T.fetch()
T.menu()
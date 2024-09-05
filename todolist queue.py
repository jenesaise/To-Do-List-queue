ToDoList = [""] * 10
Head = -1
Tail = -1

def Enqueue():
    global ToDoList, Head, Tail
    
    if  (Head == 0 and Tail == 9) or (Head == Tail + 1):
        print("To Do List Is Full...")
    else: 
        Task = input("Enter A Task To Do:")
    
        if Head == -1 and Tail == -1:
            Head = 0
            Tail = 0
        elif Tail == 9:
             Tail = 0
        else:
            Tail = Tail + 1
        ToDoList[Tail] = Task
        print("Task Successfully Added!")



def Dequeue():
    global ToDoList, Head, Tail 
    if Tail == -1 and Head == -1:
         print("To Do List Is Empty...")
    else:     
        ToDoList[Head] = ""
        if Head == Tail:
            Tail = -1
            Head = -1
        elif Head == 9:
            Head = 0
        else:
            Head = Head + 1 
        print("Task Successdully Removed!")




def Display():
    global ToDoList, Head, Tail
    print(ToDoList)
    print(f"Value of Head is: {Head}")
    print(f"Value of Tail is: {Tail}")

def Menu():
    global ToDoList, Head, Tail
    
    choice = 0
    while choice != 4: 
        print("1= Enqueue")
        print("2= Dequeue")
        print("3= Display")
        print("4= Exit")

        choice = int(input("Enter Your Choice:"))

        if choice == 1:
            Enqueue()
        elif choice == 2:
            Dequeue()
        elif choice == 3: 
            Display()
        elif choice == 4:
            print("Thank You For Using The To Do List!")
            break

        else:
            print("Invalid Choice Enterred...")

Menu()

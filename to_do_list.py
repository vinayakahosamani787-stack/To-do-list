print("<<<To-Do-List>>>")
def menu():
    print("1. Add Task\n2. View the Task\n3. Complete the Task\n4. Delete Task\n5. Exit")
tasks=[]
while True:
    menu()
    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Enter valid choice")
        continue
    if choice==1:
        task=input("Enter the Task: ")
        if task in tasks:
            print("Task already exists")
        else:
            tasks.append(task)
            print(f"Task Added:{tasks}")     
    elif choice==2:
        print(f"Tasks are:{tasks}")
        continue
    elif choice==3:
        print(f"Tasks:{tasks}")
        try:
            i=int(input("Enter the task index to complete: "))
        except ValueError:
            print("Enter valid index")
            continue
        if 0<=i<len(tasks):
            if "✅" in tasks[i]:
                print("Task is completed✅")
            else:
                tasks[i]=tasks[i]+" : ✅"
                print(tasks)
                continue
        else:
            print("Invalid index")
            continue
    elif choice==4:
        print(f"Tasks:{tasks}")
        try:
            rem=int(input("Enter the index of task to remove: "))
        except ValueError:
            print("Enter valid index")
            continue
        if 0<=rem<len(tasks):
            tasks.pop(rem)
            print(f"After the Task deleted:{tasks}")
            continue
        else:
            print("Invalid index")
            continue
    elif choice==5:
        print("Exit")
        break
    else:
        print("Invalid choice")
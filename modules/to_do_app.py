def use_to_do_app():
    import time
    tasks = []
    if not os.path.exists("to-do list.txt"):
        print(f"Previous To-Do List not found. Creating a new one.")
    else:
        with open("to-do list.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    task = line.split(".", 1)[-1] #only split on the very first ".", then stop and give me the 2nd half (the part after index)
                    tasks.append(task)
        completed_tasks = []
        with open("completed tasks.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    file_done_task = line.split(".", 1)[-1]
                    completed_tasks.append(file_done_task)
    
    while True:
        print('''
Todo List Menu:
1. View Tasks
2. Add Task
3. Remove Task
4. Mark Task as Completed
5. Save and Exit
6. Exit''')
        choice = input("\nEnter your choice: ")
        if choice == "1":
            if not tasks and not completed_tasks:
                print("\nThere are no tasks yet.")
                time.sleep(1)
            elif not completed_tasks:
                print("\n")
                for index,task in enumerate(tasks, start = 1):
                    time.sleep(0.3)
                    print(f"{index}. {task}")
            elif not tasks:
                print("\n")
                for index,task in enumerate(completed_tasks, start = 1):
                    time.sleep(0.3)
                    print(f"{index}. {task}")
            else:
                print("\n")
                for index,task in enumerate(tasks, start = 1):
                    time.sleep(0.3)
                    print(f"{index}. {task}")
                print("_____________________________________")
                print("Completed Tasks:")
                for index,task in enumerate(completed_tasks, start = 1):
                    time.sleep(0.3)
                    print(f"{index}. {task}")
            time.sleep(0.3)
        elif choice == "2":
            while True:
                add_task = input("\nEnter the task you want to add: ").strip()
                if add_task == "":
                    print("Task cannot be empty!")
                else:
                    tasks.append(add_task)
                    break
            time.sleep(1)
        elif choice == "3":
            if not tasks:
                print("\nThere are no tasks yet.")
                time.sleep(1)
            else:
                for index,task in enumerate(tasks, start = 1):
                    time.sleep(0.3)
                    print(f"{index}. {task}")
                while True:
                    try:
                        remove_task = int(input("\nEnter the index of the task you want to remove (1,2,...): "))
                        if remove_task <1 or remove_task>len(tasks):
                            print(f"Choose between 1 and {len(tasks)}.")
                        else:
                            del tasks[remove_task-1]
                            break
                    except:
                        print("\nEnter a valid index!")
        elif choice == "4":
            if not tasks:
                print("\nThere are no tasks yet.")
                time.sleep(1)
            else:
                for index,task in enumerate(tasks, start = 1):
                    time.sleep(0.3)
                    print(f"{index}. {task}")
                while True:
                    try:
                        complete_task = int(input("\nEnter the index of the task you want to mark as completed (1,2,...): "))
                        if complete_task <1 or complete_task>len(tasks):
                            print(f"Choose between 1 and {len(tasks)}.")
                        else:
                            task_done = tasks.pop(complete_task-1)
                            completed_tasks.append(task_done)
                            break
                    except:
                        print("\nEnter a valid index!")
        elif choice == "5":
            with open("to-do list.txt", "a") as file:
                for index,task in enumerate(tasks, start = 1):
                    file.write(f"{index}. {task}\n")       
            with open("completed tasks.txt", "a") as file2:
                for index,task in enumerate(completed_tasks,start =1):
                    file2.write(f"{index}. {task}")
            return
        elif choice == "6":
            return
        else:
            print("\nChoose between (1/2/3/4).")

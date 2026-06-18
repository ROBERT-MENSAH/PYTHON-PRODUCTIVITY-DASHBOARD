import time

while True:
    print("====== PERSONAL PRODUCTIVITY DASHBOARD =======")
    print("1. Countdown Timer")
    print("2. Number List Manager")
    print("3. Student Grade Manager")
    print("4. Exit")

    choice = int(input("Select your choice (1-4): "))

    # Countdown Timer
    if choice == 1:
        print("----- Countdown Timer SELECTED -----")
        while True:
            print("1. Start Countdown")
            print("2. Exit Countdown Timer")
            choice_count=int(input("Enter your choice:"))
            if choice_count==1:

                start = int(input("Enter start number: "))
                step = int(input("Enter step number: "))

                if start < 1:
                    print("Start must be positive")
                elif step < 1:
                 print("Step must be positive")
            
                current = start
                while current >= 0:
                    print(current)
                    time.sleep(1)
                    current -= step
                print("Countdown Completed!")
            elif choice_count==2:
                print("EXITED Countdown Timer. Goodbye!")
                break
            else:
                print("Invalid choice! Please select 1 or 2.")

    # Number List Manager
    elif choice == 2:
        print("----- Number List Manager SELECTED -----")
        number = []
        while True:
            print("NUMBER LIST MANAGER")
            print("1. View all members")
            print("2. Add members")
            print("3. Remove a number")
            print("4. Sort numbers (ascending)")
            print("5. View statistics")
            print("6. Clear all members")
            print("7. Exit")
            number = [float(num) for num in number]  # Convert all members to float

            sub_choice = int(input("Select a choice from the menu [1-7]: "))
            if sub_choice < 1 or sub_choice > 7:
                print("Select a number from 1-7")
            elif sub_choice == 1:
                if len(number) == 0:
                    print("List is Empty")
                else:
                    print("------CURRENT NUMBER LIST -------")
                    for i, num in enumerate(number, start=1):
                        print(f"{i}. {num}")
                
            elif sub_choice == 2:
                add = float(input("Enter a number you want to add: "))
                number.append(add)
                print(f"{add} has been added")
            elif sub_choice == 3:
                remove_num = float(input("Enter the number you want to remove: "))
                if remove_num in number:
                    number.remove(remove_num)
                    print(f"{remove_num} has been removed") 
                else:
                    print("Number not found")
            elif sub_choice == 4:
                number.sort()
                print("List sorted")
            elif sub_choice == 5:
                if len(number) == 0:
                    print("List is Empty")
                else:
                    print("------ STATISTICS -------")
                    print(number)
                    print(f"Total Count: {len(number)}")
                    print(f"Sum: {sum(number)}")
                    print(f"Average: {sum(number)/len(number)}")
                    print(f"Lowest Number: {min(number)}")
                    print(f"Highest Number: {max(number)}")
            elif sub_choice == 6:
                number.clear()
                print("All members cleared")
                print(number)
            elif sub_choice == 7:
                print("EXITED Number List Manager. Goodbye!")
                break

    # Student Grade Manager
    elif choice == 3:
        Dictionary = {}
        while True:
            print("\n--------- STUDENT GRADE POINT ----------")
            print("1. View all students & Grades")
            print("2. Add a student")
            print("3. Remove a student")
            print("4. Update a student's Grade")
            print("5. View class average")
            print("6. Find top student")
            print("7. Clear all students")
            print("8. Exit")

            sub_choice = int(input("Select an option: "))
            if sub_choice == 1:
                if len(Dictionary) == 0:
                    print("No Student Found!")
                else:
                    for i, (name, grade) in enumerate(Dictionary.items(), start=1):
                        print(f"{i}. {name}: {grade}")
            elif sub_choice == 2:
                name = input("Enter student's name: ")
                grade = float(input("Enter student's grade: "))
                Dictionary[name] = grade
                print(f"Student {name} with grade {grade} added")
            elif sub_choice == 3:
                delete = input("Enter student's name: ")
                if delete in Dictionary:
                    del Dictionary[delete]
                    print(f"{delete} removed")
                else:
                    print(f"{delete} NOT FOUND!")
            elif sub_choice == 4:
                update = input("Enter student's name: ")
                if update in Dictionary:
                    update_grade = float(input("Enter new grade: "))
                    Dictionary[update] = update_grade
                    print(f"{update} updated to {update_grade}")
                else:
                    print(f"{update} NOT FOUND!")
            elif sub_choice == 5:
                if len(Dictionary) == 0:
                    print("List is EMPTY")
                else:
                    average = sum(Dictionary.values()) / len(Dictionary)
                    print(f"Average grade: {average}")
            elif sub_choice == 6:
                if len(Dictionary) > 0:
                    high = max(Dictionary, key=Dictionary.get)
                    print(f"Top student: {high} with grade {Dictionary[high]}")
                else:
                    print("No students found")
            elif sub_choice == 7:
                Dictionary.clear()
                print("All students cleared")
            elif sub_choice == 8:
                print("EXITED Student Grade Manager. Goodbye!")
                break
            else:
                print("Invalid input!")

    # Exit
    elif choice == 4:
        print("EXITED!! Goodbye!")
        break
    else:
        print("CHOICE MUST BE WITHIN 1-4")

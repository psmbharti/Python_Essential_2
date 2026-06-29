# list_manager.py

numbers = []

while True:
    print("\n--- MENU ---")
    print("a. Add a number")
    print("b. Remove a number")
    print("c. Display the list")
    print("d. Quit")

    choice = input("Choose an option: ")

    if choice == "a":
        try:
            num = int(input("Enter an integer: "))
            numbers.append(num)
            print("Number added.")
        except ValueError:
            print("Error: Please enter a valid integer.")

    elif choice == "b":
        try:
            index = int(input("Enter index to remove: "))
            removed = numbers.pop(index)
            print("Removed:", removed)
        except ValueError:
            print("Error: Please enter a valid integer index.")
        except IndexError:
            print("Error: Invalid index. Try again.")

    elif choice == "c":
        print("Current list:", numbers)

    elif choice == "d":
        print("Exiting program...")
        break

    else:
        print("Invalid option. Please choose again.")
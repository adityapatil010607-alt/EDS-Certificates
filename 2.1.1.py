def main():
    numbers = []

    while True:
        print("1. Add")
        print("2. Remove")
        print("3. Display")
        print("4. Quit")

        choice = input("Enter choice: ")

        if choice == '1':  # Add
            value = input("Integer: ")
            try:
                num = int(value)
                numbers.append(num)
                print("List after adding:", numbers)
            except ValueError:
                print("Invalid input")

        elif choice == '2':  # Remove
            if not numbers:
                print("List is empty")
            else:
                value = input("Integer: ")
                try:
                    num = int(value)
                    if num in numbers:
                        numbers.remove(num)
                        print("List after removing:", numbers)
                    else:
                        print("Element not found")
                except ValueError:
                    print("Invalid input")

        elif choice == '3':  # Display
            if not numbers:
                print("List is empty")
            else:
                print(numbers)

        elif choice == '4':  # Quit
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

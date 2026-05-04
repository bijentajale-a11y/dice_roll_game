expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append((name, amount))

    elif choice == "2":
        for expense in expenses:
            print(f"{expense[0]} - Rs {expense[1]}")

    elif choice == "3":
        total = sum(expense[1] for expense in expenses)
        print(f"Total Expense: Rs {total}")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
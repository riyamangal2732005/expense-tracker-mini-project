#MINI PROJECT : EXPENSE TRACKER
expenses = []

while(True):
    print("----EXPENSE TRACKER-----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total expenses")
    print("4. Exit")

    choice = int(input("Enter your choice"))

    if choice == 1:
        name = input("Enter expense name : ")
        amt = float(input("Enter the amount : "))

        expenses.append([name, amt])
        print("Expense added successfully")

    elif choice == 2:
        print("Your expenses : ")
        for item in expenses:
            print(f"{item[0]} : Rs. {item[1]}")

    elif choice == 3:
        total = 0
        for item in expenses:
            total += item[1]

        print("Total expense : Rs ", total)

    elif choice == 4:
        print("Thankyou! You are exiting Expense TRcaker")
        break

    else:
        print("Invalid choice! Pls try again")
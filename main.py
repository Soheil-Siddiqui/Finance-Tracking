from expense_manager import ExpenseManager
from data_manager import DataManager

def main():
    DataManager.get_instance().load_from_file()
    expense_manager = ExpenseManager()

    while True:
        print("\n==== Finance Tracker Menu ====")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. Show All Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            expense_manager.add_expense()
        elif choice == "2":
            expense_manager.delete_expense()
        elif choice == "3":
            expense_manager.show_expenses()
        elif choice == "4":
            print("Exiting program. Goodbye.")
            break
        else:
            print("Invalid input. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

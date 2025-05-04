from expense import ExpenseFactory
from data_manager import DataManager
from input_validator import InputValidator

class ExpenseManager:
    def __init__(self):
        self.manager = DataManager.get_instance()

    def add_expense(self):
        try:
            print("\nAvailable types: Food, Travel, Utility, Personal")
            exp_type = input("Enter expense type: ").strip().capitalize()

            valid_types = ["Food", "Travel", "Utility", "Personal"]
            if exp_type not in valid_types:
                raise ValueError("Invalid type. Choose from Food, Travel, Utility, Personal.")

            amount = InputValidator.get_float_input("Enter amount: ")

            category = None
            if exp_type == "Food":
                print("Choose category: Lunch, Dinner, Snacks, Groceries")
                category = input("Enter category: ").strip().capitalize()
                if category not in ["Lunch", "Dinner", "Snacks", "Groceries"]:
                    raise ValueError("Invalid Food category.")
            elif exp_type == "Travel":
                print("Choose category: Taxi, Bus, Train, Flight")
                category = input("Enter category: ").strip().capitalize()
                if category not in ["Taxi", "Bus", "Train", "Flight"]:
                    raise ValueError("Invalid Travel category.")
            elif exp_type == "Utility":
                print("Choose category: Electricity, Water, Phone Bill, Washing Machine")
                category = input("Enter category: ").strip().capitalize()
                if category not in ["Electricity", "Water", "Phone bill", "Washing machine"]:
                    raise ValueError("Invalid Utility category.")

            date = InputValidator.get_date_input("Enter date (YYYY-MM-DD): ")

            new_id = self.manager.get_next_id()
            expense = ExpenseFactory.create_expense(exp_type, new_id, amount, category, date)

            self.manager.add_expense(expense)
            self.manager.save_to_file()
            print("Expense added successfully.")

        except Exception as e:
            print(f"Error: {e}. Expense not saved. Please try again.")

    def delete_expense(self):
        expense_id = InputValidator.get_int_input("Enter expense ID to delete: ")
        success = self.manager.delete_expense(expense_id)
        if success:
            self.manager.save_to_file()
            print("Expense deleted successfully.")
        else:
            print("Expense ID not found.")

    def show_expenses(self):
        print("\n--- Show Expenses ---")
        print("Sort by:")
        print("1. Date")
        print("2. Type")
        print("3. Default (no sorting)")

        choice = input("Choose sorting method (1-3): ").strip()

        expenses = self.manager.get_all_expenses()

        if choice == "1":
            expenses.sort(key=lambda e: e.get_details()["date"])
        elif choice == "2":
            expenses.sort(key=lambda e: e.get_details()["type"])
        elif choice != "3":
            print("Invalid choice. Showing default order.")

        if not expenses:
            print("No expenses recorded.")
        else:
            for e in expenses:
                print(e.get_details())


import json
from expense import ExpenseFactory

class DataManager:
    _instance = None

    def __init__(self):
        if DataManager._instance is not None:
            raise Exception("Use get_instance() instead of constructor.")
        self._expenses = []

    @staticmethod
    def get_instance():
        if DataManager._instance is None:
            DataManager._instance = DataManager()
        return DataManager._instance

    def load_from_file(self, filename="expenses.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for item in data:
                    expense = ExpenseFactory.create_expense(
                        item["type"],
                        item["id"],
                        item["amount"],
                        item.get("category"),
                        item["date"]  # still a string, will be parsed later if needed
                    )
                    self._expenses.append(expense)
        except FileNotFoundError:
            self._expenses = []
        except json.JSONDecodeError:
            print("Error reading the JSON file. Starting with an empty list.")
            self._expenses = []

    def save_to_file(self, filename="expenses.json"):
        with open(filename, "w") as f:
            json.dump([e.get_details() for e in self._expenses], f)

    def add_expense(self, expense):
        self._expenses.append(expense)

    def delete_expense(self, expense_id):
        before = len(self._expenses)
        self._expenses = [e for e in self._expenses if e.get_id() != expense_id]
        return before != len(self._expenses)

    def show_expenses(self):
        if not self._expenses:
            print("No expenses recorded.")
        else:
            for e in expenses:
                d = e.get_details()
                print(f"{'-'*40}")
                print(f"ID       : {d['id']}")
                print(f"Type     : {d['type']}")
                print(f"Amount   : ${d['amount']:.2f}")
                if d['category']:
                    print(f"Category : {d['category']}")
                else:
                    print(f"Category : None")
                print(f"Date     : {d['date']}")
            print(f"{'-'*40}")

    
    def get_all_expenses(self):
        return self._expenses

    def get_next_id(self):
        return max([e.get_id() for e in self._expenses], default=0) + 1

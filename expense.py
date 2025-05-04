from abc import ABC, abstractmethod

class Expense(ABC):
    def __init__(self, id, amount, category, date):
        self._id = id
        self._amount = amount
        self._category = category
        self._date = date

    @abstractmethod
    def get_details(self):
        pass

    def get_id(self):
        return self._id

class FoodExpense(Expense):
    def get_details(self):
        return {
            "id": self._id,
            "type": "Food",
            "amount": self._amount,
            "category": self._category,
            "date": str(self._date)
        }

class TravelExpense(Expense):
    def get_details(self):
        return {
            "id": self._id,
            "type": "Travel",
            "amount": self._amount,
            "category": self._category,
            "date": str(self._date)
        }

class UtilityExpense(Expense):
    def get_details(self):
        return {
            "id": self._id,
            "type": "Utility",
            "amount": self._amount,
            "category": self._category,
            "date": str(self._date)
        }

class PersonalExpense(Expense):
    def get_details(self):
        return {
            "id": self._id,
            "type": "Personal",
            "amount": self._amount,
            "category": None,
            "date": str(self._date)
        }

class ExpenseFactory:
    @staticmethod
    def create_expense(expense_type, id, amount, category, date):
        if expense_type == "Food":
            return FoodExpense(id, amount, category, date)
        elif expense_type == "Travel":
            return TravelExpense(id, amount, category, date)
        elif expense_type == "Utility":
            return UtilityExpense(id, amount, category, date)
        elif expense_type == "Personal":
            return PersonalExpense(id, amount, None, date)
        else:
            raise ValueError("Unsupported expense type")

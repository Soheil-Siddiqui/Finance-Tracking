## Finance Tracker

## Overview
This is a **modular, object-oriented Python application** to help users track their personal expenses. The program reads from and writes to a JSON file and allows users to:

- Add new expenses  
- Delete existing expenses  
- View all recorded expenses with sorting options  

The application uses all **4 Object-Oriented Programming (OOP) pillars**, implements **two design patterns**, and handles errors gracefully with **exception handling** and **manual input validation**.

---

## Features

### 1. Expense Types Supported
- **Food**: Lunch, Dinner, Snacks, Groceries  
- **Travel**: Taxi, Bus, Train, Flight  
- **Utility**: Electricity, Water, Phone Bill, Washing Machine  
- **Personal**: No category needed

Each expense includes:
- Unique ID
- Type
- Category (optional)
- Amount
- Date (as a string in `YYYY-MM-DD` format)

---

### 2. Functionalities

| Feature          | Description                                                                |
|------------------|----------------------------------------------------------------------------|
| Add Expense      | Prompts user for expense details and saves valid input to a JSON file     |
| Delete Expense   | Removes an expense by its ID                                               |
| Show Expenses    | Displays all expenses, sorted by date, type, or unsorted                  |
| File I/O         | Reads initial fake data from `expenses.json` and updates it after changes |

---

## Object-Oriented Concepts Used

| OOP Concept    | Description                                                                    |
|----------------|--------------------------------------------------------------------------------|
| Abstraction     | Abstract base class `Expense` provides a common structure                     |
| Inheritance     | `FoodExpense`, `TravelExpense`, etc. inherit from the `Expense` class         |
| Polymorphism    | All subclasses implement a shared method `get_details()`                      |
| Encapsulation   | Internal fields like `_amount` and `_date` are private                        |

---

## Design Patterns Used

| Pattern            | Description                                                            |
|--------------------|------------------------------------------------------------------------|
| Factory Pattern    | `ExpenseFactory` creates different expense objects based on user input |
| Singleton Pattern  | `DataManager` ensures only one instance manages data access            |

---

## File Structure

- main.py                  # Main program and user menu interface

- base.py                  # Defines BaseExpense (abstract class)

- food_expense.py          # FoodExpense class

- travel_expense.py        # TravelExpense class

- utility_expense.py       # UtilityExpense class

- personal_expense.py      # PersonalExpense class

- factory.py               # ExpenseFactory for creating expense objects

- expense_manager.py       # Handles add, delete, and display logic

- file_handler.py          # Reads from and writes to expenses.json

- validator.py             # Input validation (amount, date, etc.)

- expenses.json            # JSON file for storing expense data

- README.md                # Documentation for the project

---

## Conclusion

This finance tracker project was built to show how object-oriented programming can be used in a simple but realistic way. It covers all four key OOP concepts abstraction, inheritance, polymorphism, and encapsulation through a clear and modular structure. Different expense types like food, travel, utility, and personal are handled using classes and categories, which makes the program flexible and easy to understand.

Design patterns like Factory and Strategy were used to keep the code organized and easy to maintain. Data is stored in a JSON file, so it's persistent even after the program is closed. The program also includes basic error handling to guide users when they make mistakes.

Overall, this project is a solid starting point for learning how to manage data using OOP in Python and can be expanded with more features like reports, filters, or even a simple user interface.


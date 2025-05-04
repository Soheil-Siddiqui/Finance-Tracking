# Finance Tracker

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


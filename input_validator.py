class InputValidator:
    @staticmethod
    def get_float_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    @staticmethod
    def get_int_input(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter an integer.")

    @staticmethod
    def get_date_input(prompt):
        while True:
            date_str = input(prompt)
            if InputValidator.is_valid_date_format(date_str):
                return date_str
            else:
                print("Invalid date format. Use YYYY-MM-DD.")

    @staticmethod
    def is_valid_date_format(date_str):
        if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
            return False
        year, month, day = date_str[:4], date_str[5:7], date_str[8:]
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return False
        if not (1 <= int(month) <= 12):
            return False
        if not (1 <= int(day) <= 31):
            return False
        return True

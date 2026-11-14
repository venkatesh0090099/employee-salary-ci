def calculate_bonus(salary):
    return salary * 0.20


def calculate_total_salary(salary):
    bonus = calculate_bonus(salary)
    return salary + bonus


def check_salary(salary):
    if salary < 0:
        return "Invalid Salary"
    else:
        return "Valid Salary"
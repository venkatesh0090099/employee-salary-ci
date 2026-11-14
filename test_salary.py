from salary import (
    calculate_bonus,
    calculate_total_salary,
    check_salary
)

def test_bonus():
    assert calculate_bonus(20000) == 2000

def test_total_salary():
    assert calculate_total_salary(20000) == 22000

def test_salary_validation():
    assert check_salary(25000) == "Valid Salary"

def test_invalid_salary():
    assert check_salary(-5000) == "Invalid Salary"

def test_zero_salary():
    assert check_salary(0) == "Valid Salary"

def test_bonus_for_50000():
    assert calculate_bonus(50000) == 5000
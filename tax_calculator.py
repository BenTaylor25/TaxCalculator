from float_input import float_input
from income_tax import calc_income_tax
from national_insurance import calc_nat_ins
from salary_sacrifice import calc_salary_sacrifice

def tax_calculator(salary: float):
    gross = salary
    salary_sacrifice = calc_salary_sacrifice(gross)
    subtotal = salary - salary_sacrifice

    income_tax = calc_income_tax(subtotal)
    nat_ins = calc_nat_ins(subtotal)

    return subtotal - income_tax - nat_ins


if __name__ == "__main__":
    salary = float_input("Yearly Salary: ")

    tax_calculator(salary)

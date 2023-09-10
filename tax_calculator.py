from float_input import float_input
from income_tax import calc_income_tax
from national_insurance import calc_nat_ins


def tax_calculator(salary: float):
    income_tax = calc_income_tax(salary)
    nat_ins = calc_nat_ins(salary)

    return salary - income_tax - nat_ins


if __name__ == "__main__":
    salary = float_input("Yearly Salary: ")

    tax_calculator(salary)

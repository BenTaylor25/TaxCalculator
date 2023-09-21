from float_input import float_input
from format_currency import cur

from income_tax import calc_income_tax
from employee_national_insurance import calc_employee_national_insurance
from company_national_insurance import calc_company_national_insurance
from salary_sacrifice import calc_salary_sacrifice

def tax_calculator(salary: float):
    gross = salary
    salary_sacrifice = calc_salary_sacrifice(gross)
    subtotal = salary - salary_sacrifice

    print(f"Gross: {cur(gross)}")
    print()

    print(f"Salary Sacrifice: {cur(salary_sacrifice)}")
    print(f"Subtotal: {cur(subtotal)}")
    print()

    income_tax = calc_income_tax(subtotal)
    print()

    employee_national_insurance = calc_employee_national_insurance(subtotal)
    print()

    employee_net = subtotal - income_tax - employee_national_insurance
    print(f"Employee Net: {cur(employee_net)}")
    print("\n~\n")

    # ~

    print(f"Employee Salary: {cur(gross)}")

    company_national_insurance = calc_company_national_insurance(gross)
    company_total_cost = gross + company_national_insurance
    print(f"Company Cost: {cur(company_total_cost)}")
    print()


    return subtotal - income_tax - employee_national_insurance


if __name__ == "__main__":
    salary = float_input("Yearly Salary: ")

    tax_calculator(salary)

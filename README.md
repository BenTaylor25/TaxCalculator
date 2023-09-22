# UK Tax Calculator 2023/24

Tax is complicated.
There are loads of different rules that override each other,
and different resources will differ on details.

Though I have spoken to accountants during the development
of this calculator, **I am not an accountant**.
This program was initially created to help me understand how
Salary Sacrifice works (with Income Tax and National Insurance
being a prerequisite).  
**My aim in releasing this is not to offer a tool for real
calculations**, but rather to help people to understand how
tax works.

For all of the values I have tested, my calculations align with this site: https://listentotaxman.com/  
(Please raise an issue in the [Issues](https://github.com/BenTaylor25/TaxCalculator/issues) tab if you find an input that gives a different output).


## The 'Basics'

If you are working a job with an annual salary of £100,000,
you don't actually see £100,000 in your bank account every year.

Income Tax and National Insurance are deducted from your 'gross' 100k.

`Take_Home = Gross_Salary - Income_Tax - Employee_National_Insurance`  
With a Gross Salary of £100,000 this is about `£67,053.00`.

Not only that, but your employment will cost your company more than £100,000.
This is because companies also have to pay National Insurance, however the
company's National Insurance contribution is calculated differently.

`Company_Cost = Gross_Salary + Company_National_Insurance`  
With a Gross Salary of £100,000 this is about `£112,544.20`.

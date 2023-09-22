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


## Income Tax

### Tax Bands

The government website (https://www.gov.uk/income-tax-rates) suggests the following:

Unfortunately it is nowhere near as simple as this.

These bands are dependent on your Tax Band
(https://www.gov.uk/tax-codes/what-your-tax-code-means).  
Your Tax Band is determined by a number of factors; examples:
1. If you have multiple sources of income, they will use different bands.
1. If you are married you can 'donate' excess tax-free allowance to your partner.

The Tax Code that applies to most people is `1257L`,
which corresponds to the table above, however it gets more difficult still.  
The "1257" refers to the tax-free allowance (£12,570),
but the rather than a single value (£12,570),
`1257L` represents the range £12,570 - £12579.  
I don't understand why this is, but the implication is that
*some* of the bands from the table above are shifted.

In order to align the numbers in this calculator with the ListenToTaxman site,
I had to use an offset of 9 (I've used £12,579 instead of £12,570).

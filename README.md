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

### Tax-free Allowance
The first £12,570\* of your salary is tax-free\*. This is known as your Personal Allowance.

\* The £12,570 is actually *between £12,570 and £12,579*, and isn't the case for everyone (just most people) - more on this in the Tax Bands section.

\* If your Gross is over £100,000 per year, this decreases. For every £2 over £100k, your Personal Allowance decreases by £1. *Note: if you earn £100,003, your PA decreases by £1, not £1.50 - it is step-based, not ratio-based if this helps.*

If you are blind, or partially-sighted, you can receive a Blindness Allowance. I'm not sure how this is calculated, but this seems to be where it applies.

`Tax_Free_Allowance = Personal_Allowance + Blindness_Allowance`

### Tax Bands

The government website (https://www.gov.uk/income-tax-rates) suggests the following:  
![image](https://github.com/BenTaylor25/TaxCalculator/assets/97246704/4d21e5b9-1504-4b30-9a83-8ab77aacf398)  
Unfortunately it is nowhere near as simple as this.

These bands are dependent on your Tax Code
(https://www.gov.uk/tax-codes/what-your-tax-code-means).  
Your Tax Code is determined by a number of factors; examples:
1. If you have multiple sources of income, they will use different Codes.
1. If you are married and have a Gross Salary less than `£12,570` you can 'donate' excess Personal Allowance to your partner so that they pay less tax - this is done through changes in Tax Code.

The Tax Code that applies to most people is `1257L`,
which corresponds to the table above, however it gets more difficult still.  
The "1257" refers to the Tax Code's Personal Allowance (£12,570),
but the rather than an actual value (£12,570),
`1257L` represents the range £12,570 - £12579.  
I don't understand why this is, but the implication is that
*some* of the bands from the table above are shifted.

In order to align the numbers in this calculator with the ListenToTaxman site,
I had to use an offset of 9 (I've used £12,579 instead of £12,570).

Even more confusingly, when your Personal Allowance decreases, you pay the newly taxable amount at Higher Rate.  
In other words, notice that the Basic Rate band has a range of £37,700 (£50,270 - £12,570). This range stays the same for salaries over £100k.  
Let's look at an example:
```
Gross_Salary = £110,000
PERSONAL_ALLOWANCE_MAX = £12,579

Gross_Over_100k = Gross_Salary - £100,000 (if Gross_Salary > £100,000, otherwise 0)
    = £10,000
PA_Loss = round_down(Gross_Over_100k / 2)
    = £5,000
Personal_Allowance = PERSONAL_ALLOWANCE_MAX - PA_Loss
    = £12,579 - £5,000
    = £7,579
Blind_Allowance = 0
Tax_Free_Allowance = Personal_Allowance + Blind_Allowance
    = £7,579 + £0
    = £7,579

Bands Formula:
£0 - Tax_Free_Allowance at 0%
Tax_Free_Allowance - (50,279 - PA_Loss) at 20%
(50,279 - PA_Loss) - £125,140 at 40%
>£125,140 at 45%

Bands:
£0 - £7,579 at 0%
£7,579 - $45,279 at 20%
£45,279 - £125,140 at 40%
>£125,140 at 45%
```
(All-caps values mean independent of Gross_Salary).



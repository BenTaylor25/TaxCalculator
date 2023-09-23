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
£125,140+ at 45%

Bands:
£0 - £7,579 at 0%
£7,579 - £45,279 at 20%
£45,279 - £125,140 at 40%
£125,140+ at 45%
```
(All-caps values mean independent of Gross_Salary).

## Income Tax Calculation

That's the hard part of Income Tax out of the way, but we still need to add up the numbers.  
You may or may not find this intuitive, but I found that this diagram helps.
![image](https://github.com/BenTaylor25/TaxCalculator/assets/97246704/79716322-d07f-4318-b154-6d0e787041ee)  
*(not to scale)*

We can clearly see from this that we have £7,579 in the 0% band.  
0% of £7,579 is £0.

The amount in the 20% band is the `Band_Max - Band_Min`.  
£45,279 - £7,579 = £37,700.  
This means that we have £37,700 in this band.  
20% of £37,700 is £7,540.

The amount in the 40% band is calculated slightly differently because the Gross_Salary is less than the `Band_Max`.  
We use `Gross_Salary - Band_Min`.  
Or in general `min(Gross_Salary, Band_Max) - Band_Min`.  
£110,000 - £45,279 = £64,721.  
So we have £64,721 in the 40% band.  
40% of £64,721 is £25,888.40.

Since the Gross_Salary is less than the 45% Band_Min, our general formula from above will give us a negative number (which is not right) - to fix this, we can take the larger of the value and 0.  
`max(0, min(Gross_Salary, Band_Max) - Band_Min)`.  
We have £0 in the 45% band.
45% of £0 is £0.

Our total Income Tax payment is the sum of these bands:  
£0 + £7,540 + £25,888.40 + £0 = £33,428.40.

If you run the calculator program with the input `£110,000` you will see the same figures:  
![image](https://github.com/BenTaylor25/TaxCalculator/assets/97246704/098c461a-3d10-483b-a316-8d492a4ae5ef)


## Employee National Insurance

### Categories

On top of Income Tax, employees also have to pay a National Insurance contribution.

National Insurance has Classes/Categories - similar to Income Tax codes.  
https://www.gov.uk/national-insurance-rates-letters/category-letters

There are many different NI Categories, but the most common is A.  
Not only this, but a few other codes have the same rates as A
(at least for Employee NI), e.g.  
1. H - Apprentices under 25,
1. M - Employees under 21,
1. V - Employees whose previous role was in the armed forces.

https://www.gov.uk/national-insurance-rates-letters  

These classes pay:
```
£0 - £12,570 at 0%
£12,570 - £50,270 at 12%
£50,270+ at 2%
```
*Note: the Income Tax offset of 9 that we were using before doesn't
apply here even though the base band numbers are the same.*

National Income is calculated based on `Gross_Salary`,
not (`Gross_Salary` - `Income_Tax`).

### Calculation

The National Insurance calculation is done in the same way as Income Tax.  
Let's continue with the `£110,000` Gross Salary example:

Gross_Salary = £110,000

Gross_Salary > £12,570, so we reach the 12% band.  
Gross_Salary > £50,270, so we use `Band_Max` - `Band_Min` to get the amount in the band.

Twelve_Percent_Band_Amount = £50,270 - £12,570  
    = £37,700  
NI_At_Twelve_Percent = Twelve_Percent_Band_Amount * 0.12  
    = £4,524

Gross_Salary > £50,270, so we reach the 2% band.  
The 2% band is the top band, so we use `Gross_Salary` - `Band_Min` to get the amount in the band.

Two_Percent_Band_Amount = £110,000 - £50,270  
    = £59,730  
NI_At_Two_Percent = Two_Percent_Band_Amount * 0.02  
    = £1,194.60

Again, the total National Insurance Payment is the sum of
the band values.  
£4,524 + £1,194.60 = £5,718.60

And if we check this against the program, the numbers once again align.  
![image](https://github.com/BenTaylor25/TaxCalculator/assets/97246704/36f3eab7-1b5c-4cb9-ba13-c08cc577660b)


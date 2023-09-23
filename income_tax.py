from format_currency import cur

BASIC_RATE = 0.2 # 20%
HIGHER_RATE = 0.4 # 40%
ADDITIONAL_RATE = 0.45 #45%

TAX_CODE_OFFSET = 9

PERSONAL_ALLOWANCE_MAX = 12_570 + TAX_CODE_OFFSET
BASIC_CONST = 50_270 + TAX_CODE_OFFSET
HIGHER_CONST = 125_140

def get_tax_bands(tfa):
    return {
        "allowance": {
            "band_min": 0,
            "band_max": tfa,
            "band_rate": 0
        },
        "basic": {
            "band_min": tfa,
            "band_max": BASIC_CONST - (PERSONAL_ALLOWANCE_MAX - tfa),
            "band_rate": BASIC_RATE
        },
        "higher": {
            "band_min": BASIC_CONST - (PERSONAL_ALLOWANCE_MAX - tfa),
            "band_max": HIGHER_CONST,
            "band_rate": HIGHER_RATE
        },
        "additional": {
            "band_min": HIGHER_CONST,
            "band_max": float('inf'),
            "band_rate": ADDITIONAL_RATE
        },
    }

def calc_personal_allowance(gross: float) -> float:
    personal_allowance = PERSONAL_ALLOWANCE_MAX

    # decrease personal_allowance by gross_over_100k / 2
    # (but don't go below 0)
    if gross > 100_000:
        gross_over_100k = gross - 100_000
        personal_allowance = max(0, PERSONAL_ALLOWANCE_MAX - gross_over_100k//2)

    return personal_allowance


def calc_income_tax(gross: float, debug_mode: bool = True) -> float:
    personal_allowance = calc_personal_allowance(gross)
    blind_allowance = 0

    tax_free_allowance = personal_allowance + blind_allowance

    total_tax = 0

    tax_bands = get_tax_bands(tax_free_allowance)
    gross_so_far = 0
    for b in tax_bands:
        band = tax_bands[b]
        amount_in_band = min(gross - gross_so_far, band["band_max"] - band["band_min"])
        print(f"Amount in Band {int(band['band_rate']*100)}%: {cur(amount_in_band)}")
        gross_so_far += amount_in_band

        tax_from_band = amount_in_band * band["band_rate"]

        total_tax += tax_from_band

        print(f"Income Tax ({int(band['band_rate']*100)}%) - {cur(tax_from_band)}")

    print(f"Income Tax: {cur(total_tax)}")

    return total_tax


def test_income_tax(gross: float):
    gross_str = f"£{gross:,.2f}"
    print(gross_str)
    print("-" * len(gross_str))

    total_tax = calc_income_tax(gross, True)
    total_keep = gross - total_tax

    print("~")
    print(f"Tax: £{total_tax:,.2f}")
    print(f"Keep: £{total_keep:,.2f}")
    input("[press enter to continue]")
    print()

if __name__ == "__main__":
    test_income_tax(10_000)
    test_income_tax(20_000)
    test_income_tax(50_000)
    test_income_tax(75_000)
    test_income_tax(105_000)
    test_income_tax(150_000)

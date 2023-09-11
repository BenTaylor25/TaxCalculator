from format_currency import cur

TAX_OFFSET = 9

ALLOWANCE_CONST = 12_570
BASIC_CONST = 50_270
HIGER_CONST = 125_140

get_tax_bands = lambda tfa : {
    "allowance": {
        "band_min": 0,
        "band_max": tfa + TAX_OFFSET,
        "band_rate": 0
    },
    "basic": {
        "band_min": tfa + TAX_OFFSET,
        "band_max": BASIC_CONST + TAX_OFFSET,
        "band_rate": 0.2
    },
    "higher": {
        "band_min": BASIC_CONST + TAX_OFFSET,
        "band_max": HIGER_CONST,
        "band_rate": 0.4
    },
    "additional": {
        "band_min": HIGER_CONST,
        "band_max": float('inf'),
        "band_rate": 0.45
    }
}

def calc_personal_allowance(subtotal: float) -> float:
    gross_over_100k = max(0, subtotal - 100_000)
    personal_allowance = max(0, ALLOWANCE_CONST - (gross_over_100k // 2))
    return personal_allowance

def calc_income_tax(subtotal: float):
    personal_allowance = calc_personal_allowance(subtotal)
    blind_allowance = 0

    tfa = personal_allowance + blind_allowance

    tax_bands = get_tax_bands(tfa)

    income_tax = 0
    subtotal_so_far = 0
    for b in tax_bands:
        band = tax_bands[b]

        amount_in_band = min(subtotal - subtotal_so_far, band["band_max"] - band["band_min"])
        subtotal_so_far += amount_in_band
        income_tax += amount_in_band * band["band_rate"]

    return income_tax

if __name__ == "__main__":
    print(cur(calc_income_tax(150_000)))
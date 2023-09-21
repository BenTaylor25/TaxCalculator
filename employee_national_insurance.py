from format_currency import cur

BAND_ONE_RATE = 0
BAND_ONE_MAX = 12_570

BAND_TWO_RATE = 0.12 # 12%
BAND_TWO_MAX = 50_270

BAND_THREE_RATE = 0.02 # 2%

bands = [
    {
        "band_min": 0,
        "band_max": BAND_ONE_MAX,
        "band_rate": BAND_ONE_RATE
    },
    {
        "band_min": BAND_ONE_MAX,
        "band_max": BAND_TWO_MAX,
        "band_rate": BAND_TWO_RATE
    },
    {
        "band_min": BAND_TWO_MAX,
        "band_max": float('inf'),
        "band_rate": BAND_THREE_RATE
    },
]

def calc_employee_national_insurance(subtotal: float) -> float:
    subtotal_so_far = 0
    nat_ins = 0

    for band in bands:
        amount_in_band = min(subtotal - subtotal_so_far, band["band_max"] - band["band_min"])
        subtotal_so_far += amount_in_band
        nat_ins_in_band = amount_in_band * band["band_rate"]
        
        nat_ins += nat_ins_in_band

        print(f"Employee NI ({int(band['band_rate'] * 100)}%) - {cur(nat_ins_in_band)}")

    print(f"Employee NI: {cur(nat_ins)}")

    return nat_ins

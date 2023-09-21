from format_currency import cur

COMP_NAT_INS_THRESHOLD = 9_100
COMP_NAT_INS_RATE = 0.138 # 13.8%

def calc_comp_nat_ins(gross: float) -> float:
    gross_over_threshold = max(0, gross - COMP_NAT_INS_THRESHOLD)
    nat_ins = gross_over_threshold * COMP_NAT_INS_RATE

    print(f"Company National Insurance: {cur(nat_ins)}")
    return nat_ins

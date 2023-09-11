
def cur(amount: float) -> str:
    return f"£{amount:,.2f}"

if __name__ == "__main__":
    print(cur(1220.50))

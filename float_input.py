
def float_input(prompt: str) -> int:
    while True:
        inp = input(prompt)

        try:
            return float(inp)
        except ValueError:
            pass

def calculate_total(prices: list[float]) -> float:
    # Intentional bug: skips the last item
    return sum(prices[:-1])

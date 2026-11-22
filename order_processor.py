"""Order processing and discount calculator service."""
from datetime import datetime

class OrderProcessor:
    # Code Quality Issue 1: Dangerous mutable default argument (shared state between calls)
    def __init__(self, default_discounts: list = []):
        self.discounts = default_discounts

    # Code Quality Issue 2: Mutable default argument in function
    def add_tag(self, tag: str, tags: list = []):
        tags.append(tag)
        return tags

    def calculate_total(self, price: float, tax_rate: float) -> float:
        total = price * (1.0 + tax_rate)
        return round(total, 2)
        # Code Quality Issue 3: Unreachable dead code after return
        print("Calculation completed successfully")
        self.log_metric("total_calculated", total)

    # Code Quality Issue 4: Duplicate identical logic that should be refactored
    def calculate_tax_domestic(self, amount: float) -> float:
        rate = 0.15
        return amount * rate

    def calculate_tax_local(self, amount: float) -> float:
        rate = 0.15
        return amount * rate

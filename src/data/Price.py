from enum import Enum

class PriceAnimation(Enum):
    FLYIN = 0
    ROTATING = 1

class NormalPriceTypes(Enum):
    # Values are used for wighting prices
    FIRST = 3
    SECOND = 2
    THIRD = 1


PRICE_NAMES: {NormalPriceTypes: str} = {
    NormalPriceTypes.THIRD: "3. Platz",
    NormalPriceTypes.SECOND: "2. Platz",
    NormalPriceTypes.FIRST: "1. Platz"
}

NO_PRICE_NAME = "Keiner"
SPECIAL_PRICE_NAME = "Sonderpreis"


class Price:

    def __init__(self, has_special_price: bool, normal_price: NormalPriceTypes | None):
        self.has_special_price = has_special_price
        self.normal_price = normal_price

    def get_name(self, seperator: str = " + "):
        concat = []
        if self.normal_price is not None:
            concat.append(PRICE_NAMES[self.normal_price])

        if self.has_special_price:
            concat.append(SPECIAL_PRICE_NAME)

        if len(concat) <= 0:
            concat.append(NO_PRICE_NAME)

        return seperator.join(concat)


PRICES = [
    Price(False, None),  # None
    Price(True, None),  # Special
    Price(False, NormalPriceTypes.FIRST),  # First
    Price(False, NormalPriceTypes.SECOND),  # Second
    Price(False, NormalPriceTypes.THIRD),  # Third
    Price(True, NormalPriceTypes.FIRST),  # First + Special
    Price(True, NormalPriceTypes.SECOND),  # Second + Special
    Price(True, NormalPriceTypes.THIRD),  # Third + Special
]

DEFAULT_PRICE = PRICES[0]

# Generates a score based on the given price
def score_price(price: Price):
    # Base score from the special price
    score = 1 if price.has_special_price else 0

    # Appends normal price-score times then
    if price.normal_price is not None:
        score += price.normal_price.value * 10

    return score

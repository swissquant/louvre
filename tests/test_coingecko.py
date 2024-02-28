import os
from dotenv import load_dotenv
from louvre.coingecko import Coingecko

load_dotenv()

coingecko = Coingecko(os.getenv("COINGECKO_API_KEY"))


def test_fetch_historical_prices():
    prices = coingecko.fetch_historical_prices("cryptopunks")
    print(prices.keys())
    print(prices["floor_price_native"])

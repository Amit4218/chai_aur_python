chai_prices = {
    "masala": 100,
    "lemon": 300,
    "normal": 50,
}


chai_prices_in_usd = {tea:price / 80 for tea, price in chai_prices.items()}
print(chai_prices_in_usd)
# Created by Admin at 5/8/2022
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))

prices1 = {'AAA': 45.23, 'ZZZ': 45.23}
min_price1 = min(zip(prices1.values(), prices1.keys()))

prices2 = {'AAA': 45.23, 'ZZZ': 45.23, 'AAPL': 612.78}
prices_sorted2 = sorted(zip(prices2.values(), prices2.keys()), reverse=True)

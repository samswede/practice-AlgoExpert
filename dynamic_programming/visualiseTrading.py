
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def ExtractBoundariesOfIncreasingSubsequences_final(arr):
    if not arr:
        return []

    boundaries = []
    start = 0  # Change from storing the start price to start index

    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            if arr[start] != arr[i - 1]:
                boundaries.append([arr[start], start, arr[i - 1], i - 1])  # Store price and index
            start = i

    if arr[start] != arr[-1]:
        boundaries.append([arr[start], start, arr[-1], len(arr) - 1])

    return boundaries


def maxProfitWithKTransactions_final(prices, k):
    if not len(prices):
        return 0, []

    boundaryPrices = ExtractBoundariesOfIncreasingSubsequences_final(prices)
    if not boundaryPrices:
        return 0, []

    evenProfits = [0 for _ in boundaryPrices]
    oddProfits = [0 for _ in boundaryPrices]
    transactions = [[] for _ in range(k)]  # Initialize transactions for each transaction number

    for t in range(1, k + 1):
        maxThusFar = float("-inf")
        currentTransactions = None

        if t % 2 == 1:
            currentProfits, previousProfits = oddProfits, evenProfits
        else:
            currentProfits, previousProfits = evenProfits, oddProfits

        for d in range(1, len(boundaryPrices)):
            buyPrice, buyIndex, sellPrice, sellIndex = boundaryPrices[d]
            maxThusFar = max(maxThusFar, previousProfits[d - 1] - buyPrice)
            profitIfSellToday = maxThusFar + sellPrice

            if profitIfSellToday > currentProfits[d - 1]:
                currentProfits[d] = profitIfSellToday
                currentTransactions = [[buyPrice, buyIndex], [sellPrice, sellIndex]]
            else:
                currentProfits[d] = currentProfits[d - 1]

        # Store the best transaction for this transaction number
        transactions[t - 1] = currentTransactions

    maxProfit = evenProfits[-1] if k % 2 == 0 else oddProfits[-1]
    return maxProfit, transactions


# Assuming test_prices, max_transactions, and transactions are as defined in your test
def visualiseTrading1(test_prices, max_profit, transactions):
    plt.figure(figsize=(15, 8))
    plt.plot(test_prices, label='Stock Price', color='blue', linewidth=2)

    # Buy and sell markers
    buy_markers = []
    sell_markers = []

    for transaction in transactions:
        if transaction:
            buy_price, buy_index = transaction[0]
            sell_price, sell_index = transaction[1]
            buy_markers.append((buy_index, buy_price))
            sell_markers.append((sell_index, sell_price))

    # Plotting buy markers
    buy_x, buy_y = zip(*buy_markers)
    plt.scatter(buy_x, buy_y, color='green', marker='o', s=100, label='Buy', edgecolors='black')

    # Plotting sell markers
    sell_x, sell_y = zip(*sell_markers)
    plt.scatter(sell_x, sell_y, color='red', marker='X', s=100, label='Sell', edgecolors='black')

    # Adding annotations
    for i, (x, y) in enumerate(buy_markers):
        plt.annotate(f' Buy {i+1}\n(${y})', (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

    for i, (x, y) in enumerate(sell_markers):
        plt.annotate(f' Sell {i+1}\n(${y})', (x, y), textcoords="offset points", xytext=(0,-15), ha='center', fontsize=9)

    # Adjusting x-axis ticks to show day numbers
    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

    # Adding title and labels
    plt.title(f'Stock Prices and Transactions (Max Profit: ${max_profit})', fontsize=16)
    plt.xlabel('Day', fontsize=14)
    plt.ylabel('Price', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Show the plot
    plt.show()


import numpy as np

def generate_noisy_stock_data(length, start_price=100, volatility=0.5, drift=0.01):
    """
    Generates a list of stock prices that simulates a noisy market behavior.
    
    Args:
    length (int): The number of stock prices to generate.
    start_price (float): The starting stock price.
    volatility (float): The volatility of the stock market, higher means more fluctuation.
    drift (float): The overall direction and momentum of the stock market (positive for up, negative for down).
    
    Returns:
    list of float: A list representing the simulated stock prices.
    """
    prices = [start_price]
    for _ in range(1, length):
        # Calculate the price change
        change_percent = np.random.normal(drift, volatility)
        new_price = prices[-1] * (1 + change_percent)
        # Ensure the price doesn't drop below 0
        new_price = max(0, new_price)
        prices.append(new_price)
    
    return prices

# Example usage:
# Generate 100 days of stock prices with a starting price of 100, volatility of 2%, and a drift of 0.5%
stock_prices = generate_noisy_stock_data(100, 100, 0.02, 0.005)


# Test with the provided array
test_prices = [1, 2, 3, 4, 5, 10, 20, 25, 24, 23, 22, 21, 30, 40, 50, 1, 2, 3, 4, 5]

max_transactions = 1
max_profit, transactions = maxProfitWithKTransactions_final(stock_prices, max_transactions)

print(f'Transactions: {transactions}')

visualiseTrading1(stock_prices, max_profit, transactions)
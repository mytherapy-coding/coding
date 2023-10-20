import itertools
from itertools import accumulate


def maxProfit(prices: list[int]) -> int:
    profit = []
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if (prices[j] - prices[i]) > 0:
                profit.append(prices[j] - prices[i])
    max_profit = max(profit, default=0)
    return max_profit


def maxProfit1(prices: list[int]) -> int:
    profit = [prices[j] - prices[i] for i in range(len(prices)) for j in range(i + 1, len(prices)) if
              (prices[j] - prices[i]) > 0]
    max_profit = max(profit, default=0)
    return max_profit


def maxProfit2(prices: list[int]) -> int:
    profit = []
    for i in range(len(prices) - 1):
        max_sell = max(prices[i + 1:])
        profit.append(max_sell - prices[i])
    print(profit)
    return max(max(profit, default=0), 0)


def maxProfit3(prices: list[int]) -> int:
    profit = []
    for i in range(len(prices) - 1):
        max_sell = max(prices[i + 1:])
        profit.append(max_sell - prices[i])
    print(profit)
    return max(max(profit, default=0), 0)


def maxProfit4(prices: list[int]) -> int:
    max_sell = prices[-1]
    profit = []
    for i in list(range(len(prices) - 1, -1, -1)):  # [5, 4, 3, 2, 1, 0]
        profit.append(max_sell - prices[i])
        if prices[i] > max_sell:
            max_sell = prices[i]
    return max(profit)


def maxProfit5(prices: list[int]) -> int:
    max_sell = prices[-1]
    profit = []
    for i in list(range(len(prices) - 1, -1, -1)):  # [5, 4, 3, 2, 1, 0]
        profit.append(max_sell - prices[i])
        max_sell = max(prices[i], max_sell)
    return max(profit)


def maxProfit6(prices: list[int]) -> int:
    max_sell = itertools.accumulate(reversed(prices), max)
    return max(sell - buy for buy, sell in zip(reversed(prices), max_sell))


def maxProfit7(prices: list[int]) -> int:
    max_sell = [prices[-1]]
    for i in range(len(prices) - 1, -1, -1):
        max_sell.append(max(prices[i], max_sell[-1]))
    return max(max_sell[i] - prices[i] for i in range(len(prices) - 1, -1, -1))


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit6(prices))
print()
prices = [7, 6, 4, 3, 1]
print(maxProfit6(prices))
prices = []
print(maxProfit7(prices))

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    min_buy = prices[0]
    diff = []
    for price in prices[1:]:
        if price < min_buy:
            min_buy = price
        elif price > min_buy:
            diff.append(abs(min_buy - price))
        else:
            pass
    if not diff:
        return 0
    else:
        return max(diff)
            
            
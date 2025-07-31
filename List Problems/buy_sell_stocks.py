#return the max profit in from the day of buying and selling the shares.
#if there's no profit, return 0
#you cant buy and sell share on the same day
prices = [7, 1, 5, 3, 6, 4]
def share(prices): #TC is O(N2) and SC is O(1) , Not Optimal
    max_profit = 0
    for b in range(len(prices)):
        for s in range(b+1, len(prices)):
            if prices[s] > prices[b]:
                profit = prices[s] - prices[b]
                max_profit = max(max_profit, profit)
    
    return max_profit


def shareoptimal(prices): #Optimal , TC is O(N), SC is O(1)
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    
    return max_profit


print(share(prices))
print(shareoptimal(prices))



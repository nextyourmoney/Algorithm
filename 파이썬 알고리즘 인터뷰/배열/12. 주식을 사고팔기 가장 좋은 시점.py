#최대 이익 산출
import sys
from typing import List
def maxProfit (prices:List[int])->int:
    min_price = sys.maxsize
    profit = 0
    for price in prices:
        min_price = min(price,min_price)
        profit = max(price - min_price, profit)
    print(profit)
    return profit

maxProfit([7,1,5,3,6,4])
#!/urs/local/bin/python3


def buy_sell_twice(prices):
        if not prices:
            return 0

        max_profit1 = max_profit2 = curr_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            # print(i, prices[i])
            if prices[i] < prices[i-1]:
                if curr_profit > max_profit2:
                    max_profit1, max_profit2 = max_profit2, curr_profit
                elif curr_profit > max_profit1:
                    max_profit1 = curr_profit
                curr_profit = 0
                min_price = prices[i]
            curr_profit = max(curr_profit, prices[i] - min_price)
            print(min_price, curr_profit, max_profit1, max_profit2)

        if curr_profit > max_profit2:
            max_profit1, max_profit2 = max_profit2, curr_profit
        elif curr_profit > max_profit1:
            max_profit1 = curr_profit

        return max_profit1 + max_profit2


if __name__ == '__main__':
    print('Buy/Sell Stock Twice')
    print(buy_sell_twice([1,2,4,2,5,7,2,4,9,0]))

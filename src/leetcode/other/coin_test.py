def coin_change(coins, amount):
    di = dict()

    def count(n):
        if n == 0:
            return 0
        if n < 0:
            return -1
        if n in di:
            return di[n]
        res = float('INF')
        for coin in coins:
            subProblem = count(n - coin)
            if subProblem == -1:
                continue
            res = min(subProblem + 1, res)
            res = res if res != float('inf') else -1
            di[n] = res
        return res if res != float('inf') else -1

    return count(amount)


if __name__ == '__main__':
    coins = [1, 2, 3, 4, 5]
    amount = 995
    print(coin_change(coins, amount))

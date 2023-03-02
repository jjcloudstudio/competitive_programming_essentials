def get_min_coin(coins, val) -> int:
  if val < 0:
    return -1
  max_val = val + 1
  min_coins = [max_val] * (val+1)
  min_coins[0] = 0
  for coin in coins:
    for v in range(coin, val+1):
      min_coins[v] = min(1 + min_coins[v-coin], min_coins[v])

  return min_coins[-1]
    

print(get_min_coin([1, 2, 5], 18))

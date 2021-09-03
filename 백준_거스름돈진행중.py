def calc_coin(i, coin_list, remain):
    if i == len(coin_list):
        return 0
    return remain // coin_list[i] +  calc_coin(i+1, coin_list, remain % coin_list[i])

print(calc_coin(1000,[500, 100, 50, 10, 5, 1],620))

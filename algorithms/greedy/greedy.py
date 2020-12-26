# Money

def solution():
    money = 36410
    money_units = [10, 50, 100, 500, 1000, 5000]
    money_units = sorted(money_units, reverse=True)

    answer = []

    for unit in money_units:
        count = money // unit
        answer.append({unit: count})
        money -= unit * count

    print(answer)

solution()

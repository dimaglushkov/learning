# 546A A. Солдат и бананы

# Солдат хочет купить w бананов в магазине. Ему надо заплатить k долларов за первый банан, 2k долларов — за втор
# ой и так далее (иными словами, за i-й банан надо заплатить i·k долларов). У него есть n долларов. Сколько долл
# аров ему придется одолжить у однополчанина, чтобы купить w бананов?

k, n, w = [int(i) for i in input().split(' ')]
val = sum([i * k for i in range(1, w + 1)]) - n
print(val if val > 0 else 0)
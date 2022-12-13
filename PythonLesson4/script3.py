import random

setRandom1 = set()
setRandom2 = set()
i = 0
while i < 10:
    setRandom1.add(random.randint(0, 100))
    setRandom2.add(random.randint(0, 100))
    i += 1
print("Первый набор: ", setRandom1)
print("Второй набор: ", setRandom2)
print("Элементы входящие в оба набора: ", setRandom1 & setRandom2)
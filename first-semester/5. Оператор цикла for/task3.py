# Дано натуральное число n. Вычеслить
# img/1.5.3.png

n = int(input("Введите n "))
amount = 0

for i in range(0, n+1):
    amount+= ((-1)**i) * (1/(2**i))

print(amount)

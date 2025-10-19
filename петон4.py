# Afruzunova Dasha 502744
black = "\033[40m"
white = "\033[47m"
end = "\033[0m"
with open('sequence.txt') as f:
    n = []
    for l in f:
        n.append(float(l))

# 0-125
a = n[:125]
# 125-250
b = n[125:250]

# Ср по модулюю
x = 0
for num in a:
    x += abs(num)
x = x / 125
y = 0
for num in b:
    y += abs(num)
y = y / 125
# %
p = (x / (x + y)) * 100
# вывод ср
print(f"Среднее 0-125: {x:.2f}")
print(f"Среднее 125-250: {y:.2f}")

w = 50
w1 = int((p / 100) * w)
w2 = w - w1
print(black + " " * w1 + white + " " * w2 + end)

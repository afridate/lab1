import math

# Afruzunova Dasha 502744
black = "\033[40m"
white = "\033[47m"
end = "\033[0m"

s = 30
h = 15
# создаю поле, вычисляю знач функ, подрезаю поле, чиобы поле было на высоту ф-ии. т.е. масшоабтрую
for y in range(h, 0, -1):
    for x in range(s):
        func = math.sqrt(x)
        norm = func * (h / math.sqrt(s))

        if abs(norm - y) < 0.5:
            print(black + " " + end, end="")
        else:
            print(white + " " + end, end="")
    print()

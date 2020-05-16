l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

y = 1
b = ""
while y <= a:
    x = 1
    while x <= l:
        if y == 1 or y == a:
            b = b + "#"
        else:
            if x == 1 or x == l:
                b = b + "#"
            else:
                b = b + " "
        x = x + 1
    print(b)
    b = ""
    y = y + 1
l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

y = 1
b = ""
while y <= a:
    x = 1
    while x <= l:
        b = b + "#"
        x = x + 1
    print(b)
    b = ""
    y = y + 1
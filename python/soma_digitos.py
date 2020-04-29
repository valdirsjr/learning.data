n = int(input("Digite um numero inteiro:"))
s = 0
while (n >= 1):
    s = s + (n % 10)
    n = n // 10
print(s)
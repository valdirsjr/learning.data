def éPrimo(n):
    """
    Teste para numero primo

    """
    i = n - 1
    while i > 1:
        if (n % i) == 0:
            return False
        i = i - 1
    return True

def maior_primo(n):
    maior = n
    while maior > 1:
        if éPrimo(maior):
            return maior
        maior = maior - 1



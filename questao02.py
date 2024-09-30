#questão 02

def verifica_letra_a(string):

    quantasA = string.lower().count('a')

    if quantasA > 0:
        return f"A letra 'a' aparece {quantasA} vezes na string."
    else:
        return f"A letra 'a' não aparece na string."
    
#usando o metodo para ver quantas letras 'a' tem na string


letra_informada = (input("Informe a string: "))
resultado = verifica_letra_a(letra_informada)
print(resultado)
    
"""
5. Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A
passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar
os valores trocados.
"""


def main():
    vlra = int(input("informe valor a "))
    vlrb = int(input("informe valor b "))
    print(" Antes da troca  ")

    print("valor a ", vlra)
    print("valor b ", vlrb)

    aux = vlra
    vlra = vlrb
    vlrb = aux
    print(" Depois da troca  ")
    print("valor a ", vlra)
    print("valor b ", vlrb)

main()

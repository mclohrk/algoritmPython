# ! /usr/bin/env pyton3

"""
2) Faça um algoritmo que leia dois valores inteiros e escreva a sua soma



def main():

    valor_a = int(input("Digite um valor para soma"))
    valor_b = int(input("Digite outro valor para soma"))


    soma = valor_a + valor_b
    print("Valor total da soma ", soma)
main()
"""


def main():
    # a_str e b_str guardam strings
    a_str = input("Digite o primeiro numero: ")
    b_str = input("Digite o segundo numero: ")

    # a_int e b_int guardam inteiros
    a_int = int(a_str)  # converte string/texto para inteiro
    b_int = int(b_str)  # converte string/texto para inteiro

    # calcule a soma entre valores que são números inteiros
    soma = a_int + b_int

    # imprima a soma
    print("A soma de", a_int, "+", b_int, "eh igual a", soma)

    main()

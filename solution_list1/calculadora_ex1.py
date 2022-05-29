"""1. Faça um algoritmo que simule uma calculadora aritmética simples. Deve ler dois números reais,
solicitar que informe qual operação aritmética deseja realizar (soma, subtração, multiplicação ou
divisão) e ao final mostrar o resultado da operação selecionada. Depois que exibir o resultado, deve
perguntar se quer realizar outra operação. Se a resposta for positiva solicita dois números e repete o
processo descrito, caso contrário encerra o algoritmo.
"""

def main():
    def operacao():
        vlr1 =  float(input("informe valor 1 "))
        vlr2 =  float(input("informe valor 2 "))


    print("Calculadora simples")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao ")
    print("4 - Divisao ")
    opcao = int(input("Informe o tipo de operacao >> "))

    if opcao == 1:
        vlr1 =  float(input("informe valor 1 "))
        vlr2 =  float(input("informe valor 2 "))
        result = vlr1 + vlr2
        print(" Resultado da Soma é ", result)
    elif opcao == 2:
        vlr1 = float(input("informe valor 1 "))
        vlr2 = float(input("informe valor 2 "))
        result = vlr1 - vlr2
        print(" Resultado da Subtracao é ", result)
    elif opcao == 3:
        vlr1 = float(input("informe valor 1 "))
        vlr2 = float(input("informe valor 2 "))
        result = vlr1 * vlr2
        print(" Resultado da Multiplicacao é ", result)
    elif opcao == 4:
        vlr1 = float(input("informe valor 1 "))
        vlr2 = float(input("informe valor 2 "))
        result = vlr1 / vlr2
        print(" Resultado da Divisao é ", result)

	main()

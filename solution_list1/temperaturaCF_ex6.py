'''
6. Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula
de conversão é: F=9*C / 5 + 32, sendo F a temperatura em Fahrenheit e C a temperatura em
Celsius.
'''

def main():

    print("Programa conversao de Graus ")
    c = float(input("Informe graus em Celsius "))
    f = 9 * c / 5 + 32
    print("Graus em F convertido ", f)
main()
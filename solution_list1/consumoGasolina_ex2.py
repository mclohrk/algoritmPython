"""
2. Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a
distância total percorrida pelo automóvel e o total de combustível gasto
"""


def main():
    print("*** Programa calculo de consumo de combustivel ***\n")
    ds = float(input("informe a distância percorrida em KM >> "))
    dt = float(input("informe o tempo gasto em horas >> "))
    dt += (dt / 60) # conversao de hora para minutos
    consumo =  dt / ds
    print(" Consumo Medio ",consumo)
main()
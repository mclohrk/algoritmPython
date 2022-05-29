"""
3. Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre
suas vendas efetuadas, informar o seu nome, o salário fixo e salário total no final do mês.
"""


def main():
    nome = input("informe o nome do vendedor >> ")
    salarioFix = float(input("informe o salario do vendedor >>"))
    vendasTotal = float(input("informe o total de vendas em dinheiro ex: r$ 100,00 >> "))

    # CALCULO
    salarioVar = salarioFix + ((vendasTotal / 100) * 15)
    print(" Vendedor ", nome, " tem Salario fixo ", salarioFix, "salario Total ", salarioVar)
main()
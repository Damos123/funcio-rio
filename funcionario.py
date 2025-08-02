#função de calculo do salário
def calcular_salario(n_horas, valor_hora):
    n_horas = float(n_horas)
    valor_hora = float(valor_hora)
    # assume-se que 120 horas do mês corresponde a 4 semanas 
    if n_horas > 160:
        salario = 160 * valor_hora + (n_horas - 160) * valor_hora * 1.8
    else:
        salario = valor_hora * n_horas
    return salario

# Exemplo de uso:
n_horas = input("Digite o número de horas trabalhadas: ")
valor_hora = input("Digite o valor da hora: ")
print(f" O seu Salário do mês é: {calcular_salario(n_horas, valor_hora):.2f} €")
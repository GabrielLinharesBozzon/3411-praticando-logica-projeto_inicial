def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return 'Não foi possível realizar a divisão por 0'
    return a / b

def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao == 'soma':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida'
    return resultado

saida = ''

while saida.lower() != 'n':
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operacao = input('Digite a operação (+, -, *, /): ')
    resultado = calculadora(num1, num2, operacao)
    print('Resultado da operação:', resultado)
    saida = input('Deseja continuar? (S/N): ') 
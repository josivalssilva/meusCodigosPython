#Criado por Josivalssilva


def calculaIr(salarioAtual):
    impostoDeRenda = 0
    if (salarioAtual <= 1903.98):
        impostoDeRenda = 0
    elif ((salarioAtual >= 1903.99) and (salarioAtual <= 2826.65)):
        impostoDeRenda  = salarioAtual * 0.075
    elif ((salarioAtual >= 2826.66) and (salarioAtual <= 3751.05)):
        impostoDeRenda  = salarioAtual *  0.15
    elif ((salarioAtual >= 3751.06) and (salarioAtual <= 4664.68)):
        impostoDeRenda  = salarioAtual * 0.225
    else:
        impostoDeRenda = salarioAtual * 0.275

    return impostoDeRenda

def calculaInssAtual(salarioAtual):
    impostoInss = 0
    if (salarioAtual <= 1100.00):
        impostoInss = salarioAtual * 0.075
    elif ((salarioAtual >= 1100.01) and (salarioAtual <= 2203.48)):
        impostoInss  = salarioAtual * 0.09
    elif ((salarioAtual >= 2203.49) and (salarioAtual <= 3305.22)):
        impostoInss  = salarioAtual *  0.12
    elif ((salarioAtual >= 3305.23) and (salarioAtual <= 6433.57)):
        impostoInss  = salarioAtual * 0.14
    else:
        impostoInss = salarioAtual * 0.275
    if (impostoInss >= 751.97):
        impostoInss = 751.97

    return impostoInss

if __name__ == '__main__':
    salarioAtual = float(input("Digite o valor do salário da vaga atual: "))
    irAtual = calculaIr(salarioAtual)
    print('Você paga IR no emprego atual: ', irAtual )
    inssAtual = calculaInssAtual(salarioAtual)
    print('Você paga INSS no emprego atual: ', inssAtual)
    salarioLiquidoAtual = (salarioAtual - (irAtual + inssAtual))
    print('Salário Líquido: ', salarioLiquidoAtual)

    salarioProposto = float(input("Digite o valor do salário proposto da novo emprego: "))
    irNovo = calculaIr(salarioProposto)
    print('Você paga IR no emprego atual: ', irNovo)
    inssNovo = calculaInssAtual(salarioProposto)
    print('Você paga INSS no emprego atual: ', inssNovo)
    salarioLiquidoNovo = (salarioProposto - (irNovo + inssNovo))
    print('Salário Líquido: ', salarioLiquidoNovo, '\n')

    print('A diferença entre os dois salários é de : ', salarioLiquidoNovo - salarioLiquidoAtual, '\n')

    print('Importante lembrar que os benefícios em ambos empregos não estão sendo calculados aqui!\nAssim como, seu conhecimento acerca do ambiente do novo trabalho. Muito cuidado então!')



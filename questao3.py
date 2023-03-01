def dimensoesObj():
    while True:# funcao que captura e multiplica as dimensoes de um obj
     try:
        cm = int(input('Digite o comprimento do objeto em centimetros! '))
        larg = int(input('Digite a largura do objeto em centimetros! '))
        alt = int(input('Digite a altura do objeto em centimetros! '))
     except ValueError:
         print('digite um valor em centimetros')
         continue
     total = cm * larg * alt
     if(total >= 100000):
        print('Não aceitamos objetos com dimensões tão grandes\nEntre com as dimensoes do Objeto novamente! ')
        continue
     elif(total < 1000):
         return 10
     elif(total >= 1000) and (total < 10000):
         return 20
     elif(total >= 10000) and (total < 30000):
         return 30
     elif(total >= 30000) and (total < 100000):
         return  50

def pesoObj():# funcao que captura o peso do objeto e gera um multiplicador
    while True:# loop que é que é quebrado quando quando usuario digita o peso do obj
        try:
            pesoO = float(input('Digite o peso do objeto'))
            if(pesoO <= 0.1):
                return 1
            elif 0.1 <= pesoO < 1:
                return 1.5
            elif 1 <= pesoO < 10:
                return 2
            elif 10 <= pesoO < 30:
                return 3
            elif(pesoO >= 30):
                print('Peso não aceito! ')
                continue
        except ValueError:
            print('Digite valores validos')
def rotaObj(): # funcao que captura qual a rota do usuario e gera um multiplicador
    while True: #loop que é quebrado quando usuario escole uma rota
        rotas = input('Selecione a Rota:\n'
                      'BR - De Brasilia para Rio de Janeiro\n'
                      'BS - De Brasilia para São Paulo\n'
                      'RB - De Rio de Janeiro para Brasilia\n'
                      'RS - De Rio de Janeiro para São Paulo\n'
                      'SR - De São Paulo para Rio de Janeiro\n'
                      'SB - De São Paulo para Brasilia\n'
                      '>>')
        if(rotas == 'BR'):
            return 1.5
        elif(rotas == 'BS'):
            return 1.2
        elif(rotas == 'RB'):
            return 1.5
        elif(rotas == 'RS'):
            return 1
        elif(rotas == 'SR'):
            return 1
        elif(rotas == 'SB'):
            return 1.2
        else:
            print('Por favor digite uma rota valida! ')
            continue




print('Bem vindo a Companhia de Logistica do Carlos Eduardo Silva De Oliveira')
dimensoes = dimensoesObj()
peso = pesoObj()
rota = rotaObj()
total = dimensoes * peso * rota
print(f'Total a pagar(R$): {total} (dimensões: {dimensoes} * peso: {peso} * rota: {rota})')

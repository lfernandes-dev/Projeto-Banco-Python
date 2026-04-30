historico = [{'Método':'Nehum', 'Valor':0.0}]
saldo = 0.0
escolha = 0
def depositar(valor):
    global saldo
    if valor < 0:
        return None
    else:
        saldo += valor
        historico.append({'Método':'Depósito', 'Valor':valor})
        return saldo
def sacar(valor):
    global saldo
    if valor < 0:
        return None
    elif valor > saldo:
        return None
    else:
        saldo -= valor
        historico.append({'Método':'Saque', 'Valor':valor})
        return saldo
def ver_saldo():
    global saldo
    return saldo
def ver_historico():
    if not historico:
        print('Histórico vázio!')
    else:
        for historicos in historico:
                print(f'Método: {historicos["Método"]} | Valor: {historicos["Valor"]}')

while escolha != 5:
    escolha = int(input('1 - Depositar\n2 - Sacar\n3 - Ver saldo\n4 - Ver hitórico\n5 - Sair\nDigite um dos números acima: '))
    try:
        if escolha == 1:
            valor_deposito = float(input('Digite o valor que deseja depositar: '))
            novo_saldo = depositar(valor_deposito)
            if novo_saldo is not None:
                print(f'Depósito efetuado com sucesso seu saldo agora é de R${saldo}')
            else:
                print('ERROR: VALOR INVÁLIDO!')
        elif escolha == 2:
            valor_sacar = float(input('Digite o valor que deseja sacar: '))
            saldo_saque = sacar(valor_sacar)
            if saldo_saque is not None:
                print(f'Saque realizado com sucesso seu novo saldo é de R${saldo}')
            else:
                print('ERROR: VALOR INVÁLIDO!')
        elif escolha == 3:
            saldo_ver = ver_saldo()
            print(f'Seu saldo é: R${saldo_ver}')
        elif escolha == 4:
            ver_historico()
        elif escolha == 5:
            break
    except ValueError:
        print('ERROR: DIGITE UM DOS NÚMEROS ABAIXO!')

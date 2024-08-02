from datetime import datetime



# Enviar dinhero 
def enviar(saldo, valor):
    if valor <= saldo: 
        return -valor
    
    print('Sem Saldo')
    return 0

# deposito 
def deposito(valor):
    if not '-' in str(valor): 
        return valor
    
    print('Valor inválido')
    return 0 

# Edita ou input do usuario
def input_edite(texto):
    try:
      int = float(input(f'{texto}'))
      return int
    except ValueError as err:
        print(f'Erro: {err}')

#Salva hstorico do usuario
def historico_date(saldo, Extrado):
    
    with open('historio.txt', 'a')  as historico:
        historico.write(f"Saldo R$ {saldo}\n")
        for Extra in Extrado:
            historico.write(f"Extrado R$ {Extra}---{datetime.now()}\n")

# ler historico do usuaro
def Ler_historico():
    saldo = 0
    extrado = []
    try:
        with open('historio.txt', 'r') as historico:
            for his in  historico.readlines():
                if 'Saldo' in his:
                    # pegar ultimo valor  
                    if saldo > 0:
                        saldo = 0   
                    saldo += float(his[8:])
                else:
                  extrado.append(his[:-8])
    except FileNotFoundError as err:
        pass
    
    return saldo, extrado








saldo, Extrado = Ler_historico()
runn = True 
while runn:
    
    #Pegar ultimo saldo, extrado
    
    print('Banco do inu')
    print(f'Saldo {saldo}')
    print(f'1 - Extrado ---:')
    print(f'2 - Deposito --:')
    print(f'3 - Enviar ----:')
    print(f'4 - Sair ------:')
    
    
    
    opera = input_edite("Operação:")
    if opera == 4:
        print('Obrigado por usa o banco inu ')
        runn = False
    
    
    if opera == 1:
        print('Extrado: ')
        for Extra in Extrado:
            if Extra != 0:
               print(f" __valor R${Extra}__")
            
    
    if opera == 2 or opera == 3:
        valor = input_edite("R$:")
        
        if opera == 2:
            saldo_dp = deposito(valor)
            if saldo_dp:
               Extrado.append(saldo_dp)
               saldo += saldo_dp 
               
        elif opera == 3:
            saldo_en = enviar(saldo, valor)
            if saldo_en:
               Extrado.append(saldo_en) 
               saldo += saldo_en 
            
        else: 
            print('Operação Inválido')
    
    historico_date(saldo,Extrado)

    


 

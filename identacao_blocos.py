def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o seu dinheiro na boca do caixa.")
    
    print("Obrigado por ser nosso cliente. Tenha um bom dia!")
sacar(100)

def depositar(valor):
    saldo = 500
    saldo += valor
    print(saldo)
depositar(200)


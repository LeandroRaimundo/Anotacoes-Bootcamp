# Atribuí o valor 10 à variável "número"
numero = 10

# O comando print irá mostrar o valor atual da variável
print(f"O valor da variável é {numero}")

# Aqui, atribuí um novo valor à variável "numero"
numero = 50

# O comando print irá mostrar o valor atualizado da variável
print(f"O valor atualizado da variável é {numero}")

# O valor da variável será atualizado conforme a ordem de execução do código

# Exemplo: Um caixa eletrônico inicia com o valor de R$1000,00 na conta bancária do cliente
# O cliente decide sacar R$50,00
# O valor inicial da conta do cliente não será mais de R$1000,00, será de R$950,00, pois ele tirou R$50,00

# Exemplo do caixa eletrônico
saldo = float(input("Digite o valor total da conta bancária:\nR$"))
print(f"O saldo da conta é de R${saldo:.2f}")

saque = float(input("Digite o valor do saque:\nR$"))

if saque > saldo:
    print("Desculpe, o valor de saque excede o saldo!")

else:
    saldo = saldo - saque
    print(f"Saque de R${saque:.2f} efetuado com sucesso!\nO seu saldo agora é de {saldo:.2f}")
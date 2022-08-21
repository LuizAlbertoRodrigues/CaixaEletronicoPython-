#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Programa do Caixa Eletrônico
# Created by Luiz Alberto

# import sys
import os

correta = 123
i = 0
saldo = 0

while(i<=2):
    senha = int(input("Digite a senha: "))
    if(senha==correta):
        print("Acesso ao sistema OK ")
        break
    else:
        print("Senha incorreta...")
        i = i + 1
        if(i==3):
            print("")
            print("################################")
            print("Acesso negado! Cartão bloqueado!")
            print("################################")
            pause = input("Encerrando sistema...")
            os._exit(1)

while(True):

    print("+++ BANCO LUIZZ SA +++")
    print("++++++++++++++++++++++")
    print("1. Depósito ...")
    print("2. Saque ...")
    print("3. Saldo ...")
    print("4. Encerrar ...")

    op = int(input("Escolha a operação: "))
    
    if(op==1):
        valor = float(input("Qual o valor a depositar? "))
        saldo = saldo + valor
        print("Saldo atual = %.2f" % saldo)
        print("\n\n")
    elif(op==2):
        valor = float(input("Qual o valor a sacar? "))
        saldo = saldo - valor
        print("Saldo atual = %.2f" % saldo)
        print("\n\n")
    elif(op==3):
        print("Saldo atual = %.2f" % saldo)
        print("\n\n")
    else:
        print("")
        print("######################################")
        print("Obrigado por utilizar nossos serviços!")
        print("######################################")
        pause = input("Encerrando sistema...")
        os._exit(1)


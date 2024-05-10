from recursos.funcoes import limparTela, aguarde

def jogodaforca():
    limparTela()

    print('''Bem vindo ao jogo da forca.
        Vamos começar!!''')

    aguarde(2)
    limparTela()

    j1 = input('Nome do Jogador 1: ')
    j2 = input('Nome do jogador 2: ')

    limparTela()

    while True:
        palavra = input(f'{j1} digite uma palavra para o {j2} adivinhar: ')
        dicasLista = []
        dica1 = input('Digite a dica 1: ')
        dicasLista.append(dica1)
        dica2 = input('Digite a dica 2: ')
        dicasLista.append(dica2)
        dica3 = input('Digite a dica 3: ')
        dicasLista.append(dica3)
        retry = input('digite [1] para reescrever ou pressione [ENTER] para continuar: ')
        if retry == '':
            limparTela()
            break

    limparTela()

    palavraSecreta = '_' * len(palavra)  
    erros = 6
    dicas = 3
    letrasTentadas = []  
    while erros > 0:
        continuar = input('''
                            Enter para continuar ''')
        limparTela()
        print('A palavra é: ')
        print(f'{palavraSecreta}')
        print(f'''
    Voce tem {erros} vidas''')
        print(f'''
    Letras já tentadas: {" ".join(letrasTentadas)}''' 
                if letrasTentadas else '') 

        letraJogada = input('''
                            
                            Digite uma letra ou [1] para pedir dica : ''')
        if letraJogada == '1':
            if dicas > 0:
                print (f'''
                            A dica é: {dicasLista[0]}''')
                dicasLista.pop(0)
                dicas -= 1
            else:
                print('''
                            Acabou suas dicas! ''')
        else:
            if letraJogada in palavra:
                for i in range(len(palavra)):
                    if palavra[i] == letraJogada:
                        palavraSecreta = palavraSecreta[:i] + letraJogada + palavraSecreta[i+1:]
            else:
                erros -= 1
                letrasTentadas.append(letraJogada)  

            if '_' not in palavraSecreta:
                limparTela()
                print(f"Parabéns! Você venceu!")
                print(f"A palavra era: \n\n{' '.join(palavra.upper())}\n\n")
                break
            elif erros == 0:
                limparTela()
                print(f"Você perdeu! A palavra era:\n\n{' '.join(palavra.upper())}\n\n")
                break
    opcao = input("Deseja jogar novamente? (S/N): ").upper()
    if opcao == "S":
        jogodaforca()

jogodaforca()





    


        


import os


palavrasecreta = input('digite a palavra secreta : ').upper()
pontos = 6
palavrasecretaemtracos = ['_'] * len(palavrasecreta)
letrasdigitadas = []

print('\n' * 100)



while True:

    print(' '.join(palavrasecretaemtracos))   # join junta a lista e transforma em uma string

    print(f'\033[31m\nDigite 1 para sair\n\033[0;0m')

    letradigt = input('digite uma letra: ').upper()

    if letradigt in letrasdigitadas:                             # se a letra ja ter sido digitada previamente
        print(f'\033[31m'+f'{letradigt} JA FOI DIGITADA!'+'\033[0;0m')

    if letradigt not in letrasdigitadas:
        letrasdigitadas.append(letradigt)               # adiciona as letras digitadas nesta lista

    print(f'LETRAS DIGITADAS : {letrasdigitadas},')

    i = 0                         ##    para inicializar a contagem do indice da pset
    if letradigt in palavrasecreta:      ##      verificando se a letra digitada esta na palavra secreta
        for l in palavrasecreta:        ## percorrendo a palavrasecreta para achar o indice da letra
            if letradigt == l:
                palavrasecretaemtracos[i] = letradigt ## modificando a pset no indice correto
            i += 1      ##continuando a contagem da posicao
        print('Acertou!')
    else:
        pontos -= 1
        print('\033[31m Errou! \033[0;0m')

    print(f'\nVoce tem {pontos} vidas\n')

    if pontos < 1:
        print('\033[31m Perdeu! \033[0;0m')
        break

    if ''.join(palavrasecretaemtracos) == palavrasecreta:
        print('\033[32m'+f'Voce ganhou! A palavra foi {palavrasecreta.upper()}'+'\033[0;0m')
        break


    if letradigt == '1':   ## se o usuario quizer sair ele digita 1
        break


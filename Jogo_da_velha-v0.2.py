from tkinter import * #biblioteca grafica do python
import tkinter.messagebox as tkmb   #biblioteca que vai ser usada para mostrar uma caixa de pergunta na tela (perguntando se deseja reiniciar o jogo)
import os   #biblioteca que vai ser usada para limpar o terminal


aux = 'O'
padrao_O = [] #variavel que ira guardar a localizacao de cada botao com O
padrao_X = [] #variavel que ira guardar a localizacao de cada botao com X
b = [0, 1, 2, 3, 4, 5, 6, 7, 8]  #botoes em forma de lista para poderem serem modificados facilmente com um for
padroes_vencedores = [    #padroes vencedores
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8], 
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]

def limpa_os_botoes(): #funcao que ira reiniciar o jogo limpando todos os campos e resetando a contagem da pontuacao
    global padrao_O
    global padrao_X
    padrao_O = []#zerando os padroes das referencias O
    padrao_X = []#zerando os padroes das referencias X
    print(f'padrao O {padrao_O}')
    print(f'padrao x {padrao_X}')
    for i in range(9): #passando por todos os campos e limpando o campo texto
        b[i].text = '' #deixando vazio o texto do botao 
        b[i].criarbotao() #chamando a funcao de criar o botao para reinicia-lo com o novo valor vazio
        
class Principal():                                          
    def __init__(self, referencia, text, coluna, linha):                  
        self.referencia = referencia #refencia da posicao do botao           | 1 2 3 |
        self.text = text             #texto do botao(X ou O)                 | 4 5 6 |
        self.coluna = int(coluna)    #posicao(coluna) do botao na janela     | 7 8 9 |
        self.linha = int(linha)      #posicao(linha) do botao na janela
    
    def criarbotao(cls):  #cria o botao passando configuracoes independentes
        cls.Principal = Button(window, text=cls.text, height=8, width=8, command=cls.comando_botoes)
        cls.Principal.grid(column=cls.coluna, row=cls.linha)

    def comando_botoes(self):    #comandos que seram executados a cada vez que o botao for selecionado
        global aux   #varivel para trocar o valor de X para O e viceversa
        global padrao_O  
        global padrao_X
        global padroes_vencedores
        global b  #lista que contem todas as posicoes dos botoes 
        
        os.system('clear') #limpando o terminal para ler melhor as informacoes
        
        if self.Principal['text'] == '': #se o botao selecionado nao conter X nem O
            if aux == 'O':  #aux sempre vai iniciar com O e logo apos muda para X para o proximo botao
                self.Principal['text'] = 'O' # marcando o botao como O
                padrao_O.append(self.referencia) #adicionando a posicao do botao selecionado na lista padrao_O
                aux = 'X' # mudando o texto de O para X para o proximo botao
            elif aux == 'X': 
                self.Principal['text'] = 'X' # marcando o botao como X
                padrao_X.append(self.referencia) #adicionando a posicao do botao selecionado na lista padrao_X
                aux = 'O' # mudando o texto de X para O para o proximo botao  
                
            print(f'padrao O {padrao_O}') 
            print(f'padrao x {padrao_X}')
            
            for i in padroes_vencedores: #passando pelos padroes vencedores para pegar cada lista independetemente 
                pontos_X = 0 #pontuacao para verifcar se o padrao_x esta na lista i dos padroes vencedores
                pontos_O = 0 #pontuacao para verifcar se o padrao_O esta na lista i dos padroes vencedores
                
                for j in i: #pegando cada lista e verificando cada valor independetemente para saber se esta contido em cada padrao(padra_O ou padra_X)
                    if j in padrao_O: #se o valor da lista estiver contido no padrao_O
                        pontos_O += 1 #adicionando pontos
                        if pontos_O >= 3: #se o padrao_O conter todos os tres valores de qualquer lista dos padroes_vencedores
                            r = tkmb.askyesno(title='FIM DE JOGO', message='O venceu!  \n deseja jogar novamente?', icon='info')
                            if r:
                                limpa_os_botoes()
                            else:
                                window.quit()
                    if j in padrao_X:
                        pontos_X += 1
                        if pontos_X >= 3: #se o padrao_X conter todos os tres valores de qualquer lista dos padroes_vencedores
                            r = tkmb.askyesno(title='FIM DE JOGO', message='X venceu!  \n deseja jogar novamente?', icon='info')
                            if r:
                                limpa_os_botoes()
                            else:
                                window.quit()  
            
        
window = Tk()   #criando janela no tkinter
window.title('JOGO DA VELHA') #definindo o nome da janela
window.geometry('325x550')  #definindo as dimensoes da janela


b[0] = Principal(1, '', 0, 0)   #criando um objeto botao com as configuracoes (referencia, text, coluna, linha)
b[0].criarbotao()               #chamando  a funcao responsavel por criar o botao na janela

b[1] = Principal(2, '', 1, 0)   #criando um objeto botao com as configuracoes (referencia, text, coluna, linha)
b[1].criarbotao()               #chamando  a funcao responsavel por criar o botao na janela

b[2] = Principal(3, '', 2, 0)   
b[2].criarbotao()

b[3] = Principal(4, '', 0, 1)
b[3].criarbotao()

b[4] = Principal(5, '', 1, 1)
b[4].criarbotao()

b[5] = Principal(6, '', 2, 1)
b[5].criarbotao()

b[6] = Principal(7, '', 0, 2)
b[6].criarbotao()

b[7] = Principal(8, '', 1, 2)
b[7].criarbotao()

b[8] = Principal(9, '', 2, 2)
b[8].criarbotao()

resetando_jogo = Button(window, text='RESETAR JOGO', height=5, width=20, command=limpa_os_botoes) 
resetando_jogo.place(x=50, y=450)

window.mainloop()

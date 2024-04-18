# Exercício - Sistema de perguntas e respostas!

#Abaixo criaremos uma lista com 3 dicionarios, incluindo perguntas e respostas!

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },    
]


qtd_acertos = 0 # Variavel que irá armazenar a quantidade de acertos!

for pergunta in perguntas: #O "for" vai varrer a lista perguntas, exibindo cada pergunta na tela!
    print('Pergunta:', pergunta ['Pergunta'])
    print() #Esse print usa pra "quebrar linha"
    
    opcoes = pergunta['Opções'] # passando as Opções para variavel sem acento somente > opcoes
    for i, opcao in enumerate(opcoes): #Aqui vai enumerar cada opção, 1, 2 e 3
        print(f'{i}:', opcao) #o print vai mostrar o numero e a opção
    print()
    escolha = input('Escolha uma opção:') #Aqui estou atribuindo o input(pergunta ao usuário) a váriavel "escolha"
    
    acertou = False #Atribuindo false a variavel acertou
    escolha_int = None #Atribundo none a variavel escolha_int
    qtd_opcoes = len(opcoes) #Aqui o len vai ler quantas opções tem e guarda dentro da variavel > qtd_opcoes
    
    if escolha.isdigit(): #Se esscolha for digito inteiro
        escolha_int = int(escolha) #escolha_int vai receber o valor de escolha
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True 
                
    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')
    
    print()
    
print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas')   
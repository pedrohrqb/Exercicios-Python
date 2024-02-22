#Criar um função que multiplique, triplique e quadriplique o numero passado no parametro.


def criar_multiplicador(multiplicador): # Essa função pega o primeiro parametro passado numero
    def multiplicar(numero): # Essa função pega o numero e multiplica pelo (multiplicador)
        return numero * multiplicador # Aqui retornar o valor
    return multiplicar # Retornar o calculo para primeira função


duplicar = criar_multiplicador(2) # Crio uma variavel que recebe a primeira função com o paramentro 2(assim multiplica por 2) e assim emm diante...
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(triplicar(5)) # No print basta eu por o numero que eu quero e a variavel que faz a função.
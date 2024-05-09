from copy import deepcopy

def jogar(estado, movimento):
    estado = deepcopy(estado)

    for i in range(len(estado)):
            for j in range(len(estado[i])):
                if estado[i][j] == 0:           
                    if(movimento == 'Cima' and i != 0):
                        temp = estado[i - 1][j]  
                        estado[i - 1][j] = 0
                        estado[i][j] = temp
                        return estado
                    if(movimento == 'Baixo'  and i != (len(estado) - 1)):
                        temp = estado[i+1][j]  
                        estado[i+1][j] = 0
                        estado[i][j] = temp
                        return estado
                    if(movimento == 'Esquerda'  and j != 0):
                        temp = estado[i][j - 1]  
                        estado[i][j - 1] = 0
                        estado[i][j] = temp
                        return estado
                    if(movimento == 'Direita'  and j != (len(estado[i]) - 1)):
                        temp = estado[i][j + 1]  
                        estado[i][j + 1] = 0
                        estado[i][j] = temp
                        return estado
                    else:
                        return estado
    

def avaliar_pontuacao(estado, estado_final):
  count = 0
  estado_atual = deepcopy(estado)
  for i in range(len(estado_atual)):
          for j in range(len(estado_atual[i])):
            count += 1 if estado_atual[i][j] == estado_final[i][j] else 0
  return (estado_atual, count)


def busca_star(inicial, final):
    len_inicial =  avaliar_pontuacao(inicial, final)[1]
    estados = [(inicial, len_inicial)] # [(cidade, distancia)]
    jogadas = set() # Conjunto de dados únicos = cidades visitadas
    movimentos = {}

    while estados: 
        atual = max(estados, key=lambda x: x[1])        
        print(f"Atual: {atual[0]} - Pontuacao: {atual[1]}")
        
        estados = list(filter(lambda x: x != atual, estados)) # Remove a 
        
        if atual[0] == final:
            print("Destino alcançado!")
            return 
        
        jogadas.add((str(atual[0]), atual[1]))

        #print(jogar(atual[0], "Baixo"))
        for m in ["Baixo","Cima","Esquerda","Direita"]:
            jogada = jogar(atual[0], m)
            estado_pontuacao = avaliar_pontuacao(jogada, final)
            if ((str(estado_pontuacao[0]), estado_pontuacao[1])) not in jogadas:
                estados.append((estado_pontuacao))

# Estado inicial do quebra-cabeça
estado_inicial = [[1,0,3],
                  [4,2,5],
                  [7,8,6]]

# Estado final do quebra-cabeça
estado_final = [[1,2,3],
                [4,5,6],
                [7,8,0]]

busca_star(estado_inicial, estado_final)

conexoes = {
    'A': [('C', 2), ('D', 3)],
    'C': [('D', 1), ('E', 4), ('F', 6)],
    'D': [('E', 1), ('G', 5)],
    'E': [('B', 5), ('F', 2)],
    'F': [('B', 3)],
    'G': [('E', 2), ('B', 9)],
    'H': [('A', 4), ('D', 3)],
    'I': [('H', 3), ('J', 6)],
    'J': [('A', 5)]
    # você pode adicionar mais valores aqui 
}

# Heurística (distancia de x até B)
heuristica = {
    'A': 7, 'C': 5, 'D': 7, 'E': 3, 'F': 2,
    'G': 6, 'H': 8, 'I': 9, 'J': 10, 'B':0
}


def busca_star(origem, destino):
    fronteira = [(origem, 0)] # [(cidade, distancia)]
    visitados = set() # Conjunto de dados únicos = cidades visitadas
    
    custo_do_caminho = {origem: 0} # para cada cidade
    caminho = [] # Guardar o caminho escolhido

    while fronteira: 
        print(f'Fronteiras listadas antes da troca: {fronteira}')

        atual, valor = min(fronteira, key=lambda x: x[1])        
        print(f"Decisão: {atual}:{valor}")
        
        fronteira = list(filter(lambda x: x[0] != atual, fronteira)) # Remove a 
        
        if atual == destino:
            print("Destino alcançado!")
            return 
        visitados.add((atual, valor))
            
        for vizinho, distancia in conexoes.get(atual, []):
            custo = custo_do_caminho[atual] + distancia 
            f = custo + heuristica[vizinho]

            if ((vizinho,f)) not in visitados:
                caminho.append((f"{atual}:{vizinho}", f))
                custo_do_caminho[vizinho] = custo
                fronteira.append((vizinho, f))
busca_star('A', 'B')
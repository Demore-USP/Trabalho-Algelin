""" 
DUPLA:
Leonardo Doro Demore - 15674786
Arthur Filliettaz - 12532055
Turma 2
"""

import numpy as np
import networkx as nx

#========================================================================================================================
"""
Lógica: Neste bloco recebemos as entradas, criamos a matriz adjacência e calculamos-na aplicando a transformação
"""
# Recebendo a quantidade de vértices e arestas
n_vertices, m_arestas = map(int, input().split())

# Criando a matriz (preenchida com zeros)
matriz_adj = np.zeros((n_vertices, n_vertices))

# Recebendo as arestas (através de 2 vértices), junto com seu respectivo peso
# e preenchendo a matriz 
for i in range(m_arestas):
    vertice_u, vertice_v, peso_p = map(int, input().split())
    matriz_adj[vertice_u - 1][vertice_v - 1] = peso_p # Ajustando os índices

# Recebendo a transformação
transformação_s = float(input())

# Aplicando a transformação
matriz_adj = matriz_adj * transformação_s

#========================================================================================================================
"""
Lógica: Neste bloco verificamos no 'if' se o *Teorema de Perron Frobenius* é satisfeito: se sim, partimos para o cálculo da centralidade; se não, o código imprime a saída desejada. O teorema é fundamental pois garante que há um autovalor dominante e, a partir dele, encontramos o seu autovetor associado. Feito isso, basta encontrar seu maior vértice, que também será o "mais central"
*Teorema de Perron Frobenius: Para qualquer **matriz fortemente conectada** e com todos os valores positivos, Existe um autovalor dominante
** Matriz fortemente conectada: possui aresta entre quaisquer dois vértices
"""
# Cria um grafo direcionado a partir da matriz
grafo = nx.DiGraph(matriz_adj)

# Verifica se o grafo é fortemente conectado e se todos os elementos da matriz são positivos,
# ou seja, basicamente verifica se o teorema é valido :)
if nx.is_strongly_connected(grafo) and np.all(np.array(matriz_adj) >= 0):
    """Se chegou até aqui, o teorema foi satisfeito, então basta calcularmos a centralidade:
    O autovetor correspondente ao maior autovalor indica a centralidade dos vértices em um grafo: quanto maior seu valor, mais central é o vértice."""

    # Calculando os autovalores e os autovetores
    autovalores, autovetores = np.linalg.eig(matriz_adj)

    # Encontrando o autovalor dominante (o maior autovalor)
    maior_autovalor = np.argmax(autovalores)

    # Pega o vetor próprio associado ao maior autovalor
    autovetor_dominante = np.real(autovetores[:, maior_autovalor])

    # O vértice com maior centralidade será o maior no autovetor dominante
    maior_centralidade = np.argmax(autovetor_dominante) + 1 # Ajustando os índices
    print(maior_centralidade)
else:
    print("Bixo SemVerTonha")
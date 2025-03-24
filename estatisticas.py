import numpy as np

# Função que calcula as estatísticas de uma lista de 9 números
def calculate(list):
    # Verifica se a lista contém exatamente 9 números
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Converte a lista em um array e reorganiza para uma matriz 3x3
    new_array = np.array(list).reshape(3, 3)

    # Dicionário para armazenar as estatísticas calculadas
    calculations = {

        # Calcula a média por coluna, por linha e a média geral
        'mean': [
            new_array.mean(axis=0).tolist(),  # Média por coluna
            new_array.mean(axis=1).tolist(),  # Média por linha
            new_array.mean().tolist()         # Média geral
        ],

        # Calcula a variância por coluna, por linha e a variância geral
        'variance': [
            new_array.var(axis=0).tolist(),   # Variância por coluna
            new_array.var(axis=1).tolist(),   # Variância por linha
            new_array.var().tolist()          # Variância geral
        ],

        # Calcula o desvio padrão por coluna, por linha e o desvio padrão geral
        'standard deviation': [
            new_array.std(axis=0).tolist(),   # Desvio padrão por coluna
            new_array.std(axis=1).tolist(),   # Desvio padrão por linha
            new_array.std().tolist()          # Desvio padrão geral
        ],

        # Calcula o valor máximo por coluna, por linha e o valor máximo geral
        'max': [
            new_array.max(axis=0).tolist(),   # Máximo por coluna
            new_array.max(axis=1).tolist(),   # Máximo por linha
            new_array.max().tolist()          # Máximo geral
        ],

        # Calcula o valor mínimo por coluna, por linha e o valor mínimo geral
        'min': [
            new_array.min(axis=0).tolist(),   # Mínimo por coluna
            new_array.min(axis=1).tolist(),   # Mínimo por linha
            new_array.min().tolist()          # Mínimo geral
        ],

        # Calcula a soma por coluna, por linha e a soma geral
        'sum': [
            new_array.sum(axis=0).tolist(),   # Soma por coluna
            new_array.sum(axis=1).tolist(),   # Soma por linha
            new_array.sum().tolist()          # Soma geral
        ]
    }
    
    # Retorna o dicionário com as estatísticas calculadas
    return calculations
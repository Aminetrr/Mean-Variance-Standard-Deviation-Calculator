import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 Numpy array
    matrix = np.array(lst).reshape(3, 3)
    
    # Calculate the required statistics
    calculations = {
        'mean': [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()],
        'variance': [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()],
        'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()],
        'max': [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).tolist()],
        'min': [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).tolist()],
        'sum': [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()]
    }
    
    return calculations

# Demander à l'utilisateur d'entrer 9 chiffres
user_input = input("Entrez 9 chiffres séparés par des espaces : ")
input_list = list(map(int, user_input.split()))

# Appel de la fonction calculate
try:
    result = calculate(input_list)
    print(result)
except ValueError as e:
    print(e)

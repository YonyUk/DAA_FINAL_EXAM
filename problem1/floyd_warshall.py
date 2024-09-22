def init_memory(matriz):
    n = matriz.shape[0]
    memory = {}
    for i in range(n):
        for j in range(n):
            if matriz[i,j] > 0:
                memory[(i,j)] = 1
            if i == j:
                memory[(i,j)] = 0
    return memory

def floy_warshall_modified(matriz):
    n = matriz.shape[0]
    memory = init_memory(matriz)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matriz[i,k] > 0 and matriz[k,j] > 0:
                    if matriz[i,k] + matriz[k,j] < matriz[i,j]:
                        matriz[i,j] = matriz[i,k] + matriz[k,j]
                        memory[(i,j)] = memory[(i,k)] + memory[(k,j)]
    return memory
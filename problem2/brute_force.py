"""
brute force

brute force solution for problem 2
"""

from itertools import combinations
from problem2.tester import check

def brute_force(robots):
    """
    cada elemento de 'robots' debe ser una tupla donde el primer elemento es la faccion,
    y el segundo elemento es una lista donde la pieza i pertenece al fabricante en la posicion i de dicha lista
    """
    crews = {}
    relations = set()
    for i in range(len(robots)):
        if not robots[i][0] in crews.keys():
            crews[robots[i][0]] = [i]
            pass
        else:
            crews[robots[i][0]].append(i)
            pass
        pass
    for i in range(len(robots)):
        for j in range(i + 1,len(robots)):
            for piece in robots[i][1]:
                if piece in robots[j][1]:
                    relations.add((i,j))
                    relations.add((j,i))
                    break
                pass
            pass
        pass
    crews = [crews[key] for key in crews.keys()]
    robots = [i for i in range(len(robots))]
    for i in range(1,len(robots) + 1):
        for combination in combinations(robots,i):
            if check(combination,crews,relations):
                return True
            pass
        pass
    return False

def brute_force_improved(robots):
    """
    cada elemento de 'robots' debe ser una tupla donde el primer elemento es la faccion,
    y el segundo elemento es una lista donde la pieza i pertenece al fabricante en la posicion i de dicha lista
    """
    crews = {}
    relations = set()
    for i in range(len(robots)):
        if not robots[i][0] in crews.keys():
            crews[robots[i][0]] = [i]
            pass
        else:
            crews[robots[i][0]].append(i)
            pass
        pass
    for i in range(len(robots)):
        for j in range(i + 1,len(robots)):
            for piece in robots[i][1]:
                if piece in robots[j][1]:
                    relations.add((i,j))
                    relations.add((j,i))
                    break
                pass
            pass
        pass
    crews = [crews[key] for key in crews.keys()]
    robots = [i for i in range(len(robots))]
    for combination in combinations(robots,len(crews)):
        if check(combination,crews,relations):
            return True
        pass
    return False

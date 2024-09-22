"""
tester

the tester module
"""

import random

def check_crews(robots,crews):
    for crew in crews:
        yes = False
        for robot in robots:
            if robot in crew:
                yes = True
                break
            pass
        if not yes:
            return False
        pass
    return True

def check_relations(robots,relations):
    for i in range(len(robots)):
        for j in range(i + 1,len(robots)):
            if not (i,j) in relations:
                return False
            pass
        pass
    return True

def check(robots,crews,relations):
    return check_crews(robots,crews) and check_relations(robots,relations)

def generate(min_cases,max_cases,tests_cases=100,seed=2,pseed=2):
    """
    seed: usado para variar la probabilidad de que la respuesta sea negativa
    pseed: usado para controlar la probabilidad de que los robots compartan piezas
    """
    
    for _ in range(tests_cases):
        size = random.randint(min_cases,max_cases)
        robots = []
        for _ in range(size):
            faction = random.randint(0,int(size // pseed))
            pieces = [random.randint(0,int(size // pseed)) for _ in range(random.randint(1,int(size*seed)))]
            robots.append((faction,list(set(pieces))))
            pass
        yield robots
        pass
    pass

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

def generate_tuple(min_size,max_size,tests_cases=100):
    for i in range(tests_cases):
        size = random.randint(min_size,max_size)
        robots = [i for i in range(size)]
        R = [i for i in range(size)]
        P = []
        F = []

        random.shuffle(robots)
        while len(robots) > 0:
            end = random.randint(1,len(robots) - random.randint(0,len(robots) - 1))
            P.append(robots[:end])
            robots = robots[end:]
            pass
        
        f_count = random.randint(0,size**2 - random.randint(size**2 // 2,size**2))
        for _ in range(f_count):
            r0 = random.randint(0,len(R))
            options = [i for i in range(len(R)) if not i == r0]
            r1 = random.choice(options)
            if not (r0,r1) in F:
                F += [(r0,r1),(r1,r0)]
                pass
            pass
        if i % 2 == 0:
            yield R,P,make_no_transitive_relation(F)
            pass
        else:
            yield R,P,make_transitive_relation(F)
            pass
        pass
    pass

def make_no_transitive_relation(pairs):
    while True:
        ok = True
        for p0 in pairs:
            for p1 in pairs:
                if not p0 == p1 and p0[1] == p1[0] and not p0[0] == p1[1]:
                    if (p0[0],p1[1]) in pairs:
                        pairs.remove((p0[0],p1[1]))
                        pairs.remove((p1[1],p0[0]))
                        ok = False
                        pass
                    break
                pass
            if not ok:
                break
            pass
        if ok:
            break
        pass
    return pairs

def make_transitive_relation(pairs):
    while True:
        ok = True
        for p0 in pairs:
            for p1 in pairs:
                if not p0 == p1 and p1[0] == p0[1] and not p1[1] == p0[0] and not (p0[0],p1[1]) in pairs:
                    pairs.append((p0[0],p1[1]))
                    pairs.append((p1[1],p0[0]))
                    ok = False
                    break
                pass
            if not ok:
                break
            pass
        if ok:
            break
        pass
    return pairs

def encode_problem_instance(data):
    R,P,F = data[0],data[1],data[2]
    output = []
    for robot in R:
        pieces = [robot]
        r_faction = -1
        for p in P:
            if robot in p:
                r_faction = P.index(p)
                break
            pass
        for r in R:
            if not r == robot and (robot,r) in F:
                pieces.append(r)
                pass
            pass
        output.append((r_faction,pieces))
        pass
    return output

def generate(min_size,max_size,tests_cases=100):
    """
    seed: usado para variar la probabilidad de que la respuesta sea negativa
    pseed: usado para controlar la probabilidad de que los robots compartan piezas
    """
    return map(encode_problem_instance,generate_tuple(min_size,max_size,tests_cases))
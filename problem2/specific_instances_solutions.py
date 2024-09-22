"""
specific instances solutions

implementaciones especificas para algunas instancias del problema 2
"""

def transitive_instance_solution(robots):
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
    return _transitive_instance_solution(robots,crews,relations)

def _transitive_instance_solution(robots,crews,relations):

    solution = []
    crews_taken = []
    for robot in robots:
        if len(solution) == 0:
            solution.append(robot)
            for crew in crews:
                if robot in crew:
                    crews_taken.append(crew)
                    break
                pass
            pass
        elif len(solution) == len(crews):
            return True
        else:
            for crew in crews:
                if robot in crew and not crew in crews_taken:
                    if (solution[0],robot) in relations:
                        solution.append(robot)
                        crews_taken.append(crew)
                        break
                    pass
                pass
            pass
        pass
    return len(solution) == len(crews)

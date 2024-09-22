"""
problem2

todos los metodos usados para la solucion del problema 2
"""

from problem2.brute_force import brute_force,brute_force_improved
from problem2.tester import check,generate
from problem2.specific_instances_solutions import transitive_instance_solution
from datetime import datetime

def Test(tests_cases,test_function,validator_function=brute_force):

    green = '\033[32m'
    red = '\033[31m'
    reset = '\033[0m'
    
    cases = 0
    wrong_counter = 0
    for c in tests_cases:
        cases += 1
        t0 = datetime.now()
        t_result = test_function(c)
        t0 = datetime.now() - t0

        t1 = datetime.now()
        v_result = validator_function(c)
        t1 = datetime.now() - t1

        print(f'{green} test case number {cases} with size {len(c)}{reset}')
        print(f'{green} the test_function took {t0} in compute the result{reset}')
        print(f'{green} the validator_function took {t1} in compute the result{reset}')

        if not t_result == v_result:
            wrong_counter += 1
            print(f'{red} test case number {cases} wrong result for case: {c}{reset}\n')
            pass
        else:
            print(f'{green} ok {reset}\n')
            pass

        pass
    print(f'{red}{wrong_counter} wrong results {green} from {cases} testcases{reset}')
    pass
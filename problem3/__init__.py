"""
problem3

lo necesario para el analisis del problema 3
"""
from problem3.brute_force import brute_force
from problem3.recursive_solution import solve
from problem3.dynamic import dynamic_solve
from problem3.greedy import longest_good_sequence
from problem3.tester import is_good_secuence,generate
from datetime import datetime

green = "\033[32m"
red = "\033[31m"
reset = "\033[0m"

def Test(tests_cases,test_function,validator_function=brute_force):
    counter = 0
    wrong_counter = 0
    for test in tests_cases:
        counter += 1
        start_temp = datetime.now()
        result = test_function(test)
        t0 = datetime.now() - start_temp
        
        start_temp = datetime.now()
        possible_solutions = validator_function(test)
        t1 = datetime.now() - start_temp
        
        print(f'{green}testcase number {counter} with size {len(test)}{reset}')
        print(f'{green}the test_function took {t0} in compute the result{reset}')
        print(f'{green}the validator_function took {t1} in compute all the possibles results{reset}')
        
        if not result in possible_solutions:
            wrong_counter += 1
            print(f"{red}wrong result for testcase: {test}{reset}\n")
        else:
            print(f'{green}ok{reset}\n')
        pass
    print(f"{red}{wrong_counter} wrong results {green} from {counter} testcases {reset}")
    pass
import random
import numpy as np
import time

'''
    A is an n x n matrix
    1 <= A[i].length <= 30
    0 <= A[i][j] <= 100 
    B.Length = A[i]
    The solution, if it exists, must always be an integer.

    Good luck 😀
'''

#-----------------Write your code here-----------------

def Linear_Equation_System_Solver(A, B):
    
    return []
    
    


#-----------------Parameters-----------------

solvable_tests = 1000 # > 1000
non_solvable_tests = 100 # > 100
min_size = 1 # 1
max_size = 30 # > 30

#-----------------Dont touch!-----------------

def generate_integer_matrix(rows, cols, min_val=-10, max_val=10):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def generate_integer_vector(n, min_val=-10, max_val=10):
    return [random.randint(min_val, max_val) for _ in range(n)]

def is_unique_solution(A, B):
    try:
        np.linalg.solve(A, B)
        return True
    except np.linalg.LinAlgError:
        return False

def generate_test_case(n, min_val=-10, max_val=10):
    while True:
        # Generate a random solution
        solution = generate_integer_vector(n, min_val, max_val)
        
        # Generate a random matrix
        A = generate_integer_matrix(n, n, min_val, max_val)
        
        # Calculate the corresponding B vector
        B = [sum(A[i][j] * solution[j] for j in range(n)) for i in range(n)]
        
        # Check if the system has a unique solution
        if is_unique_solution(A, B):
            return A, B, solution

def generate_non_solvable_test_case(n, min_val=-10, max_val=10):
    # Generate a random (n x n) matrix
    A = generate_integer_matrix(n, n, min_val, max_val)
    
    # Generate a random B vector
    B = generate_integer_vector(n, min_val, max_val)

    # Force the system to be non-solvable
    if n == 1:
        A[0][0] = 0
        B[0] = random.randint(1, 10)  # Random non-zero value
    else:
        zero_row = [0] * n
        A[0] = zero_row
        B[0] = random.randint(1, 10)  # non-zero value to ensure inconsistency
    
    return A, B

def test_Linear_Equation_System_Solver(solvable_tests, non_solvable_tests, min_size, max_size):

    success_count = 0
    total_tests = solvable_tests + non_solvable_tests

    failed_cases = []

    # Start the stopwatch
    start_time = time.time()

    for _ in range(solvable_tests):
        n = random.randint(min_size, max_size)  # Random size between min_size and max_size
        A, B, expected_solution = generate_test_case(n)
        
        solution = Linear_Equation_System_Solver([row[:] for row in A], B[:])

        if solution == expected_solution:
            success_count += 1
        else:
            failed_cases.append((A, B, expected_solution, solution))

    for _ in range(non_solvable_tests):
        n = random.randint(min_size, max_size)  # Random size between min_size and max_size
        A, B = generate_non_solvable_test_case(n)
        expected_solution = []
        
        solution = Linear_Equation_System_Solver([row[:] for row in A], B[:])

        if solution == expected_solution:
            success_count += 1
        else:
            failed_cases.append((A, B, expected_solution, solution))

    # Stop the stopwatch and calculate the elapsed time
    elapsed_time = time.time() - start_time

    print(f"\n--- {success_count}/{total_tests} tests passed. The operation took {elapsed_time:.3f} secounds. ---\n")

    for A, B, expected_solution, solution in failed_cases:
        print(f"Input: A = {A}, B = {B}")
        print(f"Output: {solution}")
        print(f"Expected Solution: {expected_solution}")
        print()

# Test the solver
test_Linear_Equation_System_Solver(solvable_tests, non_solvable_tests, min_size, max_size)
# Algorithm for finding the reciprocal of a number N using Newton's Iterative Formula:
# 1. Input the number N whose reciprocal is to be found
# 2. Set initial guess x0 (default = 0.1)
# 3. Set number of iterations (default = 10)
# 4. For each iteration i from 1 to iterations:
#    a. Calculate xi = xi-1 * (2 - xi-1 * N)
#    b. Print current approximation
# 5. Return final approximation of 1/N

def newtons_iterative_reciprocal(N, x0=0.1, iterations=10):
    if N == 0:
        return None
    
    print(f"Finding the reciprocal of {N} using Newton's Iterative Formula")
    print(f"Initial guess x0 = {x0}")
    
    xi = x0
    for i in range(1, iterations + 1):
        xi = xi * (2 - xi * N)
        print(f"Iteration {i}: x{i} = {xi}")
    
    print(f"Approximate reciprocal of {N} after {iterations} iterations: {xi}")
    return xi

# Test the function
if __name__ == "__main__":
    N = 5
    x0 = 0.1
    iterations = 10
    result = newtons_iterative_reciprocal(N, x0, iterations)
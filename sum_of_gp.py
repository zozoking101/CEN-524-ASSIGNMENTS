import math as m


a = input('First term a: ')
r = input('Geometric progression r: ')
n = int(input('Number of terms n (0 if inf): '))
# Function to calculate the sum of a geometric progression
def gp_sum(a, r, n):
    if n != 0:
        if r < 1:
            a = ((a * (1 - r ** n))/(1 - r))
            return a
        if r > 1:
            a = ((a * (r ** n - 1))/(r - 1))
            return a
    elif n == 0:
        a = a/(1-r)
        return a
    else:
        return

# Print the sum

print(f'Sum of the geometric progression: {gp_sum(float(a), float(r), n)}')      
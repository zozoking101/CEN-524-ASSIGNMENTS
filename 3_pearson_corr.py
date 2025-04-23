import math

# Algorithm for calculating the Pearson correlation coefficient
# between two lists of numbers.

# 1. Read the two lists of numbers, x and y.
# 2. Check if the lengths of the two lists are equal.
# 3. Calculate the means of x and y.
# 4. Calculate the covariance of x and y.
# 5. Calculate the standard deviations of x and y.
# 6. Calculate the Pearson correlation coefficient using the formula:
#    r = covariance(x, y) / (std_dev(x) * std_dev(y))
# 7. Return the Pearson correlation coefficient.
# 8. If the lengths of the two lists are not equal, return None.
# 9. If the lists are empty, return None.
# 10. If the lists contain non-numeric values, return None.

def pearson_correlation(x, y):
    # Check if lengths are equal
    if len(x) != len(y):
        return None
    
    # Check if lists are empty
    if len(x) == 0 or len(y) == 0:
        return None
    
    try:
        n = len(x)
        
        # Calculate means
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        
        # Calculate covariance
        covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        
        # Calculate standard deviations
        std_dev_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x))
        std_dev_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y))
        
        # Check for zero standard deviation
        if std_dev_x == 0 or std_dev_y == 0:
            return None
        
        # Calculate correlation coefficient
        r = covariance / (std_dev_x * std_dev_y)
        
        return r
        
    except (TypeError, ValueError):
        # Handle non-numeric values
        return None

# Test the function
if __name__ == "__main__":
    # Test case 1: Positive correlation
    x1 = [1, 2, 3, 4, 5]
    y1 = [2, 4, 5, 4, 5]
    print(f"Test 1: {pearson_correlation(x1, y1):.4f}")
    
    # Test case 2: Negative correlation
    x2 = [1, 2, 3, 4, 5]
    y2 = [5, 4, 3, 2, 1]
    print(f"Test 2: {pearson_correlation(x2, y2):.4f}")
    
    # Test case 3: No correlation
    x3 = [1, 2, 3, 4, 5]
    y3 = [1, 1, 1, 1, 1]
    print(f"Test 3: {pearson_correlation(x3, y3)}")

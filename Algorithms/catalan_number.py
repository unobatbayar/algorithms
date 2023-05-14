def catalan_number(n):
    """
    Calculates the nth Catalan number using the Catalan number algorithm.
    
    Args:
        n (int): The index of the desired Catalan number.
    
    Returns:
        int: The nth Catalan number.
    """
    # Base case: Catalan number for n = 0 or n = 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Initialize the result variable
    result = 0
    
    # Iterate from i = 0 to n-1
    for i in range(n):
        # Compute the product of two terms: (2*(i+1)*(2*(i+1)-1))
        # and the Catalan number calculated recursively for i
        product = (2 * (i + 1) * (2 * (i + 1) - 1)) * catalan_number(i)
        
        # Add the product to the result
        result += product
    
    # Return the computed result
    return result

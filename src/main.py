def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    
    Args
    values:
        1D array of values (list or numpy array)
    num_iteration:
        Integer to set the number of iterations
    """
    # code
    for _ in range(num_iterations):
        
        # Get the maximum value and it's index in the list. Then calculate the working share
        max_value = max(values)
        idx = values.index(max_value)
        current_share = max_value*share
        
        # Update the values to reflect the current iteration
        # Make sure the index does not go out of bounds
        if idx-1 == -1:
            values[len(values)-1] = values[len(values)-1] + current_share
        else:
            values[idx-1] = values[idx-1] + current_share
        
        # Subtract the distributed amount from the maximum value
        values[idx] = values[idx] - current_share*2
        
        # Make sure the index does not go out of bounds
        if idx+1 == len(values):
            values[0] = values[0] + current_share
        else:
            values[idx+1] = values[idx+1] + current_share
            
        # Make return value    
        values_new = values
            
    return values_new

if __name__ == "__main__":
    print(fair_sharer([1000,0,800,0], 1))
def two_sum(nums, target):
    # Create a dictionary to store the numbers and their indices.
    num_dict = {}
    
    # Iterate through the array.
    for i, num in enumerate(nums):
        # Calculate the complement (the number needed to reach the target).
        complement = target - num
        
        # Check if the complement exists in the dictionary.
        if complement in num_dict:
            # If found, return the indices of the two numbers.
            return (num_dict[complement], i)
        
        # If not found, add the current number to the dictionary.
        num_dict[num] = i

from typing import List

def finalValueAfterOperations(operations: List[str]) -> int:
    """
    Given a list of operations on a variable X initialized at 0, calculate the final value of X
    after all operations are applied.

    Parameters:
    - operations (List[str]): A list of strings, each representing an operation on X.
    
    Returns:
    - int: The final value of X after all operations.
    """
    # Count total increment and decrement operations
    return operations.count("++X") + operations.count("X++") - operations.count("--X") - operations.count("X--")

# Example usage:
if __name__ == "__main__":
    # Sample operations list
    operations = ["++X", "X++", "--X", "X--", "X++"]
    
    # Get the result after all operations
    result = finalValueAfterOperations(operations)
    
    # Print the result
    print("Final value of X:", result)

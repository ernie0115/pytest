import pytest 

def add(x, y): 
    """It is a summation function, returning sum of 2 numbers.""" 
    return x + y 

def test_add(): 
    assert add(1, 2) == 3, "It should return the sum of 2 numbers." 
    assert add(-1, 1) == 0, "Summation of -1 and 1 is 0." 
    assert add(-1, -1) == -2, "Inspect 2 negative numbers summation." 

# pytest 

# if __name__ == '__main__': 
#     pytest 
#     test_add() 
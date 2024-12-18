import pytest 

def add(x, y): 
    """It is a summation function, returning sum of 2 numbers.""" 
    return x + y 

@pytest.mark.parametrize("test_input,expected", [(1, 2), (3, 4), (5, 6)]) 
def test_add(test_input, expected): 
    assert add(test_input, 1) == expected 
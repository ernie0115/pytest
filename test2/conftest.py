import pytest 

@pytest.fixture 
def dataset_test2(): 
    """Return some data to test functions""" 
    print("dataset_test2 fixture is being called") 
    return {'data3': 3, 'data4': 4} 
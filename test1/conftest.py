import pytest 

@pytest.fixture 
def dataset_test1(): 
    """Return some data to test functions""" 
    print("dataset_test1 fixture is being called") 
    return {'data1': 1, 'data2': 2} 
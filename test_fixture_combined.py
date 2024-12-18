import pytest 
from test1.conftest import dataset_test1 
from test2.conftest import dataset_test2 

# Assuming pytest will automatically find the fixtures in the conftest.py files in the test1 and test2 directories 

def test_combined_datasets(dataset_test1): 
    # This will use the dataset fixture from the closest conftest.py file 
    assert dataset_test1['data1'] == 1 
    assert dataset_test1['data2'] == 2 

def test_combined_datasets_test2(dataset_test2): 
    # To explicitly use the dataset fixture from test2, you can create a separate test function 
    assert dataset_test2['data3'] == 3 
    assert dataset_test2['data4'] == 4 
import pytest 

# @pytest.fixture
# def db_connection():
#     connection = create_connection()
#     yield connection
#     connection.close() 

# def test_query(db_connection):
#     # 使用db_connection進行測試
#     assert db_connection.query("SELECT * FROM table") is not None 

@pytest.fixture 
def dataset(): 
    """Return some data to test functions""" 
    return {'data1': 1, 'data2': 2} 

def test_dataset(dataset): 
    """test and confirm fixture value""" 
    assert dataset == {'data1': 1, 'data2': 2} 

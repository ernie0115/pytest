# Pytest 
Pytest automatically discovers any function prefixed with "test_" in the specified file (Ex: test_add.py, test_fixture.py, test_fixture_combined.py, test_parametrize.py). 

# Fixture 
Provide a predefined set of data that can be used across multiple test functions. 

# Parametrize 

# (A) test_add.py 
## **Objective:** 
It checks whether "add()" function is giving correct result or not. 

## **Annotation:** 
- "add()" function returns the sum of 2 input arguments. 
- "test_add()" function serves as a unit test for the "add()" function and checks the correctness of the "add()" function for different sets of input arguments.
- Reporting Results: If all assertions pass (meaning the add() function behaves as expected), pytest will report that the test has passed.
- Reporting Results: If any assertion fails, pytest will provide an error message indicating which assertion failed and the reason for the failure.

## **Guide:**  
- Enter "pytest test_add.py". 

# (B) test_fixture.py 
## **Objective:** 
It checks whether "dataset()" function is giving correct result or not. 

## **Annotation:**  
- The "@pytest.fixture" decorator above "dataset()" function indicates that the "dataset()" function is a fixture. 
- The "test_dataset" function is a test case that uses the "dataset" fixture. 
- By including "dataset" as a parameter in the test function, pytest automatically provides the fixture's return value when the test is run. 
- The test asserts that the value returned by the fixture is equal to the expected dictionary, confirming that the fixture is set up correctly.

## **Guide:**  
- Enter "pytest test_fixture.py". 

# (C) test_fixture_combined.py 
## **Objective:** 
It checks whether "dataset_test1()" and "dataset_test2()" function are giving correct result or not. 

## **Annotation:** 
- "def test_combined_datasets(dataset_test1)": It defines a test function that uses the "dataset_test1" fixture. The function asserts that the values in the dataset_test1 dictionary match expected values (1 and 2).
- "def test_combined_datasets_test2(dataset_test2)": It defines another test function that uses the "dataset_test2" fixture. It asserts that the values in the dataset_test2 dictionary match expected values (3 and 4).

## **Guide:**  
- Enter "pytest test_fixture_combined.py". 

## **Issue:**  
- Normally, "from test1.conftest import dataset_test1" and "from test2.conftest import dataset_test2" aren't required, given that there is corresponding "conftest.py" in "test1" and "test2" folders.
- However, pytest returns "dataset_test1" and "dataset_test2" not being recognized,
- even the fixtures are listed when I run "pytest --fixtures", indicating that "dataset_test1" and "dataset_test2" are correctly defined in their respective "conftest.py" files. 

# (D) test1\conftest.py 
## **Objective:** 
Provide "test_fixture_combined.py" with fixture to do testing. 

## **Annotation:** 
- The "@pytest.fixture" decorator above "dataset_test1()" function indicates that the "dataset_test1()" function is a fixture. 

# (E) test2\conftest.py 
## **Objective:** 
Provide "test_fixture_combined.py" with fixture to do testing. 

## **Annotation:** 
- The "@pytest.fixture" decorator above "dataset_test2()" function indicates that the "dataset_test2()" function is a fixture. 

# (F) test_parametrize.py 
## **Objective:** 
It checks whether "add()" function is giving correct result or not for different sets of input arguments. 

## **Annotation:** 
- The "@pytest.mark.parametrize" decorator above "test_add()" function creates a parameterized test.
- It specifies that the "test_add()" function will be run multiple times with different sets of inputs. 

## **Guide:**  
- Enter "pytest test_parametrize.py". 

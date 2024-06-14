import pytest
import os
from gendiff import generate_diff

@pytest.fixture
def expected():
    file_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'expected_f1_f2.txt')
    expected_string = ""
    try: 
        with open(file_path, 'r') as output:
            expected_string = output.read()
    except (FileNotFoundError, PermissionError) as err:
        print(f"Error opening expected_f1_f2.txt when testing: {err}")
    return expected_string

@pytest.fixture
def file1_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')

@pytest.fixture
def file2_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')

def test_normal_case(expected, file1_path, file2_path):
    assert generate_diff(file1_path, file2_path) == expected

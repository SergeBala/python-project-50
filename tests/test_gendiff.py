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
def file_path():
    def _file_path(filename):
        return os.path.join(os.path.dirname(__file__), 'fixtures', filename)
    return _file_path

def test_normal_case(file_path, expected):
    file1_path = file_path('file1.json')
    file2_path = file_path('file2.json')
    assert generate_diff(file1_path, file2_path) == expected

def test_list_json(file_path):
    list_json_path = file_path('list.json')
    file1_path = file_path('file1.json')
    assert generate_diff(list_json_path, file1_path) == None

def test_empty_json(file_path):
    empty_json_path = file_path('empty.json')
    file1_path = file_path('file1.json')
    assert generate_diff(empty_json_path, file1_path) == None
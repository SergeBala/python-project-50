import json


def generate_diff(file_path1, file_path2):
    try:
        with open(file_path1, 'r') as file1:
            data_1 = json.load(file1)
    except (FileNotFoundError, PermissionError) as err:
        print(f"Error opening file1: {err}")
        data_1 = None
        return None
    except (json.JSONDecodeError):
        print(f"Error: The file '{file_path1}' contains invalid JSON.")
        return None
    try:
        with open(file_path2, 'r') as file2:
            data_2 = json.load(file2)
    except (FileNotFoundError, PermissionError) as err:
        print(f"Error opening file1: {err}")
        data_2 = None
        return
    except (json.JSONDecodeError):
        print(f"Error: The file '{file_path2}' contains invalid JSON.")
        return None
    if (not isinstance(data_1, dict)) or (not isinstance(data_2, dict)):
        print("Only works with json files that start with curly braces")
        return None
    result_str = "{\n"
    sorted_keys1 = sorted(data_1.keys())
    sorted_keys2 = sorted(data_2.keys())
    unique_sorted_keys = sorted((set(sorted_keys1)).union(set(sorted_keys2)))
    for key in unique_sorted_keys:
        if key in sorted_keys1 and key in sorted_keys2:
            if data_1[key] == data_2[key]:
                result_str += f"    {key}: {data_1[key]}\n"
            else:
                result_str += f"  - {key}: {data_1[key]}\n"
                result_str += f"  + {key}: {data_2[key]}\n"
        elif key in sorted_keys1 and key not in sorted_keys2:
            result_str += f"  - {key}: {data_1[key]}\n"
        else:
            result_str += f"  + {key}: {data_2[key]}\n"
    result_str += "}"
    return result_str

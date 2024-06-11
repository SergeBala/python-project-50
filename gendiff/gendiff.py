import json

def generate_diff(file_path1, file_path2):
    try:
        with open(file_path1, 'r') as file1:
            data_1 = json.load(file1)
    except (FileNotFoundError, PermissionError) as err: 
        print(f"Error opening file1: {err}")
        data_1 = None
    try:
        with open(file_path2, 'r') as file2:
            data_2 = json.load(file2)
    except (FileNotFoundError, PermissionError) as err: 
        print(f"Error opening file1: {err}")
        data_2 = None
    if (not isinstance(data_1, dict)) or (not isinstance(data_2, dict)):
        return ""
    result_str = "{\n"
    ordered_keys_1 = sorted(data_1.keys())
    ordered_keys_2 = sorted(data_2.keys())
    unique_ordered_keys_1_2 = sorted((set(ordered_keys_1)).union(set(ordered_keys_2)))
    for key in unique_ordered_keys_1_2:
        if key in ordered_keys_1 and key in ordered_keys_1:
            if data_1[key] == data_2[key]:
                result_str += f"    {key}: {data_1[key]}\n"
            else: 
                result_str += f"  - {key}: {data_1[key]}\n"
                result_str += f"  + {key}: {data_2[key]}\n"
        elif key in ordered_keys_1 and key not in ordered_keys_2:
            result_str += f"  - {key}: {data_1[key]}\n"
        else:
            result_str += f"  + {key}: {data_2[key]}\n"
    result_str += "\n}"
    return result_str




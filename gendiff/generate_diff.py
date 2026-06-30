import json


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as f1:
        data1 = json.load(f1)
    with open(file_path2, 'r') as f2:
        data2 = json.load(f2)

    keys = data1.keys() | data2.keys()
    sorted_keys = sorted(keys)

    result = []
    for key in sorted_keys:
        if key in data1 and key not in data2:
            result.append(f"  - {key}: {to_str(data1[key])}")
        elif key in data2 and key not in data1:
            result.append(f"  + {key}: {to_str(data2[key])}")
        elif data1[key] != data2[key]:
            result.append(f"  - {key}: {to_str(data1[key])}")
            result.append(f"  + {key}: {to_str(data2[key])}")
        else:
            result.append(f"    {key}: {to_str(data1[key])}")

    inner_text = '\n'.join(result)
    return f"{{\n{inner_text}\n}}"

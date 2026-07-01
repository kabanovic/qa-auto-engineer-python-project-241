import os

from gendiff.formatters.stylish import make_stylish
from gendiff.parser import parse


def get_data(file_path):
    format_name = os.path.splitext(file_path)[1][1:].lower()

    with open(file_path, 'r') as file:
        content = file.read()

    return parse(content, format_name)


def build_diff(data1, data2):
    keys = data1.keys() | data2.keys()
    sorted_keys = sorted(keys)
    diff = []

    for key in sorted_keys:
        if key in data1 and key not in data2:
            diff.append({'key': key, 'type': 'deleted', 'value': data1[key]})
        elif key not in data1 and key in data2:
            diff.append({'key': key, 'type': 'added', 'value': data2[key]})
        elif data1[key] != data2[key]:
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })
        else:
            diff.append({'key': key, 'type': 'unchanged', 'value': data1[key]})

    return diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    diff = build_diff(data1, data2)

    return make_stylish(diff)
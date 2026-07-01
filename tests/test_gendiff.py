import os

from gendiff import generate_diff


def get_data_path(filename):
    return os.path.join('tests', 'test_data', filename)


def read_file(filename):
    with open(get_data_path(filename), 'r') as file:
        return file.read()


def test_generate_diff_flat_json():
    file1_path = get_data_path('file1.json')
    file2_path = get_data_path('file2.json')

    expected = read_file('result_stylish.txt')

    actual = generate_diff(file1_path, file2_path)

    assert actual == expected


def test_generate_diff_flat_yaml():
    file1_path = get_data_path('file1.yml')
    file2_path = get_data_path('file2.yaml')

    expected = read_file('result_stylish.txt')

    actual = generate_diff(file1_path, file2_path)

    assert actual == expected


def test_generate_diff_plain_json():
    file1_path = get_data_path('file1.json')
    file2_path = get_data_path('file2.json')
    expected = read_file('result_plain.txt')

    actual = generate_diff(file1_path, file2_path, 'plain')
    assert actual == expected


def test_generate_diff_plain_yaml():
    file1_path = get_data_path('file1.yml')
    file2_path = get_data_path('file2.yaml')
    expected = read_file('result_plain.txt')

    actual = generate_diff(file1_path, file2_path, 'plain')
    assert actual == expected
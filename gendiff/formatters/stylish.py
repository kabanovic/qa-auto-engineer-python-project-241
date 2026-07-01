def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def make_stylish(diff):
    result = []
    for item in diff:
        key = item['key']
        status = item['type']

        if status == 'unchanged':
            result.append(f"    {key}: {to_str(item['value'])}")
        elif status == 'deleted':
            result.append(f"  - {key}: {to_str(item['value'])}")
        elif status == 'added':
            result.append(f"  + {key}: {to_str(item['value'])}")
        elif status == 'changed':
            result.append(f"  - {key}: {to_str(item['old_value'])}")
            result.append(f"  + {key}: {to_str(item['new_value'])}")

    inner_text = '\n'.join(result)
    return f"{{\n{inner_text}\n}}"

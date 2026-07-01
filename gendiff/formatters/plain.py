def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def make_plain(diff):
    result = []

    for item in diff:
        key = item['key']
        status = item['type']

        if status == 'deleted':
            result.append(f"Property '{key}' was removed")
        elif status == 'added':
            val = to_str(item['value'])
            result.append(f"Property '{key}' was added with value: {val}")
        elif status == 'changed':
            old_val = to_str(item['old_value'])
            new_val = to_str(item['new_value'])
            result.append(
                f"Property '{key}' was updated. From {old_val} to {new_val}"
            )

    return '\n'.join(result)
import re

def parse_nested_keys(form_data):
    result = {}

    for key, value in form_data.items():
        current = result
        parts = re.findall(r'([^\[\]]+)|\[(\d+)\]', key)
        parts = [p[0] if p[0] else int(p[1]) for p in parts]

        for i, part in enumerate(parts):
            if i == len(parts) - 1:
                if isinstance(part, int):
                    while len(current) <= part:
                        current.append(None)
                    current[part] = value
                else:
                    current[part] = value
            else:
                next_part = parts[i + 1]
                if isinstance(part, int):
                    while len(current) <= part:
                        current.append({} if isinstance(next_part, str) else [])
                    if current[part] is None:
                        current[part] = {} if isinstance(next_part, str) else []
                    current = current[part]
                else:
                    if part not in current:
                        current[part] = {} if isinstance(next_part, str) else []
                    current = current[part]

        try:
            current[part] = int(current[part])
        except (ValueError, TypeError):
            pass

    return result
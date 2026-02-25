import re
from typing import Any, Dict, List, Union


NestedType = Union[Dict[str, Any], List[Any]]


def cast_value(value: Any) -> Any:
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return value
    return value


def parse_nested_keys(form_data) -> Dict[str, Any]:
    result: Dict[str, Any] = {}

    for key in form_data:
        values = (
            form_data.getlist(key)
            if hasattr(form_data, "getlist")
            else [form_data[key]]
        )

        for value in values:
            current: NestedType = result

            parts = re.findall(r"([^\[\]]+)|\[(\d+)\]", key)
            parts = [p[0] if p[0] else int(p[1]) for p in parts]

            if not parts:
                continue

            if isinstance(parts[0], int):
                raise ValueError("Root key must be a string.")

            for i, part in enumerate(parts):
                is_last = i == len(parts) - 1

                if is_last:
                    if isinstance(part, int):
                        if not isinstance(current, list):
                            raise TypeError("Invalid nested structure.")

                        while len(current) <= part:
                            current.append(None)

                        current[part] = cast_value(value)

                    else:
                        if not isinstance(current, dict):
                            raise TypeError("Invalid nested structure.")

                        current[part] = cast_value(value)

                else:
                    next_part = parts[i + 1]

                    if isinstance(part, int):
                        if not isinstance(current, list):
                            raise TypeError("Invalid list nesting.")

                        while len(current) <= part:
                            current.append({} if isinstance(next_part, str) else [])

                        if current[part] is None:
                            current[part] = {} if isinstance(next_part, str) else []

                        current = current[part]

                    else:
                        if part not in current:
                            current[part] = {} if isinstance(next_part, str) else []

                        current = current[part]

    return result

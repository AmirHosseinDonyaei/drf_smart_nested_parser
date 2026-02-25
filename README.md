# DRF Smart Nested Parser

A simple parser for Django REST Framework that converts `form-data` and `application/x-www-form-urlencoded` inputs into nested structures (dict / list). For JSON, it uses the default DRF JSON parser without additional conversion.

## Installation

If you're using this package locally, ensure it is importable from your project. If published on PyPI, install it by the package name.

## Usage

### Add to DRF settings

```python
# settings.py
REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": [
        "drf_smart_nested_parser.SmartNestedParser",
    ]
}
```

### Or only for a single view

```python
from rest_framework.views import APIView
from drf_smart_nested_parser import SmartNestedParser

class MyView(APIView):
    parser_classes = [SmartNestedParser]
```

## Input and Output

### Example for `multipart/form-data` or `application/x-www-form-urlencoded`

Form keys with bracket notation (`[]`) are converted to nested structures:

```
user[name] = Amir
user[age] = 30
items[0][title] = Book
items[0][price] = 120
items[1][title] = Pen
```

Output:

```json
{
  "user": {
    "name": "Amir",
    "age": 30
  },
  "items": [
    {"title": "Book", "price": 120},
    {"title": "Pen"}
  ]
}
```

Note: If a value can be converted to a number, it will be cast to `int`.

## Parser Behavior

- If `Content-Type` includes `application/json`, DRF's `JSONParser` is used.
- If `Content-Type` includes `multipart/form-data`, data is parsed and keys are converted to nested structures.
- Otherwise (e.g. `application/x-www-form-urlencoded`), `FormParser` is used and the same conversion applies.

## Limitations and Notes

- Keys should start with a string root (e.g. `items[0]` should be used as part of a root like `items[0][name]` or at least `items[0]` alongside a textual root). A valid example: `items[0][name]`.
- File values in `multipart/form-data` are kept in `files` and are not modified.

## Development

Code layout:

- `parsers.py`: `SmartNestedParser` implementation
- `utils.py`: `parse_nested_keys` helper

## License

MIT

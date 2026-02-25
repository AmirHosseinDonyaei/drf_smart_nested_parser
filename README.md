# DRF Smart Nested Parser

A custom parser class for Django REST Framework (DRF) that converts bracket-notation form keys into properly nested Python structures.

It transparently handles:

* `multipart/form-data`
* `application/x-www-form-urlencoded`
* `application/json` (delegated to DRF's default `JSONParser`)

This allows frontend clients to submit nested data using standard HTML form conventions while preserving DRF’s normal behavior.

---

## Why?

Django REST Framework does **not natively support nested bracket notation** in form submissions such as:

```
user[name]
items[0][title]
```

This parser bridges that gap, enabling clients (Browsers, Postman, Bruno, mobile apps) to send nested form data without switching to JSON payloads.

---

## Features

* Parses nested keys like `user[name]`, `items[0][title]`
* Builds proper nested `dict` and `list` structures
* Preserves uploaded files in `request.FILES`
* Delegates JSON requests to DRF’s native `JSONParser`
* Automatically casts numeric string values to `int` when possible
* Works seamlessly as a global or per-view parser

---

## Requirements

* Python >= 3.8
* Django >= 4.2
* djangorestframework >= 3.14

---

## Installation

Available on PyPI:

```
pip install drf_smart_nested_parser
```

---

## Quick Start

### Global configuration

```python
# settings.py

REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": [
        "drf_smart_nested_parser.SmartNestedParser",
    ]
}
```

This replaces DRF’s default parsers while internally delegating to:

* `JSONParser`
* `MultiPartParser`
* `FormParser`

---

### Per-view usage

```python
from rest_framework.views import APIView
from drf_smart_nested_parser import SmartNestedParser

class MyView(APIView):
    parser_classes = [SmartNestedParser]
```

---

## Example

### Incoming request

(`multipart/form-data` or `application/x-www-form-urlencoded`)

```
user[name] = Amir
user[age] = 30
items[0][title] = Book
items[0][price] = 120
items[1][title] = Pen
```

### Parsed result (`request.data`)

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

Uploaded files remain accessible via:

```python
request.FILES
```

---

## Behavior

| Content-Type                        | Behavior                                                                     |
| ----------------------------------- | ---------------------------------------------------------------------------- |
| `application/json`                  | Uses DRF's `JSONParser` without modification                                 |
| `multipart/form-data`               | Parsed using `MultiPartParser`, then keys are converted to nested structures |
| `application/x-www-form-urlencoded` | Parsed using `FormParser`, then keys are converted to nested structures      |

Numeric string values are automatically cast to `int` when possible.

---

## Key Rules

Valid examples:

```
items[0][name]
user[address][city]
```

Invalid example:

```
[0][name]
```

Keys must start with a string root.

---

## File Handling

File objects are preserved and returned inside `DataAndFiles.files`.
They are **not modified or transformed**.

---

## Use Cases

* Complex nested form submissions
* Frontend frameworks sending bracket-notation keys
* Multipart requests combining nested data + file uploads
* Replacing JSON with form submissions while keeping structure

---

## Project Structure

```
drf_smart_nested_parser/
├── parsers.py
├── utils.py
└── __init__.py
```

---

## License

MIT License

---

## Contributing

Pull requests are welcome.
Please open an issue first to discuss major changes.
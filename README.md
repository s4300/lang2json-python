# Lang2JSON Python
Simple python library that converts .lang files to json, and vice versa.

Licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Installation
You can install this package from PyPI, or from the setup.py file.
```
pip install lang2json
-- OR --
python setup.py install
```

## Examples
Converting JSON into the .lang format
```py
import lang2json

print(lang2json.json_to_lang({
    "hello": "world",
    "lang2json": "working"
}))

# Output:
# hello=world
# lang2json=working
```

Converting JSON into the .lang format
```py
import lang2json

with open("example.lang", "r", encoding="utf-8") as file:
    print(lang2json.lang_to_json(file.readlines()))

# Output: {'hello': 'world', 'lang2json': 'working'}
```
# parser_pro
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Overview

**parser_pro** is a Python library that simplifies JSON data parsing and manipulation. It provides a collection of functions for extracting, transforming, and processing JSON objects and lists efficiently.  


## installation

```commandline
    pip install git+https://github.com/VinayPundhir/parserpro.git
```

## Usage

```comma
>> from parser_pro import parse

>> data = {"name": "parser-pro", "address": {"street": "random"}, "nums": [1, 2, 3, 4]}

>> expr = "address.street"
>> print(parse(data, expr))

random
```

For advanced usage read the [Documentation](https://htmlpreview.github.io/?https://github.com/VinayPundhir/parserpro/blob/master/docs/_build/index.html).
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from jsonschema import validate

if __name__ == "__main__":
    schema = {
    "type": "object",
    "properties": {
        "punkt": {"type": "string"},
        "nomer": {"type": "string"},
        "time": {"type": "number"},
    },
    }

    with open("first.json", "r", encoding="utf-8") as fin:
        a = json.load(fin)
        for i in a:
            validate(instance=i, schema=schema)
import os
import re
from typing import List

from config import Config


def get_file(filename) -> str:
    try:
        with open(os.path.join(Config.DATA_DIR, filename), 'r', encoding='utf-8') as file:
            return file.read()
    except Exception:
        raise


def commands(cmd=None, value1=None, data=None) -> List[str]:
    if cmd == 'filter':
        return list(filter(lambda v: value1 in v, data.split('\n')))
    if cmd == 'map':
        return list(map(lambda v: v.split()[int(value1)], data.split('\n')))
    if cmd == 'unique':
        return list(set(data.split('\n')))
    if cmd == 'sort':
        if value1 == 'desc':
            return sorted(data.split('\n'), reverse=True)
        return sorted(data.split('\n'), reverse=False)
    if cmd == 'limit':
        return [i for i in data[:int(value1)]]
    if cmd == 'regex':
        exp = re.compile(value1)
        return re.findall(exp, data)
    return []
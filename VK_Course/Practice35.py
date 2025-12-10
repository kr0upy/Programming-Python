from collections import defaultdict
from typing import List, Tuple

def fill_specializations(specializations: List[Tuple[str, str]]):
    result = defaultdict(list)
    for spec, name in specializations:
        result[spec].append(name)
    return dict(result) 


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
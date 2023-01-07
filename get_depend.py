import json

from typing import List, Dict
# get project dependencies


FILENAME = "package.json"


def get_all_requirements(file: str = "requirements.txt") -> List[List[str]]:
    with open(file, "r") as req:
        require = req.readlines()
        require = [v.split("==") for v in require]

    return require


def swap_to_dict() -> Dict[str, str]:
    requirements = get_all_requirements()

    dependencies = {
        value[0]: value[1][: -1]
        for value in requirements
    }

    return dependencies


def save_dependencies() -> bool:
    depend = swap_to_dict()

    dependencies = json.dumps(depend, indent=4)

    with open(FILENAME, "w", encoding="utf-8") as dep:
        dep.writelines(dependencies)

    with open(FILENAME, "r") as the:
        check = the.read()

    return len(check) > 0


if __name__ == '__main__':
    save_dependencies()
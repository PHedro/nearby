import json
import os


def write_to_file(data, path):
    with open(path, "w") as data_file:
        for item in data:
            data_file.write("{}, {}\n".format(*item))


def from_file(path, class_to_cast=None):
    if os.path.exists(path) and os.path.isfile(path) and os.path.getsize(path) > 0:
        with open(path, "r") as data_file:
            for line in data_file:
                if class_to_cast:
                    yield class_to_cast(**json.loads(line))
                else:
                    yield json.loads(line)
    else:
        raise FileNotFoundError

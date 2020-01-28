import json
import os


class LocalDAO:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.isfile(file_path):
            with open(file_path, "w") as fp:
                fp.write(json.dumps({}))
        with open(file_path, "r") as fp:
            self.contents = json.loads(fp.read())

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()
        print("Writing back contents into file.")

    def get(self, key):
        if key in self.contents:
            return self.contents[key]
        else:
            raise KeyError("Could not find tiny url {} in database.".format(key))

    def put(self, key, val):
        self.contents[key] = val

    def flush(self):
        with open(self.file_path, "w") as fp:
            fp.write(json.dumps(self.contents, indent=4))





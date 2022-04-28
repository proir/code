from distutils.log import info
import json

class DataBase:
    def __init__(self, Path):
        self.Path = Path
    
    def __enter__(self):
        with open(self.Path) as f:
            self.TempDB = json.load(f)
        return self

    def __exit__(self, *args):
        with open(self.Path, "w") as f:
            json.dump(self.TempDB, f)

    def list(self):
        return self.TempDB.keys()
    def get(self, key):
        return self.TempDB[key]
    def set(self, key, val):
        self.TempDB[key] = val

with DataBase("info.json") as db:
    db.set("Alice", "Reed")
    db.set("aaa", "bbb")
    db.set("foo", "bar")

with DataBase("info.json") as db:
    print(db.get("Alice"))
    print(db.get("aaa"))
    print(db.get("foo"))
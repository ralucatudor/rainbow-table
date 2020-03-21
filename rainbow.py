from pathlib import Path
from hashlib import sha256


class Rainbow:
    # load password
    def load(path):
        print("Loading ", path)
        x = Rainbow()
        passwords = Path(path).read_text().split('\n')
        x.table = {
            sha256(password.encode("utf-8")).hexdigest(): password
            for password in passwords
        }
        print("The rainbow table is ", x.table)
        return x

    # find password by hash function
    def find(self, hash):
        # table becomes self.table
        if hash in self.table:
            return self.table[hash]
        return None  # or just return

#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    att = dir(hidden_4)
    for name in sorted(att):
        if not name.startswith("__"):
            print(name)

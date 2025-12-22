import os
import sys

def scanner(path: str, depth: int = 0, skip: list[str]=None):
    if skip is None:
        skip=[]

    with os.scandir(path) as entries:
        for entry in entries:

            if entry.name in skip:
                continue

            if entry.is_dir() and entry.name not in (".", ".."):  
                print(" "*depth+entry.name+"/")  
                scanner(os.path.join(path, entry.name), depth+1, skip)
            else:
                print("  "*depth+entry.name) 

def main():
    path = "."
    skip = []

    if len(sys.argv) > 1:
        path = sys.argv[1]

    if len(sys.argv) > 2:
        skip = sys.argv[2].split(",")

    scanner(path, 0, skip)

if __name__ == "__main__":
    main()


                


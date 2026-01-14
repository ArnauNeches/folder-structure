import os
import argparse

def scanner(path: str = ".", depth: int = 0, skip: list[str] = None, indent: bool = False):
    if skip is None:
        skip=[]
 
    indent1 = "     " if indent else "   "

    with os.scandir(path) as entries:
        for entry in entries:

            if entry.name in skip:
                continue

            if entry.is_dir():  
                print(indent1*depth+entry.name+"/")  
                scanner(os.path.join(path, entry.name), depth+1, skip, indent)
            else:
                print(indent1*depth+entry.name) 

def main():

    parser = argparse.ArgumentParser(description="Directory scanner")
    parser.add_argument("path", nargs="?", default=".", help="Path to scan")
    parser.add_argument("--skip", "-s", help="Comma-separated list of files/folders to skip", default="")
    parser.add_argument("-l", help="Longer indentation", action="store_true")

    args = parser.parse_args()
    skip = [s.strip() for s in args.skip.split(",") if s]

    scanner(args.path, 0, skip, args.l)

if __name__ == "__main__":
    main()


                


# A Python program to read the contents of a file similar to cat command in linux.
import sys
def main():
    for arg in sys.argv[1:]:
        with open(arg, "r") as f:
            print(f"\t\t\t'{arg}'")
            data = "".join(f.readlines())
            print(data)    
main()

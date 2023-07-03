import sys
def main():
    args = sys.argv[1:]
    copied_file = args[0]
    data = ""
    with open(args[0], 'rb') as f:
        data = f.read()
    # Writing operations.
    for f in range(1,len(args)):
        with open(args[f],"wb") as file:
            file.write(data)
    print("Completed copying files.") 
main()
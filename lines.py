import sys

def main():
    if argument_count():
        filename = sys.argv[1]
        if check_if_python_file(filename):
            total_lines = count_lines(filename)
            print(total_lines)
            

def argument_count():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()
    else:
        return True

def check_if_python_file(filename):
    if not filename.endswith(".py"):
        print("Not a Python file")
        sys.exit()
    else:
        return True

def count_lines(filename):
    count = 0
    try:
        with open(filename) as file:
            for line in file:
                every_line = line.lstrip()
                if every_line and not every_line.startswith("#"): 
                    # checks if it's a non-empty line that isn't a comment
                    count += 1
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()
    return count



if __name__ == "__main__":
    main()
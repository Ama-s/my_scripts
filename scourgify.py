import sys
import csv

def main():
    if argument_count():
        declutter_file(sys.argv[1], sys.argv[2])

def argument_count():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        return True

    
def declutter_file(before_file, after_file):
    try:
        with open(before_file) as file:
            dict_reader = csv.DictReader(file)

    except FileNotFoundError:
        print("f{Could not read}, before_file")


if __name__ == "__main__":
    main()
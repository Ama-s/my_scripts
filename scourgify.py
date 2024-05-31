import sys
import csv

def main():
    if argument_count():
        before = sys.argv[1]
        after = sys.argv[2]
        declutter_file(before, after) 

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
        file = open(before_file)
        dict_reader = csv.DictReader(file)

        new_file = open(after_file, "w")
        fieldnames = ["first name", "last name", "house"]
        dict_writer = csv.DictWriter(new_file, fieldnames = fieldnames)

        for line in dict_reader:
            full_name = line["name"].strip()
            house = line["house"].strip()

            # Split the full name into last name and first name, and strip each
            last_name, first_name = [part.strip() for part in full_name.split(",")]
            #last_name, first_name = line["name"].split(",").strip()
            #house = line["house"].strip()
            dict_writer.writerow({"first name": first_name, "last name": last_name, "house": house})

        file.close()
        new_file.close()
        
    except FileNotFoundError:
        print(f"Could not read {before_file}")
        sys.exit(1)


if __name__ == "__main__":
    main()
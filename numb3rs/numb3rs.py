import re


def main():
    print(validate(input("IPv4 Address: ")))

def allow_digits(ip):
    first_part, second_part, third_part, forth_part = ip.split(".")
    if (not first_part.isdigit() or not second_part.isdigit() or not third_part.isdigit() or not forth_part.isdigit()):
        return False
    else:
        return True

def validate(ip):
    if allow_digits:
        valid_ip = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
        if valid_ip:
            first_part, second_part, third_part, forth_part = valid_ip.groups()
            if all(0 <= int(part) < 256 for part in [first_part, second_part, third_part, forth_part]):
                return True
            else:
                return False
        else:
            return False


...


if __name__ == "__main__":
    main()
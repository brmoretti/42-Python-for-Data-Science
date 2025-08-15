from sys import argv

if len(argv) == 1:
    exit(0)

try:
    if len(argv) > 2:
        raise AssertionError("more than one argument is provided")
    try:
        number = int(argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    print("I'm " + ("Odd" if number % 2 else "Even") + ".")
except AssertionError as e:
    print(f"AssertionError: {e}")
    exit(1)

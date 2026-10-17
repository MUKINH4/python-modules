from sys import argv

def main():
    print("=== Command Quest ===")
    argc = len(argv)
    i = 1
    print(f"Program name: {argv[0]}")
    if argc < 2:
        print("No arguments provided!")
    else:
        print("Arguments received:", argc - 1)
        while i < argc:
            print(f"Argument {i}: {argv[i]}")
            i += 1
    print("Total arguments:", argc)


if __name__ == "__main__":
    main()
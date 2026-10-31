from sys import argv
import typing


def usage() -> None:
    print("Usage: ft_ancient_text.py <file>")


def open_file(filename: str):
    print(f"Accessing file: '{filename}'")
    try:
        fd: typing.TextIOWrapper = open(filename)
        content = fd.read()
        print("---\n")
        print(content)
        print("\n---")
        fd.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")


def main():
    argc = len(argv)
    if (argc != 2):
        usage()
        return
    print("=== Cyber Archives Recovery ===")
    open_file(argv[1])


if __name__ == "__main__":
    main()

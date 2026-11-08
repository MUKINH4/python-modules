from sys import argv, stdin, stdout, stderr


def usage() -> None:
    print("Usage: ft_stream_management.py <file>")


def read_file(filename: str) -> str | None:
    try:
        print(f"Accessing file'{filename}'")
        file = open(filename, "r")
        content = file.read()
        file.close()
        print("---")
        print(content, end="")
        print("---")
        print(f"File'{filename}'closed.")
        return content
    except OSError as error:
        print(f"[STDERR] Error opening file'{filename}': {error}", file=stderr)
        return None


def transform_data(content: str) -> None:
    lines = content.split("\n")
    transformed_lines = []
    for line in lines:
        if line != "":
            transformed_lines.append(line + "#")
    transformed_content = "\n".join(transformed_lines)
    if content.endswith("\n"):
        transformed_content += "\n"

    print("Transform data:\n---")
    print(transformed_content, end="")
    print("---")
    stdout.write("Enter new file name (or empty): ")
    stdout.flush()
    new_filename = stdin.readline().rstrip("\n")
    if new_filename == "":
        print("Not saving data.")
        return
    print(f"Saving data to'{new_filename}'")
    if save_new_file(new_filename, transformed_content) == 0:
        print("Data not saved.")
        return
    print(f"Data saved in file'{new_filename}'.")


def save_new_file(new_filename: str, content: str) -> int:
    try:
        file = open(new_filename, "w")
        file.write(content)
        file.close()
        return 1
    except OSError as error:
        print(f"[STDERR] Error opening file'{new_filename}':",
              f"{error}", file=stderr)
        return 0


def main() -> None:
    argc = len(argv)
    if argc != 2:
        usage()
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    content = read_file(argv[1])
    if content is not None:
        transform_data(content)


if __name__ == "__main__":
    main()

import sys


def usage():
    print("Usage: ft_archive_creation <file>")


def read_file(filename: str) -> str:
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
        print(f"Error opening file'{filename}': {error}")
        return ""


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
    new_filename = input("Enter new file name (or empty): ")
    if new_filename == "":
        print("Not saving data.")
        return
    print(f"Saving data to'{new_filename}'")
    save_new_file(new_filename, transformed_content)
    print(f"Data saved in file'{new_filename}'.")


def save_new_file(new_filename: str, content: str) -> None:
    file = open(new_filename, "w")
    file.write(content)
    file.close()


def main():
    argc = len(sys.argv)
    if argc != 2:
        usage()
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    content = read_file(sys.argv[1])
    if content is not None:
        transform_data(content)


if __name__ == "__main__":
    main()

def secure_archive(file_name: str, action: str,
                   content: str = "") -> tuple[bool, str]:
    if action == "read":
        try:
            lines: str = ""
            with open(file_name, "r") as file:
                for line in file:
                    lines = lines + line
            return (True, lines)
        except OSError as e:
            return (False, f"{e}")
    elif action == "write" and content != "":
        try:
            with open(file_name, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        except OSError as e:
            return (False, f"{e}")
    else:
        print("Invalid action or empty content!")
    return (False, "Unknown Error")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "read"))
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "write", "testando"))


if __name__ == "__main__":
    main()

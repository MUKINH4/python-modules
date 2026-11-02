import sys
import os
from site import getsitepackages


def is_in_venv() -> bool:
    if sys.prefix != sys.base_prefix:
        return True
    return False


def create_venv_helper():
    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate # On Linux")
    print("lab_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")


def get_env_name(env_name: str) -> str:
    dirs: list[str] = env_name.split(os.sep)
    return dirs[-1]


def get_python_dir(full_directory: str) -> str:
    dirs: list[str] = full_directory.split(os.sep)
    return f"{dirs[-3]}/{dirs[-2]}/{dirs[-1]}"


def main() -> None:
    if not is_in_venv():
        print("\nLABORATORY STATUS: You are working in the open\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: None detected\n")
        print("WARNING: You are in the global environment!",
              "Every reagent you install here leaks into the whole system.\n")
        create_venv_helper()
    else:
        print("\nLABORATORY STATUS: The laboratory is sealed\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {get_env_name(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting the global system.\n")
        print(f"Reagent installation path:\n{getsitepackages()[0]}")


if __name__ == "__main__":
    main()
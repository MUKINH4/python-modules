import importlib.util
import sys


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    required_packages: dict[str, str] = {
        "numpy": "Numerical computation",
        "pandas": "Data manipulation",
    }
    missing: list[str] = []
    print("Checking dependencies:")
    for package, description in required_packages.items():
        check = importlib.util.find_spec(package)
        if check is None:
            missing.append(package)
            print(f"[KO] Missing package: {package}")
        else:
            mod = importlib.import_module(package)
            version = getattr(mod, "__version__", "unknown")
            print(f"[OK] {package} ({version}): {description}-ready")

    if missing:
        packages = " ".join(missing)
        print("\nPlease install missing reagents:")
        print(f"  pip install {packages}")
        print(f"  poetry add {packages}")
        sys.exit(1)
    else:
        print("\npip vs Poetry:\n",
              "requirements.txt declares what to install;"
              "pip resolves it at install time.\n",
              "pyproject.toml declares the same constraints,"
              "and Poetry pins the resolved\n",
              "versions in poetry.lock so every install is identical.\n")
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()

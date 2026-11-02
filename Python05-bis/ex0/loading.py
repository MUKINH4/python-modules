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
            version = getattr(mod, "__version__")
            print(f"[OK] {package} ({version}): {description}-ready")

    if missing:
        print("\nPlease install missing packages before continuing.")
        sys.exit(1)


if __name__ == "__main__":
    main()
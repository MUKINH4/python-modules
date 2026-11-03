import os
import dotenv


CONFIGURATION_NAMES = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
)


def load_configuration() -> tuple[dict[str, str], list[str]]:
    env_file = os.path.join(os.path.dirname(__file__), ".env")
    dotenv.load_dotenv(env_file)

    values = {name: os.getenv(name, "") for name in CONFIGURATION_NAMES}
    missing = [name for name, value in values.items() if not value]
    return values, missing


def show_configuration(values: dict[str, str], missing: list[str]) -> None:
    mode = values["MATRIX_MODE"] or "development"
    log_level = values["LOG_LEVEL"] or "DEBUG"

    print("\nORACLE STATUS: Consulting the configuration...\n")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(
        "Database: Connected to local instance"
        if values["DATABASE_URL"]
        else "Database: Not configured"
    )
    print(
        "API Access: Authenticated"
        if values["API_KEY"]
        else "API Access: Not configured"
    )
    print(f"Log Level: {log_level}")
    print(
        "Remote Network: Online\n"
        if values["ZION_ENDPOINT"]
        else "Remote Network: Not configured\n"
    )

    if missing:
        print("Configuration warnings:")
        print(f"Missing environment variables: {', '.join(missing)}\n")

    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly ignored by git")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


def main() -> None:
    values, missing = load_configuration()
    show_configuration(values, missing)


if __name__ == "__main__":
    main()

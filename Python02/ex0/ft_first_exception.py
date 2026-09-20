def input_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        temp_int = int(temp_str)
        print(f"Temperature is now {temp_int}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")


def test_temperature() -> None:
    input_temperature("25")
    input_temperature("abc")


if __name__ == "__main__":
    test_temperature()
    print("All tests completed - program didn't crash!")

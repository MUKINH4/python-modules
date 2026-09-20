def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    try:
        temp_int = int(temp_str)
        if temp_int > 40:
            raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
        elif temp_int < 0:
            raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature is now {temp_int}°C\n")
            return temp_int
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")
    return 0


def test_temperature() -> None:
    input_temperature("25")
    input_temperature("100")
    input_temperature("-50")
    input_temperature("abc")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")

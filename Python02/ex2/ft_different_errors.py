def garden_operations(operation_number: int):
    print("Testing operation", operation_number)
    try:
        if operation_number == 0:
            int("abc")
        elif operation_number == 1:
            1 / 0
        elif operation_number == 2:
            open("/non/existent/file")
        elif operation_number == 3:
            "oii" + 3
        else:
            return
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    except TypeError as error:
        print("Caught TypeError:", error)


def test_error_types() -> None:
    garden_operations(0)
    garden_operations(1)
    garden_operations(2)
    garden_operations(3)
    garden_operations(4)


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("Operation completed successfully")
    print("\nAll error types tested successfully!")

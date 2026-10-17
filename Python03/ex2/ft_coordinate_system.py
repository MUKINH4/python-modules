from math import sqrt

def calculate_distance(first_coord: tuple[float, float, float],
                       second_coord: tuple[float, float, float]) -> float:
    x1, y1, z1 = first_coord
    x2, y2, z2 = second_coord
    return sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def get_coordinates() -> tuple[float, float, float]:
    while True:
        inp = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = inp.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        coords = []
        valid = True
        for part in parts:
            item = part.strip()
            try:
                coords.append(float(item))
            except ValueError as e:
                print(f"Error on parameter '{item}': {e}")
                valid = False
                break
        if valid:
            return (coords[0], coords[1], coords[2])


def get_player_pos() -> None:
    center_coordinate: tuple[float, float, float] = (0.0, 0.0, 0.0)
    print("Get a first set of coordinates")
    initial_coords = get_coordinates()
    print(f"Got a first tuple: {initial_coords}")
    x, y, z = initial_coords
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print(f"Distance to center: {calculate_distance(initial_coords, center_coordinate):.4f}\n")
    print("Get a second set of coordinates")
    second_coords = get_coordinates()
    print(f"Distance between the 2 sets of coordinates: {calculate_distance(initial_coords, second_coords):.4f}")

if __name__ == "__main==":
    print("=== Game Coordinate System ===\n")
    get_player_pos()

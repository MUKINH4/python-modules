from math import sqrt

def get_player_pos() -> None:
    inp = input("Type the new player coordinates (x,y,z): ").strip().replace(" ", "")
    try:
        initial_cords: tuple[float, float, float] = tuple(float(coord) for coord in inp.split(","))
        print(initial_cords)
        if len(initial_cords) > 3:
            print("Invalid sintax")
            return get_player_pos()
    except ValueError as e:
        print(f"Error on parameter '{e.__traceback__.tb_frame.f_locals}': {e}")

get_player_pos()

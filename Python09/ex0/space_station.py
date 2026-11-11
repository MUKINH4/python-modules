from datetime import datetime
from pydantic import BaseModel, Field


class SpaceStation(BaseModel):
    station_id: str = Field(
        ...,
        min_length=3,
        max_length=10,
        description="station identificator",
    )
    name: str = Field(
        ..., min_length=1, max_length=50, description="name field"
    )
    crew_size: int = Field(
        ..., ge=1, le=20, description="crew size field (1 to 20)"
    )
    power_level: float = Field(
        ..., ge=0.0, le=100.0, description="power level percentage"
    )
    oxygen_level: float = Field(
        ..., ge=0.0, le=100.0, description="oxygen level percentage"
    )
    last_maintence: datetime
    is_operational: bool = True
    notes: str = Field(
        default="", max_length=200, description="notes field"
    )


def main() -> None:
    print("Space Station Date Validation")
    print("========================================")
    print("Valid station created:")
    try:
        spaceS = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintence="2026-10-20T10:00:00",
        )
        print(f"ID: {spaceS.station_id}")
        print(f"Name: {spaceS.name}")
        print(f"Crew: {spaceS.crew_size} people")
        print(f"Power: {spaceS.power_level}%")
        print(f"Oxygen: {spaceS.oxygen_level}%")
        print("status: ", end="")
        if spaceS.is_operational:
            print("Operational\n")
        else:
            print("Offline\n")
        print("========================================")
    except Exception:
        print("Input should be less than or equal to 20")
    print("Expected validation error:")
    try:
        spaceS = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=0,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintence="2026-10-20T10:00:00",
        )
    except Exception:
        print("Input should be less than or equal to 20")


if __name__ == "__main__":
    main()
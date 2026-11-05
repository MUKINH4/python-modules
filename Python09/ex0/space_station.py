from pydantic import BaseModel, Field, field_validator, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(
        ge=0.0,
        le=100.0,
        description="Power level in percentage (0.0 to 100.0)",
    )
    oxygen_level: float = Field(
        ge=0.0,
        le=100.0,
        description="Oxygen level in percentage (0.0 to 100.0)",
    )
    last_maintenance: datetime = Field(
        default_factory=datetime.now,
        description="Timestamp of the last maintenance check",
    )
    is_operational: bool = Field(default=True)
    notes: str | None = Field(
        default=None,
        max_length=200,
        description="Additional notes about the space station",
    )

    @field_validator("station_id")
    @classmethod
    def validate_station_id(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Station ID cannot be empty")
        return value

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Station name cannot be empty")
        return value

    @field_validator("crew_size")
    @classmethod
    def validate_crew_size(cls, value: int) -> int:
        if not 1 <= value <= 20:
            raise ValueError("Crew size must be between 1 and 20")
        return value

    @field_validator("power_level")
    @classmethod
    def validate_power_level(cls, value: float) -> float:
        if not 0.0 <= value <= 100.0:
            raise ValueError("Power level must be between 0.0 and 100.0")
        return value

    @field_validator("oxygen_level")
    @classmethod
    def validate_oxygen_level(cls, value: float) -> float:
        if not 0.0 <= value <= 100.0:
            raise ValueError("Oxygen level must be between 0.0 and 100.0")
        return value

    @field_validator("last_maintenance")
    @classmethod
    def validate_last_maintenance(cls, value: datetime) -> datetime:
        if value > datetime.now():
            raise ValueError("Last maintenance cannot be in the future")
        return value

    @field_validator("is_operational")
    @classmethod
    def validate_is_operational(cls, value: bool) -> bool:
        if not isinstance(value, bool):
            raise ValueError("Operational status must be a boolean")
        return value

    @field_validator("notes")
    @classmethod
    def validate_notes(cls, value: str | None) -> str | None:
        if value is None:
            return value
        value = value.strip()
        if not value:
            raise ValueError("Notes cannot be empty")
        return value

    def output(self) -> None:
        print("=== Space Station Data ===")
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        people_word = "people" if self.crew_size != 1 else "person"
        print(f"Crew Size: {self.crew_size} {people_word}")
        print(f"Power Level: {self.power_level}%")
        print(f"Oxygen Level: {self.oxygen_level}%")
        print(f"Last Maintenance: {self.last_maintenance}")
        operational_status = ""
        if self.is_operational:
            operational_status = "Operational"
        else:
            operational_status = "Not Operational"
        print(f"Operational Status: {operational_status}")
        if self.notes:
            print(f"Notes: {self.notes}")


def main() -> None:
    # Example of creating a SpaceStation instance
    print("Space Station Data Validation")
    print("========================================")
    print("Valid Station Created:")
    station = SpaceStation(
        station_id="ISS-001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now(),
        is_operational=True,
        notes="Routine maintenance completed."
    )
    station.output()

    print("========================================")
    print("Expected Validation Error:")
    try:
        SpaceStation(
            station_id="ISS-001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="Routine maintenance completed.",
        )
    except ValidationError as error:
        print(error.errors()[0]["msg"])


if __name__ == "__main__":
    main()

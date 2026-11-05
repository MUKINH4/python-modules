from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class RankEnum(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: RankEnum
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        leadership_exists = any(
            member.rank in {RankEnum.CAPTAIN, RankEnum.COMMANDER}
            for member in self.crew
        )
        if not leadership_exists:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        experienced_count = sum(
            member.years_experience >= 5 for member in self.crew
        )
        if self.duration_days > 365 and experienced_count * 2 < len(self.crew):
            raise ValueError(
                "Long missions require at least 50% experienced crew"
            )
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank=RankEnum.COMMANDER,
                age=38,
                specialization="Mission Command",
                years_experience=12,
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=RankEnum.LIEUTENANT,
                age=34,
                specialization="Navigation",
                years_experience=7,
            ),
            CrewMember(
                member_id="C003",
                name="Alice Johnson",
                rank=RankEnum.OFFICER,
                age=29,
                specialization="Engineering",
                years_experience=3,
            ),
        ],
    )
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - "
            f"{member.specialization}"
        )

    print("\n=========================================")
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M2024_TEST",
            mission_name="Test Mission",
            destination="Mars",
            duration_days=30,
            budget_millions=100.0,
            crew=[
                CrewMember(
                    member_id="C004",
                    name="Bob Carter",
                    rank=RankEnum.OFFICER,
                    age=31,
                    specialization="Science",
                    years_experience=4,
                )
            ],
        )
    except ValidationError as error:
        message = error.errors()[0]["msg"]
        print(message.removeprefix("Value error, "))


if __name__ == "__main__":
    main()

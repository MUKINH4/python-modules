from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    TELEPATHIC = "telepathic"
    PHYSICAL = "physical"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def verify_contact(self) -> "AlienContact":
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contacts must be verified")
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contacts must have at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must include a received message")
        return self

    def output(self) -> None:
        print(f"ID: {self.contact_id}")
        print(f"Type: {self.contact_type.value}")
        print(f"Location: {self.location}")
        print(f"Signal: {self.signal_strength}/10")
        print(f"Contact Time: {self.timestamp}")
        print(f"Duration: {self.duration_minutes} minutos")
        print(f"Witness: {self.witness_count}")
        if self.message_received:
            print(f"Message Received: {self.message_received}")
        else:
            print("Message Received: None")
        print(f"Is Verified: {'Yes' if self.is_verified else 'No'}")


def main() -> None:
    print("Alien Contact Log Validation")
    print("====================================")
    print("Valid contact report:")
    try:
        contact = AlienContact(
            contact_id="AC_2026_001",
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True,
        )
        contact.output()
    except ValidationError as error:
        print(error.errors()[0]["msg"])

    try:
        print("\nInvalid contact report:")
        contact = AlienContact(
            contact_id="AC_2026_002",
            location="Roswell, New Mexico",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=9.0,
            duration_minutes=30,
            witness_count=2,
            message_received=None,
            is_verified=False,
        )
    except ValidationError as error:
        message = error.errors()[0]["msg"]
        print(message.removeprefix("Value error, "))


if __name__ == "__main__":
    main()

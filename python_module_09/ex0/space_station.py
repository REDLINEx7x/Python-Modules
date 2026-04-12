from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:

    print("Space Station Data Validation")
    print("========================================")
    # Valid sp_station
    sp_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-01-15T10:30:00",  # Pydantic auto-converts!
    )
    print("Valid sp_station created:")
    print(f"ID: {sp_station.station_id}")
    print(f"Crew: {sp_station.crew_size} people")
    print(f"Power: {sp_station.power_level}")
    print(f"Oxygen: {sp_station.oxygen_level}")
    print(f"Status: {'Operational' if sp_station.is_operational else 'Offline'}")
    print()
    print("========================================")

    # Invalid sp_station — triggers ValidationError
    try:
        s = SpaceStation(
            station_id="BAD",
            name="Bad Station",
            crew_size=99,  # Exceeds max of 20
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance="2024-01-15T10:30:00",
        )
    except ValidationError as e:
        print(f"Expected validation error: {e.errors()[0]['msg']}")


if __name__ == "__main__":
    main()

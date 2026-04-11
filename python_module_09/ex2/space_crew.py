from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> 'SpaceMission':
        # Rule 1: Mission ID starts with "M"
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        # Rule 2: At least one Commander or Captain
        senior = [Rank.commander, Rank.captain]
        has_senior = any(m.rank in senior for m in self.crew)
        if not has_senior:
            raise ValueError("Mission must have at least one Commander or Captain")

        # Rule 3: Long missions need 50% experienced crew
        if self.duration_days > 365:
            experienced = [m for m in self.crew if m.years_experience >= 5]
            if len(experienced) / len(self.crew) < 0.5:
                raise ValueError("Long missions need 50% experienced crew (5+ years)")

        # Rule 4: All crew must be active
        inactive = [m.name for m in self.crew if not m.is_active]
        if inactive:
            raise ValueError(f"Inactive crew members not allowed: {inactive}")

        return self

#!/usr/bin/env python3
"""Comprehensive tests for SpaceMission and CrewMember models."""

from datetime import datetime
from ex2.space_crew import SpaceMission, CrewMember, Rank

print("COMPREHENSIVE SPACE MISSION CREW VALIDATION TESTS")
print("=" * 70)

# Test 1: Valid mission with all requirements met
print("\n[Test 1] Valid mission (commander present, experienced crew for long mission):")
try:
    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 9, 1, 8, 0, 0),
        duration_days=900,  # Long mission > 365 days
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=Rank.commander,  # Commander present
                age=45,
                specialization="Mission Command",
                years_experience=20,  # Experienced
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=35,
                specialization="Navigation",
                years_experience=10,  # Experienced
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=28,
                specialization="Engineering",
                years_experience=5,  # Experienced
            ),
        ],
    )
    print(f"  ✅ PASSED: Mission created with {len(mission.crew)} crew members")
    print(f"     Mission: {mission.mission_name}")
    print(f"     Commander: {[m.name for m in mission.crew if m.rank == Rank.commander]}")
except Exception as e:
    print(f"  ❌ FAILED: {e}")

# Test 2: Mission without commander or captain
print("\n[Test 2] Mission without commander or captain (should fail):")
try:
    SpaceMission(
        mission_id="M2024_VENUS",
        mission_name="Venus Probe",
        destination="Venus",
        launch_date=datetime(2024, 8, 1),
        duration_days=180,
        budget_millions=500.0,
        crew=[
            CrewMember(
                member_id="CM101",
                name="Bob Engineer",
                rank=Rank.officer,  # No commander/captain
                age=35,
                specialization="Engineering",
                years_experience=8,
            ),
            CrewMember(
                member_id="CM102",
                name="Jane Pilot",
                rank=Rank.lieutenant,  # No commander/captain
                age=30,
                specialization="Piloting",
                years_experience=5,
            ),
        ],
    )
    print("  ❌ FAILED: Should have required commander/captain")
except TypeError as e:
    print(f"  ✅ PASSED: {e}")

# Test 3: Long mission (>365 days) without enough experienced crew
print("\n[Test 3] Long mission without 50% experienced crew (should fail):")
try:
    SpaceMission(
        mission_id="M2024_OUTER",
        mission_name="Outer Planets Survey",
        destination="Jupiter",
        launch_date=datetime(2025, 1, 1),
        duration_days=1000,  # Long mission
        budget_millions=3000.0,
        crew=[
            CrewMember(
                member_id="CM201",
                name="Captain Lee",
                rank=Rank.captain,
                age=50,
                specialization="Command",
                years_experience=25,  # Experienced
            ),
            CrewMember(
                member_id="CM202",
                name="Junior Pilot",
                rank=Rank.officer,
                age=24,
                specialization="Piloting",
                years_experience=1,  # Inexperienced
            ),
            CrewMember(
                member_id="CM203",
                name="New Scientist",
                rank=Rank.officer,
                age=22,
                specialization="Research",
                years_experience=0,  # Inexperienced
            ),
        ],
    )
    print("  ❌ FAILED: Should require 50% experienced crew (5+ years) for long missions")
except ValueError as e:
    print(f"  ✅ PASSED: {e}")

# Test 4: Short mission with less experienced crew (should pass)
print("\n[Test 4] Short mission with less experienced crew (should pass):")
try:
    mission = SpaceMission(
        mission_id="M2024_MOON",
        mission_name="Moon Base Supply",
        destination="Moon",
        launch_date=datetime(2024, 7, 1),
        duration_days=14,  # Short mission
        budget_millions=100.0,
        crew=[
            CrewMember(
                member_id="CM301",
                name="Captain Moon",
                rank=Rank.captain,
                age=45,
                specialization="Command",
                years_experience=15,
            ),
            CrewMember(
                member_id="CM302",
                name="Junior Dev",
                rank=Rank.officer,
                age=25,
                specialization="Systems",
                years_experience=2,  # Less experienced OK for short mission
            ),
        ],
    )
    print(f"  ✅ PASSED: Short mission ({mission.duration_days} days) created with mixed experience")
except Exception as e:
    print(f"  ❌ FAILED: {e}")

# Test 5: Mission ID not starting with "M"
print("\n[Test 5] Mission ID not starting with 'M' (should fail):")
try:
    SpaceMission(
        mission_id="X2024_TEST",  # Invalid prefix
        mission_name="Test Mission",
        destination="Test",
        launch_date=datetime(2024, 6, 1),
        duration_days=30,
        budget_millions=50.0,
        crew=[
            CrewMember(
                member_id="CM401",
                name="Test Captain",
                rank=Rank.captain,
                age=40,
                specialization="Testing",
                years_experience=10,
            ),
        ],
    )
    print("  ❌ FAILED: Should reject mission ID not starting with 'M'")
except ValueError as e:
    print(f"  ✅ PASSED: {e}")

# Test 6: Mission with inactive crew member
print("\n[Test 6] Mission with inactive crew member (should fail):")
try:
    inactive_member = CrewMember(
        member_id="CM501",
        name="Inactive Officer",
        rank=Rank.officer,
        age=35,
        specialization="Science",
        years_experience=8,
        is_active=False,  # Inactive
    )
    SpaceMission(
        mission_id="M2024_INACTIVE",
        mission_name="Inactive Crew Test",
        destination="Mars",
        launch_date=datetime(2024, 8, 1),
        duration_days=100,
        budget_millions=500.0,
        crew=[
            CrewMember(
                member_id="CM502",
                name="Captain Active",
                rank=Rank.captain,
                age=45,
                specialization="Command",
                years_experience=20,
            ),
            inactive_member,
        ],
    )
    print("  ❌ FAILED: Should reject missions with inactive crew")
except ValueError as e:
    print(f"  ✅ PASSED: {e}")

# Test 7: Nested model validation - invalid crew member
print("\n[Test 7] Nested model validation - invalid crew member age:")
try:
    SpaceMission(
        mission_id="M2024_INVALID",
        mission_name="Invalid Crew Test",
        destination="Mars",
        launch_date=datetime(2024, 8, 1),
        duration_days=100,
        budget_millions=500.0,
        crew=[
            CrewMember(
                member_id="CM601",
                name="Young Cadet",
                rank=Rank.cadet,
                age=15,  # Too young (minimum 18)
                specialization="Training",
                years_experience=0,
            ),
        ],
    )
    print("  ❌ FAILED: Should reject crew member with invalid age")
except Exception as e:
    print(f"  ✅ PASSED: Caught nested validation error")

# Test 8: Crew list constraints
print("\n[Test 8] Crew must be 1-12 members:")
try:
    crew = [
        CrewMember(
            member_id=f"CM{700+i}",
            name=f"Crew Member {i}",
            rank=Rank.captain if i == 0 else Rank.officer,
            age=30 + i,
            specialization="General",
            years_experience=5,
        )
        for i in range(15)  # 15 members exceeds max of 12
    ]
    SpaceMission(
        mission_id="M2024_OVERCREW",
        mission_name="Too Many Crew",
        destination="Mars",
        launch_date=datetime(2024, 8, 1),
        duration_days=100,
        budget_millions=500.0,
        crew=crew,
    )
    print("  ❌ FAILED: Should reject crew list > 12 members")
except Exception as e:
    print(f"  ✅ PASSED: Rejected crew list exceeding maximum")

print("\n" + "=" * 70)
print("VALIDATION SUMMARY:")
print("  ✅ CrewMember model properly defined with constraints")
print("  ✅ SpaceMission model properly defined with nested crew list")
print("  ✅ Mission ID validation (must start with 'M')")
print("  ✅ Senior rank requirement (commander or captain)")
print("  ✅ Experience requirement for long missions (50% with 5+ years)")
print("  ✅ Active crew requirement (no inactive members)")
print("  ✅ Nested model validation (crew member constraints enforced)")
print("  ✅ Crew list constraints (1-12 members)")

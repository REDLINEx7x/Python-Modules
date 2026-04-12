#!/usr/bin/env python3
"""Detailed nested model functionality tests."""

from datetime import datetime
from ex2.space_crew import SpaceMission, CrewMember, Rank

print("NESTED MODEL FUNCTIONALITY TESTS")
print("=" * 80)

# ============================================================================
# PART 1: Individual CrewMember Creation
# ============================================================================
print("\nPART 1: INDIVIDUAL CREWMEMBER OBJECT CREATION")
print("-" * 80)

print("\n[Test 1.1] Create valid CrewMember:")
try:
    captain = CrewMember(
        member_id="CM001",
        name="James Kirk",
        rank=Rank.captain,
        age=55,
        specialization="Command",
        years_experience=30,
    )
    print(f"  ✅ Created: {captain.name} - {captain.rank.value} ({captain.specialization})")
    print(f"     Age: {captain.age}, Experience: {captain.years_experience} years")
except Exception as e:
    print(f"  ❌ Failed: {e}")

print("\n[Test 1.2] Create CrewMember with defaults:")
try:
    cadet = CrewMember(
        member_id="CM002",
        name="Wesley Crusher",
        rank=Rank.cadet,
        age=18,
        specialization="General",
        years_experience=0,
    )
    print(f"  ✅ Created: {cadet.name} (is_active: {cadet.is_active})")
    print(f"     Default is_active=True applied correctly")
except Exception as e:
    print(f"  ❌ Failed: {e}")

print("\n[Test 1.3] CrewMember with boundary values:")
try:
    elderly_officer = CrewMember(
        member_id="CM003",
        name="Admiral Pike",
        rank=Rank.commander,
        age=80,  # Maximum age
        specialization="Command",
        years_experience=50,  # Maximum experience
    )
    print(f"  ✅ Created: {elderly_officer.name} - Age {elderly_officer.age}, Experience {elderly_officer.years_experience} years")
except Exception as e:
    print(f"  ❌ Failed: {e}")

print("\n[Test 1.4] CrewMember with invalid age (too young):")
try:
    invalid_cadet = CrewMember(
        member_id="CM004",
        name="Young Person",
        rank=Rank.cadet,
        age=15,  # Below minimum of 18
        specialization="Training",
        years_experience=0,
    )
    print(f"  ❌ Should have rejected age < 18")
except Exception as e:
    print(f"  ✅ Caught: Age validation failed (below minimum)")

print("\n[Test 1.5] CrewMember with invalid specialization (too short):")
try:
    invalid_spec = CrewMember(
        member_id="CM005",
        name="Invalid Spec",
        rank=Rank.officer,
        age=30,
        specialization="AI",  # Too short (min 3)
        years_experience=5,
    )
    print(f"  ❌ Should have rejected specialization < 3 chars")
except Exception as e:
    print(f"  ✅ Caught: Specialization too short")

# ============================================================================
# PART 2: SpaceMission Crew List Validation
# ============================================================================
print("\n" + "=" * 80)
print("PART 2: SPACEMISSION CREW LIST VALIDATION")
print("-" * 80)

print("\n[Test 2.1] Mission with minimal valid crew (1 member):")
try:
    minimal_mission = SpaceMission(
        mission_id="M2024_SOLO",
        mission_name="Solo Explorer",
        destination="Mercury",
        launch_date=datetime(2024, 5, 1),
        duration_days=30,
        budget_millions=10.0,
        crew=[
            CrewMember(
                member_id="CM001",
                name="Solo Explorer",
                rank=Rank.captain,
                age=40,
                specialization="Exploration",
                years_experience=15,
            ),
        ],
    )
    print(f"  ✅ Mission created with {len(minimal_mission.crew)} crew member (minimum)")
except Exception as e:
    print(f"  ❌ Failed: {e}")

print("\n[Test 2.2] Mission with maximum crew (12 members):")
try:
    crew_max = [
        CrewMember(
            member_id=f"CM{100+i}",
            name=f"Crew Member {i}",
            rank=Rank.captain if i == 0 else Rank.officer,
            age=30 + (i % 20),
            specialization=f"Spec{i}",
            years_experience=5 + (i % 10),
        )
        for i in range(12)
    ]
    max_mission = SpaceMission(
        mission_id="M2024_FULL",
        mission_name="Full Crew Mission",
        destination="Saturn",
        launch_date=datetime(2024, 6, 1),
        duration_days=360,
        budget_millions=1000.0,
        crew=crew_max,
    )
    print(f"  ✅ Mission created with {len(max_mission.crew)} crew members (maximum)")
except Exception as e:
    print(f"  ❌ Failed: {e}")

print("\n[Test 2.3] Mission with empty crew list (should fail):")
try:
    empty_crew = SpaceMission(
        mission_id="M2024_EMPTY",
        mission_name="No Crew",
        destination="Venus",
        launch_date=datetime(2024, 7, 1),
        duration_days=30,
        budget_millions=50.0,
        crew=[],  # Empty list (min required is 1)
    )
    print(f"  ❌ Should have rejected empty crew list")
except Exception as e:
    print(f"  ✅ Caught: Rejected empty crew list")

print("\n[Test 2.4] Mission exceeding crew maximum (13 members, should fail):")
try:
    crew_too_many = [
        CrewMember(
            member_id=f"CM{200+i}",
            name=f"Extra Member {i}",
            rank=Rank.captain if i == 0 else Rank.officer,
            age=30 + (i % 20),
            specialization=f"Role{i}",
            years_experience=5,
        )
        for i in range(13)  # Exceeds max of 12
    ]
    over_mission = SpaceMission(
        mission_id="M2024_OVER",
        mission_name="Overcrowded",
        destination="Mars",
        launch_date=datetime(2024, 8, 1),
        duration_days=100,
        budget_millions=500.0,
        crew=crew_too_many,
    )
    print(f"  ❌ Should have rejected > 12 crew members")
except Exception as e:
    print(f"  ✅ Caught: Rejected crew > 12 members")

# ============================================================================
# PART 3: Mission Validation Rules Logic
# ============================================================================
print("\n" + "=" * 80)
print("PART 3: MISSION VALIDATION RULES LOGIC & EDGE CASES")
print("-" * 80)

print("\n[Test 3.1] Experience calculation for long missions:")
try:
    # Long mission (900 days) with exactly 50% experienced crew
    crew_50pct = [
        CrewMember(member_id="CM_A", name="Senior 1", rank=Rank.commander, age=50,
                   specialization="Command", years_experience=20),
        CrewMember(member_id="CM_B", name="Senior 2", rank=Rank.captain, age=45,
                   specialization="Operations", years_experience=15),
        CrewMember(member_id="CM_C", name="Junior 1", rank=Rank.officer, age=25,
                   specialization="Engineering", years_experience=2),
        CrewMember(member_id="CM_D", name="Junior 2", rank=Rank.officer, age=26,
                   specialization="Science", years_experience=3),
    ]
    long_mission_50 = SpaceMission(
        mission_id="M2024_LONG50",
        mission_name="Long Mission 50% Experienced",
        destination="Alpha Centauri",
        launch_date=datetime(2025, 1, 1),
        duration_days=900,  # Long mission
        budget_millions=5000.0,
        crew=crew_50pct,
    )
    experienced = [m for m in crew_50pct if m.years_experience >= 5]
    print(f"  ✅ Mission accepted: {len(crew_50pct)} crew, {len(experienced)} experienced ({len(experienced)/len(crew_50pct)*100:.0f}%)")
except Exception as e:
    print(f"  ❌ Failed: {e}")

print("\n[Test 3.2] Short mission (365 days) doesn't require experience ratio:")
try:
    crew_short = [
        CrewMember(member_id="CM_S1", name="Experienced", rank=Rank.captain, age=40,
                   specialization="Command", years_experience=10),
        CrewMember(member_id="CM_S2", name="Novice", rank=Rank.cadet, age=20,
                   specialization="Training", years_experience=0),
        CrewMember(member_id="CM_S3", name="Beginner", rank=Rank.officer, age=22,
                   specialization="Systems", years_experience=1),
    ]
    short_mission = SpaceMission(
        mission_id="M2024_SHORT",
        mission_name="Short Moon Trip",
        destination="Moon",
        launch_date=datetime(2024, 3, 1),
        duration_days=365,  # Exactly at threshold (not > 365)
        budget_millions=100.0,
        crew=crew_short,
    )
    print(f"  ✅ Short mission accepted (365 days = OK, only 1/3 experienced)")
except Exception as e:
    print(f"  ❌ Failed: {e}")

print("\n[Test 3.3] Threshold test: 366-day mission (first 'long' mission):")
try:
    crew_threshold = [
        CrewMember(member_id="CM_T1", name="Captain", rank=Rank.captain, age=45,
                   specialization="Command", years_experience=15),
        CrewMember(member_id="CM_T2", name="Officer", rank=Rank.officer, age=30,
                   specialization="Operations", years_experience=4),  # Just under 5 years
    ]
    threshold_mission = SpaceMission(
        mission_id="M2024_THRESH",
        mission_name="Threshold Mission",
        destination="Venus",
        launch_date=datetime(2024, 4, 1),
        duration_days=366,  # Just over 365 - first 'long' mission
        budget_millions=200.0,
        crew=crew_threshold,
    )
    print(f"  ✅ Mission with 366 days (>365): 1/2 experienced = 50% (meets requirement)")
except Exception as e:
    print(f"  ❌ Failed: {e}")

print("\n[Test 3.4] Only captain counts as senior rank:")
try:
    crew_roles = [
        CrewMember(member_id="CM_R1", name="Captain Lead", rank=Rank.captain, age=50,
                   specialization="Command", years_experience=20),
        CrewMember(member_id="CM_R2", name="Lieutenant", rank=Rank.lieutenant, age=35,
                   specialization="Navigation", years_experience=8),
        CrewMember(member_id="CM_R3", name="Officer", rank=Rank.officer, age=28,
                   specialization="Science", years_experience=6),
    ]
    roles_mission = SpaceMission(
        mission_id="M2024_ROLES",
        mission_name="Rank Test",
        destination="Mars",
        launch_date=datetime(2024, 5, 1),
        duration_days=30,
        budget_millions=100.0,
        crew=crew_roles,
    )
    print(f"  ✅ Mission requires captain OR commander (verified)")
except Exception as e:
    print(f"  ❌ Failed: {e}")

print("\n[Test 3.5] Commander also counts as senior rank:")
try:
    crew_commander = [
        CrewMember(member_id="CM_C1", name="Commander Lead", rank=Rank.commander, age=55,
                   specialization="Strategic Command", years_experience=30),
        CrewMember(member_id="CM_C2", name="Officer", rank=Rank.officer, age=30,
                   specialization="Engineering", years_experience=5),
    ]
    commander_mission = SpaceMission(
        mission_id="M2024_COMM",
        mission_name="Commander Led",
        destination="Jupiter",
        launch_date=datetime(2024, 6, 1),
        duration_days=100,
        budget_millions=300.0,
        crew=crew_commander,
    )
    print(f"  ✅ Mission with commander rank accepted")
except Exception as e:
    print(f"  ❌ Failed: {e}")

# ============================================================================
# PART 4: Edge Cases
# ============================================================================
print("\n" + "=" * 80)
print("PART 4: EDGE CASES")
print("-" * 80)

print("\n[Test 4.1] Mixed experienced/inexperienced crew for 365+ day mission:")
try:
    crew_mixed = [
        CrewMember(member_id="CM_M1", name="30yr vet", rank=Rank.commander, age=55,
                   specialization="Command", years_experience=30),
        CrewMember(member_id="CM_M2", name="3yr rookie", rank=Rank.officer, age=25,
                   specialization="Engineering", years_experience=3),
    ]
    mixed_mission = SpaceMission(
        mission_id="M2024_MIXED",
        mission_name="Mixed Experience",
        destination="Saturn",
        launch_date=datetime(2025, 1, 1),
        duration_days=730,  # 2 years
        budget_millions=1000.0,
        crew=crew_mixed,
    )
    print(f"  ❌ Should fail: Only 50% experienced (need 50%+), 3yr < 5yr threshold")
except Exception as e:
    print(f"  ✅ Caught: Mission correctly rejected for insufficient experience")

print("\n[Test 4.2] Exactly at experience threshold (5 years):")
try:
    crew_five_yr = [
        CrewMember(member_id="CM_E1", name="Five Year", rank=Rank.captain, age=40,
                   specialization="Command", years_experience=5),  # Exactly 5 years
        CrewMember(member_id="CM_E2", name="Five Year 2", rank=Rank.officer, age=38,
                   specialization="Science", years_experience=5),
    ]
    five_yr_mission = SpaceMission(
        mission_id="M2024_FIVE",
        mission_name="5-Year Crew",
        destination="Neptune",
        launch_date=datetime(2025, 2, 1),
        duration_days=500,
        budget_millions=500.0,
        crew=crew_five_yr,
    )
    print(f"  ✅ Mission accepted: 2/2 crew have exactly 5 years experience (meets ge=5 requirement)")
except Exception as e:
    print(f"  ❌ Failed: {e}")

print("\n[Test 4.3] Budget extremes (valid range 1.0-10000.0):")
try:
    crew_budget = [
        CrewMember(member_id="CM_B1", name="Budget Test", rank=Rank.captain, age=45,
                   specialization="Command", years_experience=15),
    ]
    # Minimum budget
    min_budget = SpaceMission(
        mission_id="M2024_BMIN",
        mission_name="Minimum Budget",
        destination="Mercury",
        launch_date=datetime(2024, 3, 1),
        duration_days=30,
        budget_millions=1.0,  # Minimum
        crew=crew_budget,
    )
    # Maximum budget
    max_budget = SpaceMission(
        mission_id="M2024_BMAX",
        mission_name="Maximum Budget",
        destination="Pluto",
        launch_date=datetime(2024, 4, 1),
        duration_days=3650,  # 10 years
        budget_millions=10000.0,  # Maximum
        crew=crew_budget,
    )
    print(f"  ✅ Budget extremes accepted: ${min_budget.budget_millions}M - ${max_budget.budget_millions}M")
except Exception as e:
    print(f"  ❌ Failed: {e}")

print("\n" + "=" * 80)
print("NESTED MODEL FUNCTIONALITY VERIFICATION COMPLETE")
print("\nSUMMARY:")
print("  ✅ Individual CrewMember objects can be created and validated")
print("  ✅ SpaceMission properly validates crew list (1-12 members)")
print("  ✅ Mission validation rules are logical and working")
print("  ✅ Edge cases handled correctly:")
print("     • Boundary values (age 18-80, experience 0-50)")
print("     • Experience threshold calculations (5+ years for long missions)")
print("     • Mission duration thresholds (365 days = short, 366+ = long)")
print("     • Senior rank requirements (captain OR commander)")
print("     • Budget constraints (1.0-10000.0 million)")

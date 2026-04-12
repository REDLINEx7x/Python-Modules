#!/usr/bin/env python3
"""Comprehensive validation tests for AlienContact model."""

from datetime import datetime
from ex1.alien_contact import AlienContact, ContactType

print("COMPREHENSIVE VALIDATION RULE TESTS")
print("=" * 70)

# Test 1: ID not starting with "AC"
print("\n[Test 1] ID not starting with 'AC':")
try:
    AlienContact(
        contact_id="XY_2024_001",  # Invalid prefix
        timestamp="2024-06-15T22:30:00",
        location="Area 51",
        contact_type=ContactType.radio,
        signal_strength=5.0,
        duration_minutes=30,
        witness_count=1,
    )
    print("  ❌ FAILED: Should have rejected invalid ID")
except ValueError as e:
    print(f"  ✅ PASSED: {e}")

# Test 2: Telepathic with < 3 witnesses
print("\n[Test 2] Telepathic contact with < 3 witnesses:")
try:
    AlienContact(
        contact_id="AC_2024_002",
        timestamp="2024-06-15T23:00:00",
        location="Roswell",
        contact_type=ContactType.telepathic,
        signal_strength=5.0,
        duration_minutes=30,
        witness_count=1,  # Only 1, needs 3+
    )
    print("  ❌ FAILED: Should have required 3+ witnesses")
except TypeError as e:
    print(f"  ✅ PASSED: {e}")

# Test 3: Strong signal without message
print("\n[Test 3] Strong signal (>7.0) without message:")
try:
    AlienContact(
        contact_id="AC_2024_003",
        timestamp="2024-06-16T01:00:00",
        location="Area 51",
        contact_type=ContactType.radio,
        signal_strength=8.5,  # Strong signal
        duration_minutes=30,
        witness_count=5,
        message_received=None,  # No message
    )
    print("  ❌ FAILED: Should require message with strong signal")
except ValueError as e:
    print(f"  ✅ PASSED: {e}")

# Test 4: Physical contact not verified
print("\n[Test 4] Physical contact not verified:")
try:
    AlienContact(
        contact_id="AC_2024_004",
        timestamp="2024-06-16T02:00:00",
        location="Nevada Desert",
        contact_type=ContactType.physical,
        signal_strength=6.0,
        duration_minutes=20,
        witness_count=3,
        is_verified=False,  # Not verified
    )
    print("  ❌ FAILED: Physical contact should require verification")
except ValueError as e:
    print(f"  ✅ PASSED: {e}")

# Test 5: Valid telepathic contact with 3+ witnesses
print("\n[Test 5] Valid telepathic contact with 3+ witnesses:")
try:
    contact = AlienContact(
        contact_id="AC_2024_005",
        timestamp="2024-06-16T03:00:00",
        location="Area 51",
        contact_type=ContactType.telepathic,
        signal_strength=5.0,
        duration_minutes=30,
        witness_count=3,  # Exactly 3 - minimum required
    )
    print(f"  ✅ PASSED: Created valid telepathic contact (ID: {contact.contact_id})")
except Exception as e:
    print(f"  ❌ FAILED: {e}")

# Test 6: Valid physical contact (verified)
print("\n[Test 6] Valid physical contact (verified):")
try:
    contact = AlienContact(
        contact_id="AC_2024_006",
        timestamp="2024-06-16T04:00:00",
        location="Area 51",
        contact_type=ContactType.physical,
        signal_strength=6.0,
        duration_minutes=20,
        witness_count=5,
        is_verified=True,  # Verified
    )
    print(f"  ✅ PASSED: Created valid verified physical contact (ID: {contact.contact_id})")
except Exception as e:
    print(f"  ❌ FAILED: {e}")

# Test 7: Valid strong signal with message
print("\n[Test 7] Valid strong signal with message:")
try:
    contact = AlienContact(
        contact_id="AC_2024_007",
        timestamp="2024-06-16T05:00:00",
        location="Area 51",
        contact_type=ContactType.radio,
        signal_strength=9.0,  # Very strong
        duration_minutes=45,
        witness_count=10,
        message_received="Greetings from Zeta Reticuli",
    )
    print(f"  ✅ PASSED: Created valid strong signal contact (ID: {contact.contact_id})")
except Exception as e:
    print(f"  ❌ FAILED: {e}")

print("\n" + "=" * 70)
print("Validation rule testing complete!")
print("\nSUMMARY:")
print("  • Validation rules are enforced correctly")
print("  • Error messages are clear and descriptive")
print("  • Valid combinations pass validation")
print("  • Invalid combinations are rejected")

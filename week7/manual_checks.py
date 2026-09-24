from datetime import date, datetime

from smartcare_v04_final import (Appointment, AppointmentStatus, Patient,
                           Practitioner, ValidationError)


def check(number, description, condition, detail=""):
    line = f"{number:>2}. {description}: {'PASS' if condition else 'FAIL'}"
    if detail:
        line += f" | {detail}"
    print(line)


print("SmartCare v0.4 - manual behaviour checks")
print("-" * 70)

alice = Patient("P001", "Alice Smith", date(1990, 4, 12), "0400 000 000")
dr_doe = Practitioner("PR01", "Dr John Doe", "General Practice")
slot = datetime(2026, 10, 6, 9, 0)
appt = Appointment("A001", alice, dr_doe, slot)

check(1, "Create patient (FR-01)",
      str(alice) == "Alice Smith (P001)", str(alice))

check(2, "Create practitioner (FR-04)",
      dr_doe.specialty == "General Practice", str(dr_doe))

check(3, "Book appointment (FR-05, FR-08)",
      appt.status is AppointmentStatus.BOOKED, str(appt))

try:
    Patient("P002", "   ", date(1985, 1, 1), "0400 111 111")
    check(4, "Blank name rejected (FR-07)", False)
except ValidationError as error:
    check(4, "Blank name rejected (FR-07)", True, str(error))

try:
    Appointment("A002", alice, dr_doe, "next Tuesday")
    check(5, "Non date and time rejected (FR-07)", False)
except ValidationError as error:
    check(5, "Non date and time rejected (FR-07)", True, str(error))

try:
    Appointment("A003", "Alice Smith", dr_doe, slot)
    check(6, "Patient name string rejected in place of a Patient (FR-07)", False)
except ValidationError as error:
    check(6, "Patient name string rejected in place of a Patient (FR-07)",
          True, str(error))

check(7, "Practitioner reports slot as taken (FR-06)",
      dr_doe.is_busy(slot) is True, "09:00 on 06/10/2026")

check(8, "A different slot is free (FR-06)",
      dr_doe.is_busy(datetime(2026, 10, 6, 10, 0)) is False,
      "10:00 on 06/10/2026")

appt.cancel()

check(9, "Cancelled slot is free (FR-09)",
      dr_doe.is_busy(slot) is False, "09:00 on 06/10/2026")

check(10, "Record is kept, not deleted, after cancellation (FR-09, FR-11)",
      appt in alice.history(),
      f"history holds {len(alice.history())} record(s), status {appt.status}")

bob = Patient("P003", "Bob Nguyen", date(1978, 11, 3), "0400 333 333")
rebooked = Appointment("A004", bob, dr_doe, slot)

check(11, "Freed slot can be rebooked (FR-05, FR-06)",
      rebooked.status is AppointmentStatus.BOOKED, str(rebooked))

print("-" * 70)
print("All checks complete.")

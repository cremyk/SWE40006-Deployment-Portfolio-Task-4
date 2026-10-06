import sys
import socket
import datetime

# Student Metadata
STUDENT_NAME = "Hoo Ying Kit"
STUDENT_ID = "105190469"

# Pre-populated Doctors Database
DOCTORS = [
    {"id": 1, "name": "Dr. Sarah Jenkins", "specialty": "Cardiology", "room": "Room 301"},
    {"id": 2, "name": "Dr. Marcus Vance", "specialty": "Pediatrics", "room": "Room 105"},
    {"id": 3, "name": "Dr. Elena Rostova", "specialty": "General Medicine", "room": "Room 204"},
    {"id": 4, "name": "Dr. Kevin Tan", "specialty": "Dermatology", "room": "Room 412"},
]

# In-memory Appointment Store
appointments = []

def get_container_id():
    return socket.gethostname()

def print_header():
    print("\n" + "=" * 65)
    print("      MEDICARE CLINICAL APPOINTMENT SYSTEM (CLI)")
    print("      SWE40006 Software Deployment - Task 4.4 (HD Level)")
    print("=" * 65)
    print(f" Developer: {STUDENT_NAME} | Student ID: {STUDENT_ID}")
    print("=" * 65)

def list_doctors():
    print("\n--- AVAILABLE CLINICAL SPECIALISTS ---")
    print(f"{'ID':<4} {'Doctor Name':<24} {'Specialty':<20} {'Location':<10}")
    print("-" * 62)
    for doc in DOCTORS:
        print(f"{doc['id']:<4} {doc['name']:<24} {doc['specialty']:<20} {doc['room']:<10}")
    print("-" * 62)

def book_appointment():
    list_doctors()
    try:
        doc_id = int(input("\nEnter Doctor ID to book with: ").strip())
        selected_doc = next((d for d in DOCTORS if d["id"] == doc_id), None)
        if not selected_doc:
            print("[ERROR] Invalid Doctor ID selected.")
            return

        patient_name = input("Enter Patient Full Name: ").strip()
        if not patient_name:
            print("[ERROR] Patient name cannot be blank.")
            return

        date_str = input("Enter Preferred Date (YYYY-MM-DD): ").strip()
        time_slot = input("Enter Time Slot (e.g. 10:00 AM, 02:30 PM): ").strip()

        appt_id = len(appointments) + 101
        booking = {
            "appt_id": appt_id,
            "patient": patient_name,
            "doctor": selected_doc["name"],
            "specialty": selected_doc["specialty"],
            "room": selected_doc["room"],
            "date": date_str,
            "time": time_slot,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        appointments.append(booking)
        print(f"\n[SUCCESS] Appointment confirmed! Booking Reference: #{appt_id}")

    except ValueError:
        print("[ERROR] Please enter a valid numerical Doctor ID.")

def view_appointments():
    print("\n--- CONFIRMED PATIENT APPOINTMENTS ---")
    if not appointments:
        print("No appointments have been scheduled yet.")
        return

    print(f"{'Ref #':<8} {'Patient':<18} {'Doctor':<22} {'Date':<12} {'Time':<10}")
    print("-" * 72)
    for appt in appointments:
        print(f"#{appt['appt_id']:<7} {appt['patient']:<18} {appt['doctor']:<22} {appt['date']:<12} {appt['time']:<10}")
    print("-" * 72)

def cancel_appointment():
    global appointments  # Placed at the very top of function to fix SyntaxError
    view_appointments()
    if not appointments:
        return

    try:
        ref_id = int(input("\nEnter Appointment Reference # to cancel: ").strip())
        initial_len = len(appointments)
        appointments = [a for a in appointments if a["appt_id"] != ref_id]

        if len(appointments) < initial_len:
            print(f"[SUCCESS] Appointment #{ref_id} has been successfully canceled.")
        else:
            print(f"[ERROR] Appointment #{ref_id} not found.")
    except ValueError:
        print("[ERROR] Please enter a valid numerical Reference #.")

def main_menu():
    while True:
        print_header()
        print(" [1] Browse Available Doctors")
        print(" [2] Book New Appointment")
        print(" [3] View Scheduled Appointments")
        print(" [4] Cancel Existing Appointment")
        print(" [5] Exit System")
        print("-" * 65)

        choice = input("Enter your selection (1-5): ").strip()

        if choice == "1":
            list_doctors()
            input("\nPress Enter to return to main menu...")
        elif choice == "2":
            book_appointment()
            input("\nPress Enter to return to main menu...")
        elif choice == "3":
            view_appointments()
            input("\nPress Enter to return to main menu...")
        elif choice == "4":
            cancel_appointment()
            input("\nPress Enter to return to main menu...")
        elif choice == "5":
            print(f"\nExiting Medicare Hospital System. Goodbye!\n")
            sys.exit(0)
        else:
            print("[ERROR] Invalid menu choice. Please select 1 through 5.")

if __name__ == "__main__":
    main_menu()
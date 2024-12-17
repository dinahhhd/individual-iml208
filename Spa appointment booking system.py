import tkinter as tk
from tkinter import messagebox
import re

# Store appointments in a list
data = []

def is_valid_date(date_str):
    # Simple regex for DD-MM-YYYY format
    return bool(re.match(r"^\d{2}-\d{2}-\d{4}$", date_str))

def is_valid_time(time_str):
    # Simple regex for 24-hour time format HH:MM
    return bool(re.match(r"^\d{2}:\d{2}$", time_str))

def create_appointment():
    # Collect personal information
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    age = entry_age.get()
    dob = entry_dob.get()
    street_address = entry_street_address.get()
    street_address_line_2 = entry_street_address_line_2.get()
    city = entry_city.get()
    state_province = entry_state_province.get()
    postal_code = entry_postal_code.get()
    phone_number = entry_phone_number.get()
    date_of_appointment = entry_date_of_appointment.get()
    time_of_appointment = entry_time_of_appointment.get()

    # Validate date and time
    if not is_valid_date(date_of_appointment):
        messagebox.showwarning("Invalid Date", "Please enter a valid date in the format DD-MM-YYYY.")
        return

    if not is_valid_time(time_of_appointment):
        messagebox.showwarning("Invalid Time", "Please enter a valid time in the format HH:MM.")
        return

    # Display packages and allow selection
    package_choice = package_var.get()
    if package_choice == "4":
        custom_package = entry_custom_package.get()
    else:
        custom_package = ""

    # Store appointment
    appointment = {
        "First Name": first_name,
        "Last Name": last_name,
        "Age": age,
        "Date of Birth": dob,
        "Street Address": street_address,
        "Street Address Line 2": street_address_line_2,
        "City": city,
        "State/Province": state_province,
        "Postal Code": postal_code,
        "Phone Number": phone_number,
        "Date of Appointment": date_of_appointment,
        "Time of Appointment": time_of_appointment,
        "Package": package_choice,
        "Custom Package": custom_package
    }
    data.append(appointment)
    refresh_list()
    messagebox.showinfo("Success", "Appointment created successfully!")

def update_appointment():
    # Ensure an appointment is selected in the listbox
    selected_index = listbox_appointments.curselection()
    if not selected_index:
        messagebox.showwarning("Warning", "Please select an appointment to update.")
        return

    index = selected_index[0]

    # Validate input fields (date and time validation included)
    if not is_valid_date(entry_date_of_appointment.get()):
        messagebox.showwarning("Invalid Date", "Please enter a valid date in the format DD-MM-YYYY.")
        return

    if not is_valid_time(entry_time_of_appointment.get()):
        messagebox.showwarning("Invalid Time", "Please enter a valid time in the format HH:MM.")
        return

    # Update the selected appointment with the current form data
    data[index] = {
        "First Name": entry_first_name.get(),
        "Last Name": entry_last_name.get(),
        "Age": entry_age.get(),
        "Date of Birth": entry_dob.get(),
        "Street Address": entry_street_address.get(),
        "Street Address Line 2": entry_street_address_line_2.get(),
        "City": entry_city.get(),
        "State/Province": entry_state_province.get(),
        "Postal Code": entry_postal_code.get(),
        "Phone Number": entry_phone_number.get(),
        "Date of Appointment": entry_date_of_appointment.get(),
        "Time of Appointment": entry_time_of_appointment.get(),
        "Package": package_var.get(),
        "Custom Package": entry_custom_package.get() if package_var.get() == "4" else ""
    }

    # Refresh the listbox to show updated details
    refresh_list()

    # Notify the user of the successful update
    messagebox.showinfo("Success", "Appointment updated successfully!")

def delete_appointment():
    selected_index = listbox_appointments.curselection()
    if not selected_index:
        messagebox.showwarning("Warning", "Please select an appointment to delete.")
        return

    index = selected_index[0]
    del data[index]
    refresh_list()
    messagebox.showinfo("Success", "Appointment deleted successfully!")

def read_appointment():
    if not data:
        messagebox.showinfo("No Appointments", "No appointments found.")
        return

    # Create a string that includes all the appointment details
    appointment_details = ""
    for appointment in data:
        appointment_details += f"Name: {appointment['First Name']} {appointment['Last Name']}\n"
        appointment_details += f"Age: {appointment['Age']}\n"
        appointment_details += f"Date of Birth: {appointment['Date of Birth']}\n"
        appointment_details += f"Street Address: {appointment['Street Address']}\n"
        appointment_details += f"Street Address Line 2: {appointment['Street Address Line 2']}\n"
        appointment_details += f"City: {appointment['City']}\n"
        appointment_details += f"State/Province: {appointment['State/Province']}\n"
        appointment_details += f"Postal Code: {appointment['Postal Code']}\n"
        appointment_details += f"Phone Number: {appointment['Phone Number']}\n"
        appointment_details += f"Date of Appointment: {appointment['Date of Appointment']}\n"
        appointment_details += f"Time of Appointment: {appointment['Time of Appointment']}\n"
        appointment_details += f"Package: {appointment['Package']}\n"
        if appointment['Custom Package']:
            appointment_details += f"Custom Package: {appointment['Custom Package']}\n"
        appointment_details += "-" * 40 + "\n"

    # Display all the appointment details in a messagebox
    messagebox.showinfo("Appointments", appointment_details)

def refresh_list():
    # Refresh the appointment list display
    listbox_appointments.delete(0, tk.END)
    for i, appointment in enumerate(data, start=1):
        listbox_appointments.insert(tk.END, f"{i}. {appointment['First Name']} {appointment['Last Name']} ({appointment['Package']})")

def load_appointment(event):
    selected_index = listbox_appointments.curselection()
    if not selected_index:
        return

    index = selected_index[0]
    appointment = data[index]

    # Populate form fields with the selected appointment data
    entry_first_name.delete(0, tk.END)
    entry_first_name.insert(0, appointment["First Name"])

    entry_last_name.delete(0, tk.END)
    entry_last_name.insert(0, appointment["Last Name"])

    entry_age.delete(0, tk.END)
    entry_age.insert(0, appointment["Age"])

    entry_dob.delete(0, tk.END)
    entry_dob.insert(0, appointment["Date of Birth"])

    entry_street_address.delete(0, tk.END)
    entry_street_address.insert(0, appointment["Street Address"])

    entry_street_address_line_2.delete(0, tk.END)
    entry_street_address_line_2.insert(0, appointment["Street Address Line 2"])

    entry_city.delete(0, tk.END)
    entry_city.insert(0, appointment["City"])

    entry_state_province.delete(0, tk.END)
    entry_state_province.insert(0, appointment["State/Province"])

    entry_postal_code.delete(0, tk.END)
    entry_postal_code.insert(0, appointment["Postal Code"])

    entry_phone_number.delete(0, tk.END)
    entry_phone_number.insert(0, appointment["Phone Number"])

    entry_date_of_appointment.delete(0, tk.END)
    entry_date_of_appointment.insert(0, appointment["Date of Appointment"])

    entry_time_of_appointment.delete(0, tk.END)
    entry_time_of_appointment.insert(0, appointment["Time of Appointment"])

    package_var.set(appointment["Package"])
    entry_custom_package.delete(0, tk.END)
    entry_custom_package.insert(0, appointment["Custom Package"])

def setup_form():
    root = tk.Tk()
    root.title("Spa Appointment System")

    frame_form = tk.Frame(root)
    frame_form.pack(padx=20, pady=20)

    # Personal Information
    tk.Label(frame_form, text="First Name:").grid(row=0, column=0, sticky=tk.W)
    global entry_first_name
    entry_first_name = tk.Entry(frame_form)
    entry_first_name.grid(row=0, column=1)

    tk.Label(frame_form, text="Last Name:").grid(row=1, column=0, sticky=tk.W)
    global entry_last_name
    entry_last_name = tk.Entry(frame_form)
    entry_last_name.grid(row=1, column=1)
    
    tk.Label(frame_form, text="Age:").grid(row=2, column=0, sticky=tk.W)
    global entry_age
    entry_age = tk.Entry(frame_form)
    entry_age.grid(row=2, column=1)

    tk.Label(frame_form, text="Date of Birth (DD-MM-YY):").grid(row=3, column=0, sticky=tk.W)
    global entry_dob
    entry_dob = tk.Entry(frame_form)
    entry_dob.grid(row=3, column=1)

    tk.Label(frame_form, text="Street Address:").grid(row=4, column=0, sticky=tk.W)
    global entry_street_address
    entry_street_address = tk.Entry(frame_form)
    entry_street_address.grid(row=4, column=1)

    tk.Label(frame_form, text="Street Address Line 2:").grid(row=5, column=0, sticky=tk.W)
    global entry_street_address_line_2
    entry_street_address_line_2 = tk.Entry(frame_form)
    entry_street_address_line_2.grid(row=5, column=1)

    tk.Label(frame_form, text="City:").grid(row=6, column=0, sticky=tk.W)
    global entry_city
    entry_city = tk.Entry(frame_form)
    entry_city.grid(row=6, column=1)

    tk.Label(frame_form, text="State/Province:").grid(row=7, column=0, sticky=tk.W)
    global entry_state_province
    entry_state_province = tk.Entry(frame_form)
    entry_state_province.grid(row=7, column=1)

    tk.Label(frame_form, text="Postal Code:").grid(row=8, column=0, sticky=tk.W)
    global entry_postal_code
    entry_postal_code = tk.Entry(frame_form)
    entry_postal_code.grid(row=8, column=1)

    tk.Label(frame_form, text="Phone Number:").grid(row=9, column=0, sticky=tk.W)
    global entry_phone_number
    entry_phone_number = tk.Entry(frame_form)
    entry_phone_number.grid(row=9, column=1)

    # Date of Appointment and Time of Appointment Entry Fields
    tk.Label(frame_form, text="Date of Appointment (DD-MM-YYYY):").grid(row=10, column=0, sticky=tk.W)
    global entry_date_of_appointment
    entry_date_of_appointment = tk.Entry(frame_form)
    entry_date_of_appointment.grid(row=10, column=1)

    tk.Label(frame_form, text="Time of Appointment (HH:MM):").grid(row=11, column=0, sticky=tk.W)
    global entry_time_of_appointment
    entry_time_of_appointment = tk.Entry(frame_form)
    entry_time_of_appointment.grid(row=11, column=1)

    # Package Selection
    tk.Label(frame_form, text="Package:").grid(row=12, column=0, sticky=tk.W)
    global package_var
    package_var = tk.StringVar()
    tk.Radiobutton(frame_form, text="1: Full body massage + Facial treatment + Hot tub", variable=package_var, value="1").grid(row=13, column=0, sticky=tk.W)
    tk.Radiobutton(frame_form, text="2: Full body massage + Manicure + Pedicure", variable=package_var, value="2").grid(row=14, column=0, sticky=tk.W)
    tk.Radiobutton(frame_form, text="3: Back massage + Hair treatment", variable=package_var, value="3").grid(row=15, column=0, sticky=tk.W)
    tk.Radiobutton(frame_form, text="4: Custom Package", variable=package_var, value="4").grid(row=16, column=0, sticky=tk.W)

    global entry_custom_package
    entry_custom_package = tk.Entry(frame_form)
    entry_custom_package.grid(row=16, column=1)

    # Buttons
    tk.Button(frame_form, text="Create Appointment", command=create_appointment).grid(row=17, column=0, pady=10)
    tk.Button(frame_form, text="Update Appointment", command=update_appointment).grid(row=17, column=1, pady=10)
    tk.Button(frame_form, text="Delete Appointment", command=delete_appointment).grid(row=18, column=0, pady=10)
    tk.Button(frame_form, text="Read Appointment", command=read_appointment).grid(row=18, column=1, pady=10)

    # Listbox for Appointments
    global listbox_appointments
    listbox_appointments = tk.Listbox(root, height=10, width=80)
    listbox_appointments.pack(pady=20)
    listbox_appointments.bind("<<ListboxSelect>>", load_appointment)

    root.mainloop()

setup_form()
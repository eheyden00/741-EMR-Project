#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime
from tkinter import *
from tkinter import ttk
from record import Record
from user import Admin
from professional import Professional
from management import Management


class Window:

    # Writes a line to the usage log csv
    def write_usage_log(self, line):
        with open('./usage_log.csv', 'a') as f:
            f.write('\n'+self.username.get()+','+self.role+','+str(self.login_time)+','+line)

    
    # Called when a login attempt is made. Checks credentials
    def login(self):
        self.login_time = datetime.now()
        self.role = None        
        for i, row in self.credentials.iterrows():
            # If credentials match, get role
            if row['username'] == self.username.get() and row['password'] == self.password.get():
                self.role = row['role']
                break

        if not self.role:
            self.login_message.set('Username or password is incorrect')
            self.role = "N/A"
            self.write_usage_log('Failed login attempt')
        else: 
            self.write_usage_log('Successful login')
            self.main_window()

    # Creates frame for count_visits
    def count_visits(self):
        self.frm2.destroy()
        self.frm2 = ttk.Frame(self.root, padding=10)
        self.frm2.grid(column=0, row=1)
        self.date = StringVar()
        self.date_string = StringVar()
        ttk.Label(self.frm2, text='Enter date to check total visits').grid(column=0, row=0)
        ttk.Entry(self.frm2, textvariable=self.date).grid(column=1, row=0)
        ttk.Button(self.frm2, text="Submit", command=self.submit_date).grid(column=2, row=0)
        ttk.Label(self.frm2, textvar=self.date_string).grid(column=0, row=1)

    # Called when count_visits is submitted
    def submit_date(self):
        visits = self.user.count_visits(self.date.get())
        self.date_string.set('On '+self.date.get()+' there were '+str(visits)+' total visits.')
        self.write_usage_log('Count_visits')

    # Called when Remove_patient is submitted
    def submit_remove_id(self):
        patient_id = self.patient_id.get()
        patient = self.user.records.get_patient(patient_id)
        if not patient: ttk.Label(self.frm2, text='Alert: Patient ID not found in records').grid(column=0, row=1)
        else:
            self.user.remove_patient(patient_id)
            ttk.Label(self.frm2, text='Patient removed from records').grid(column=0, row=1)
            self.write_usage_log('Remove_patient')

    # Called when View_note is submitted
    def submit_view_note(self):
        patient_id = self.patient_id.get()
        patient = self.user.records.get_patient(patient_id)
        if not patient: ttk.Label(self.frm2, text='Alert: Patient ID not found in records').grid(column=0, row=2)
        else:
            note_text = self.user.view_note(patient, self.date.get())
            if not note_text:
                ttk.Label(self.frm2, text='Alert: Patient has no records on this date').grid(column=0, row=2)
            else:
                textbox = Text(self.frm2, wrap="word", height=10, width=80)
                textbox.grid(row=2, column=0, columnspan=2)
                scrollbar = Scrollbar(self.frm2, orient="vertical", command=textbox.yview)
                textbox.config(yscrollcommand=scrollbar.set)
                scrollbar.grid(row=2, column=2, sticky="ns")
                textbox.insert(END, note_text)
                textbox.config(state=DISABLED)
                self.write_usage_log('View_note')

    # Called when Retrieve_patient is submitted
    def submit_retrieve_patient(self):
        patient_id = self.patient_id.get()
        patient = self.user.records.get_patient(patient_id)
        if not patient: ttk.Label(self.frm2, text='Alert: Patient ID not found in records').grid(column=0, row=2)
        else:
            note_text = self.user.retrieve_patient(patient)
            textbox = Text(self.frm2, wrap="word", height=10, width=80)
            textbox.grid(row=2, column=0, columnspan=2)
            scrollbar = Scrollbar(self.frm2, orient="vertical", command=textbox.yview)
            textbox.config(yscrollcommand=scrollbar.set)
            scrollbar.grid(row=2, column=2, sticky="ns")
            textbox.insert(END, note_text)
            textbox.config(state=DISABLED)
            self.write_usage_log('Retrieve_patient')

    # Called when Add_patient is submitted
    def submit_add_patient(self):
        patient = self.user.records.get_patient(self.patient_id.get())
        newdata = []
        newdata.append(self.patient_id.get())
        newdata.append(self.date.get())
        newdata.append(self.department.get())
        newdata.append(self.race.get())
        newdata.append(self.gender.get())
        newdata.append(self.ethnicity.get())
        newdata.append(self.age.get())
        newdata.append(self.zip.get())
        newdata.append(self.insurance.get())
        newdata.append(self.complaint.get())
        newdata.append(self.note_type.get())
        newdata.append(self.note.get())
        self.user.add_patient(patient, newdata)
        self.write_usage_log('Add_patient')

        if not patient:
            self.add_patient_text.set('Added new patient info to records')
        else:
            self.add_patient_text.set('Added new visit info to existing patient in records')

        
        
    # Called when Generate_key_statistics is pressed
    def generate_key_statistics(self):
        self.user.create_plots()
        self.frm2.destroy()
        self.frm2 = ttk.Frame(self.root, padding=10)
        self.frm2.grid(column=0, row=1)
        ttk.Label(self.frm2, text='Visit trend plots saved to this directory. Plots are by gender, race, ethnicity, and overall visits.').grid(column=0, row=0)
        self.write_usage_log('Generate_key_statistics')

    # Creates frame for add_patient
    def add_patient(self):
        self.frm2.destroy()
        self.frm2 = ttk.Frame(self.root, padding=10)
        self.frm2.grid(column=0, row=1)

        self.patient_id = StringVar()
        self.date = StringVar()
        self.department = StringVar()
        self.race = StringVar()
        self.gender = StringVar()
        self.ethnicity = StringVar()
        self.age = StringVar()
        self.zip = StringVar()
        self.insurance = StringVar()
        self.complaint = StringVar()
        self.note_type = StringVar()
        self.note = StringVar()
        
        ttk.Label(self.frm2, text='Patient ID').grid(column=0, row=0)
        ttk.Entry(self.frm2, textvariable=self.patient_id).grid(column=0, row=1)
        ttk.Label(self.frm2, text='Visit Date').grid(column=1, row=0)
        ttk.Entry(self.frm2, textvariable=self.date).grid(column=1, row=1)
        ttk.Label(self.frm2, text='Department').grid(column=2, row=0)
        departments = ['Cardiology','Emergency department','Head and Neck','Neorology',
                       'Obstetrics and gynaecology','Pediatrics','Psychiatry','Radiology','Surgery']
        ttk.Combobox(self.frm2, textvariable=self.department, values=departments, state='readonly').grid(column=2, row=1)
        ttk.Label(self.frm2, text='Race').grid(column=3, row=0)
        races = ['Asian','Black','Native Americans','Pacific Islanders','White','Unknown']
        ttk.Combobox(self.frm2, textvariable=self.race, values=races, state='readonly').grid(column=3, row=1)
        ttk.Label(self.frm2, text='Gender').grid(column=4, row=0)
        genders=['Female','Male','Non-binary']
        ttk.Combobox(self.frm2, textvariable=self.gender, values=genders, state='readonly').grid(column=4, row=1)
        ttk.Label(self.frm2, text='Ethnicity').grid(column=5, row=0)
        ethnicities=['Hispanic','Non-Hispanic','Other','Unknown']
        ttk.Combobox(self.frm2, textvariable=self.ethnicity, values=ethnicities, state='readonly').grid(column=5, row=1)
        ttk.Label(self.frm2, text='Age').grid(column=0, row=2)
        ttk.Entry(self.frm2, textvariable=self.age).grid(column=0, row=3)
        ttk.Label(self.frm2, text='ZIP code').grid(column=1, row=2)
        ttk.Entry(self.frm2, textvariable=self.zip).grid(column=1, row=3)
        ttk.Label(self.frm2, text='Insurance').grid(column=2, row=2)
        insurances = ['Blueshield','Medicaid','Medicare','Not Available','Unknown']
        ttk.Combobox(self.frm2, textvariable=self.insurance, values=insurances, state='readonly').grid(column=2, row=3)
        ttk.Label(self.frm2, text='Chief complaint').grid(column=3, row=2)
        ttk.Entry(self.frm2, textvariable=self.complaint).grid(column=3, row=3)
        ttk.Label(self.frm2, text='Note type').grid(column=4, row=2)
        note_types = ['admission note','discharge note','oncology note',
                      'progress note','social work note']
        ttk.Combobox(self.frm2, textvariable=self.note_type, values=note_types, state='readonly').grid(column=4, row=3)
        ttk.Label(self.frm2, text='Note').grid(column=5, row=2)
        ttk.Entry(self.frm2, textvariable=self.note).grid(column=5, row=3)
        
        ttk.Button(self.frm2, text="Submit", command=self.submit_add_patient).grid(column=0, row=4)

        self.add_patient_text = StringVar()
        ttk.Label(self.frm2, textvar=self.add_patient_text).grid(column=1, row=4)


    # Creates frame for remove_patient
    def remove_patient(self):
        self.frm2.destroy()
        self.frm2 = ttk.Frame(self.root, padding=10)
        self.frm2.grid(column=0, row=1)
        self.patient_id = StringVar()
        ttk.Label(self.frm2, text='Enter Patient ID to remove').grid(column=0, row=0)
        ttk.Entry(self.frm2, textvariable=self.patient_id).grid(column=1, row=0)
        ttk.Button(self.frm2, text="Submit", command=self.submit_remove_id).grid(column=2, row=0)


    # Creates frame for retrieve_patient
    def retrieve_patient(self):
        self.frm2.destroy()
        self.frm2 = ttk.Frame(self.root, padding=10)
        self.frm2.grid(column=0, row=1)
        self.patient_id = StringVar()
        ttk.Label(self.frm2, text='Enter Patient ID').grid(column=0, row=0)
        ttk.Entry(self.frm2, textvariable=self.patient_id).grid(column=1, row=0)
        ttk.Button(self.frm2, text="Submit", command=self.submit_retrieve_patient).grid(column=2, row=0)


    # Creates frame for View_note
    def view_note(self):
        self.frm2.destroy()
        self.frm2 = ttk.Frame(self.root, padding=10)
        self.frm2.grid(column=0, row=1)
        self.patient_id = StringVar()
        self.date = StringVar()
        ttk.Label(self.frm2, text='Enter Patient ID').grid(column=0, row=0)
        ttk.Entry(self.frm2, textvariable=self.patient_id).grid(column=1, row=0)
        ttk.Label(self.frm2, text='Enter date').grid(column=0, row=1)
        ttk.Entry(self.frm2, textvariable=self.date).grid(column=1, row=1)
        ttk.Button(self.frm2, text="Submit", command=self.submit_view_note).grid(column=2, row=0)

    # Creates main window after successful login
    def main_window(self):
        self.frm.destroy()
        self.root.title(self.role + ' interface')
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm2 = ttk.Frame(self.root, padding=10)
        self.frm.grid(column=0, row=0)
        # Reads the data and note files
        df = pd.read_csv('./PA3_data.csv', dtype = str)
        notes_df = pd.read_csv('./PA3_Notes.csv', dtype = str, index_col = 0)
        
        # Parses patient data into Record, Patient, and Visit objects
        records = Record(df, notes_df)
    
        # User is of type 'Professional'
        if self.role == 'nurse' or self.role == 'clinician':
            self.user = Professional(records)
            ttk.Button(self.frm, text="Add_patient", command=self.add_patient).grid(column=0, row=1)
            ttk.Button(self.frm, text="Remove_patient", command=self.remove_patient).grid(column=1, row=1)
            ttk.Button(self.frm, text="Retrieve_patient", command=self.retrieve_patient).grid(column=2, row=1)
            ttk.Button(self.frm, text="Count_visits", command=self.count_visits).grid(column=3, row=1)
            ttk.Button(self.frm, text="View_note", command=self.view_note).grid(column=4, row=1)
    
        # User is of type 'Admin'
        elif self.role == 'admin':
            self.user = Admin(records)
            ttk.Button(self.frm, text="Count_visits", command=self.count_visits).grid(column=0, row=1)

            
    
        # User is of type 'Management'
        else:
            self.user = Management(records)
            ttk.Button(self.frm, text="Generate_key_statistics", command=self.generate_key_statistics).grid(column=0, row=1)
    

        
        ttk.Button(self.frm, text="Exit", command=self.root.destroy).grid(column=0, row=0)


    # Creates initial login window
    def __init__(self, root):
        self.credentials = pd.read_csv('./PA3_credentials.csv', index_col = 0)

        self.root = root
        self.root.title('Staff Portal')
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        ttk.Label(self.frm, text="Staff Login").grid(column=1, row=0)
        ttk.Label(self.frm, text="Username").grid(column=0, row=1)

        self.username = StringVar()
        username_entry = ttk.Entry(self.frm, textvariable=self.username)
        username_entry.grid(column=1, row=1)

        ttk.Label(self.frm, text="Password").grid(column=0, row=2)
        self.password = StringVar()
        ttk.Entry(self.frm, textvariable=self.password).grid(column=1, row=2)
        
        ttk.Button(self.frm, text="Exit", command=self.root.destroy).grid(column=0, row=3)
        ttk.Button(self.frm, text="Log In", command=self.login).grid(column=1, row=3)

        self.login_message = StringVar()
        ttk.Label(self.frm, textvariable=self.login_message).grid(column=1, row=4)
        
        username_entry.focus()


# Creates usage_log.csv if it doesn't already exist
try:
    with open('./usage_log.csv', 'x') as f:
        f.write('Username,Role,Login_time,Action')
except FileExistsError:
    pass
    
root = Tk()
Window(root)
root.mainloop()


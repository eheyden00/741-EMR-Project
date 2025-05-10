#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from patient import Patient

# Record contains Patients, which contain Visits
class Record:

    # Takes dataframe from input file as input
    def __init__(self, df, notes_df):

        # Stores the data df and notes df
        self.df = df
        self.notes_df = notes_df
        
        # List of Patients contained in this Record
        self.patients = []

        # Iterates through rows in the dataframe
        for i, row in df.iterrows():
            # Adds the patient into the records
            self.add_patient(row)


    
    # Returns a Patient object with the corresponding patient ID
    def get_patient(self, Patient_ID):
        for patient in self.patients:
            if patient.ID == Patient_ID:
                return patient

        # If there is no Patient with the ID in Record, return None
        return None

    # Takes a pandas row of new visit information and adds it to the records
    def add_patient(self, row):
        # Need to check if the patient ID already exists
            # Check if self.patients has a Patient object with the ID
            patient = self.get_patient(row['Patient_ID'])

            # If patient doesn't already exist, create a new Patient object and add it to patients
            if patient == None:
                self.patients.append(Patient(row))

            # If patient does already exist, add a new Visit to the Patient object
            else: patient.add_visit(row)


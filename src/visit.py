#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Visit objects are contained in Patients, which are contained in a Record
class Visit:
    
    # Creates a new Visit object with the data in the given row
    def __init__(self, row):
        self.ID = row['Visit_ID']
        self.time = row['Visit_time']
        self.department = row['Visit_department']
        self.race = row['Race']
        self.gender = row['Gender']
        self.ethnicity = row['Ethnicity']
        self.age = row['Age']
        self.zip = row['Zip_code']
        self.insurance = row['Insurance']
        self.complaint = row['Chief_complaint']
        self.note_ID = row['Note_ID']
        self.note_type = row['Note_type']


    # Defines how the visit info is displayed when the visit object is printed
    def __str__(self):
        return ('\nVisit ID: ' + self.ID +
                '\nVisit date: ' + self.time +
                '\nVisit department: ' + self.department +
                '\nPatient race: ' + self.race +
                '\nPatient gender: ' + self.gender +
                '\nPatient ethnicity: ' + self.ethnicity +
                '\nPatient age: ' + self.age +
                '\nPatient ZIP code: ' + self.zip +
                '\nPatient insurance: ' + self.insurance +
                '\nChief complaint: ' + self.complaint +
                '\nNote ID: ' + self.note_ID +
                '\nNote type: ' + self.note_type)


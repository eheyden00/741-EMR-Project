#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from user import User
import pandas as pd
import random

# This type of user is for clinicians and nurses. They are able to perform several actions
class Professional(User):
    

    # This function is called during the 'Add_patient' action
    # Gets a randomly generated visit ID and note ID that are not already used for the patient
    def get_unique_ids(self, patient):
        visit_id = str(random.randint(1, 999999))
        note_id = str(random.randint(1, 999999))
    
        # If patient is already in records, check for conflicts
        if patient != None:
    
            # Gets visit IDs and note IDs already in use for the patient
            existing_visit_ids = []
            existing_note_ids = []
            for visit in patient.visits:
                existing_visit_ids.append(visit.ID)
                existing_note_ids.append(visit.note_ID)
    
            # Re-generates new IDs until they are unique for the patient
            while visit_id in existing_visit_ids:
                visit_id = str(random.randint(1, 999999))
            while note_id in existing_note_ids:
                note_id = str(random.randint(1, 999999))
                
        return visit_id, note_id


   
    def add_patient(self, patient, newdata):

        visit_id, note_id = self.get_unique_ids(patient)
        newdata.insert(1, visit_id)
        newdata.insert(11, note_id)

        # Gets the data needed for the notes csv
        newdata_note = [newdata[i] for i in [0,1,11,13]]

        # Removes the note text from the list for the data csv
        newdata.pop()
        
        # Creates rows to be added to the data and notes df's
        row_df = pd.DataFrame([newdata], columns=self.records.df.columns)
        row_notes_df = pd.DataFrame([newdata_note], columns=self.records.notes_df.columns)
        
        # Adds the new patient info to records
        self.records.add_patient(row_df.squeeze())
        
        # Appends the new row to the end of the data and notes df's
        self.records.df.loc[self.records.df.index.max() + 1] = newdata
        self.records.notes_df.loc[self.records.notes_df.index.max() + 1] = newdata_note
        
        # Overwrites the input files with the new data
        self.records.df.to_csv('./PA3_data.csv', index = False)
        self.records.notes_df.to_csv('./PA3_Notes.csv')

    
    def remove_patient(self, patient_id):
        # Removes all rows from the df's where the patient's ID is present
        self.records.df = self.records.df[self.records.df['Patient_ID'] != patient_id]
        self.records.notes_df = self.records.notes_df[self.records.notes_df['Patient_ID'] != patient_id]

        # Corrects the index of the notes df
        self.records.notes_df = self.records.notes_df.reset_index(drop = True)

        # Overwrites the input files with the patient's data removed
        self.records.df.to_csv('./PA3_data.csv', index = False)
        self.records.notes_df.to_csv('./PA3_Notes.csv')

        # Removes the patient object from records
        self.records.patients.remove(self.records.get_patient(patient_id))

    
    def retrieve_patient(self, patient):
        note_text = ''
        for visit in patient.visits:
            note_text = note_text + str(visit) + '\n'
        return note_text

    
    def view_note(self, patient, date):
        visit_list = []
        for visit in patient.visits:
            if visit.time == date: visit_list.append(visit)

         # For each visit on the date, prints the visit ID, note ID, note type, and note text
        note_text = ''
        for visit in visit_list:
            # Gets the note text for the visit
            df = self.records.notes_df.loc[self.records.notes_df['Visit_ID'] == visit.ID]
            note_text += '\n\nVisit ID: ' + visit.ID
            note_text += '\nNote ID: ' + visit.note_ID
            note_text += '\nNote type: ' + visit.note_type
            note_text += '\nNote: ' + df.iloc[0]['Note_text']
        return note_text


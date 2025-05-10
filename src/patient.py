#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from visit import Visit

# Patient contains Visits and is contained in Record
class Patient:

    # Takes a dataframe row as input
    def __init__(self, row):

        # Stores the patient's ID
        self.ID = row['Patient_ID']

        # List of Visit objects for this patient
        self.visits = []

        # Adds the first Visit for this Patient with the row data
        self.add_visit(row)

    # Creates new Visit object for this patient with the given row data
    def add_visit(self, row):
        self.visits.append(Visit(row))

    # Gets the visit object with the given visit ID
    def get_visit(self, visit_id):
        for visit in self.visits:
            if visit.ID == visit_id: return visit
        return None


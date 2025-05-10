#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# User has subclasses Admin, Management, and Professional
# Management and Professional are in separate files
class User:


    def __init__(self, records):
        # Stores records for easy access
        self.records = records

    # Counts the total number of visits on a given date
    def count_visits(self, date):
        # Counter for total number of visits at given date
        num_visits = 0
        # Iterates through all visits for all patients
        for patient in self.records.patients:
            for visit in patient.visits:

                # Increment num_visits if the visit date matches
                if visit.time == date:
                    num_visits += 1

        # Prints the results to the terminal
        return num_visits


# This type of user is only able to count visits
class Admin(User):
    pass


# 741-EMR-Project
By: Evan Heyden

Toy model of an electronic medical record system

Description:
This program implements a simple electronic medical record system for a fictional hospital through a GUI. This was created as an exercise, and should not be used to store any real, sensitive information.

After a user logs in, the available functionality depends on the role of the user. Nurses and clinicians have access to most of the functionality, including adding, removing, and viewing patient records. Administrators are only able to count the total number of visits to the hospital on a given date. Managers are only able to generate time plots of visits per year for various demographic groups.



Running the program:
This program was written using the standard libraries in Python 3.12.7 . For the exact environment used, see requirements.txt .

The program should be launched from the terminal by navigating to its directory and running "python main.py" without quotes. The directory must contain all of the .py files provided in this project, as well as the provided files "PA3_credentials.csv", "PA3_data.csv", and "PA3_Notes.csv".

IMPORTANT NOTES: All dates entered into the program should be in the format yyyy-mm-dd
Failure to follow this format may result in failure to retrieve relevant information, and may result in a crash when management generates key statistics.
Also, when adding new records, care should be taken that all information is filled in before pressing submit.



CSV information:
"PA3_credentials.csv" contains the usernames and passwords of all authorized users, as well as each user's respective role ('nurse', 'clinician', 'admin', or 'management').

"PA3_data.csv" is a dataframe where each row corresponds to a unique visit by a patient. This file contains all of the information about a patient's visit EXCEPT for the note associated with the visit, which is contained in "PA3_Notes.csv". Both of these files are updated whenever a patient's records are added or removed.

"usage_log.csv" is created by the program and updated during use. Each time an action is performed in the program, including all login attempts, the type of action is logged along with the user's username, role, and date and time of login.

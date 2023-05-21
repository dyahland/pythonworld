# README PROJECT PYTHON FUNDAMENTAL
## by Dyah Witamara

This program is a CRUD (Create, Read, Update, Delete) program for patient data at the "Rumah Sakit Pasti Sembuh" using a nested list format. The choice of nested lists is suitable for the table display feature called "tabulate" used to show the patient data.

There are 8 sub-data in this program: JKN number, patient name, age, gender, illness, department, room number, and status. As the name suggests, this program executes the Create, Read, Update, and Delete functions.

1. Create function: Initially, the program contains data for 3 patients that have been added previously, which can be displayed using the "tabulate" table and "format grid" function for a neater presentation. Additionally, the program allows for adding new patient data, which will be verified to check if the data already exists or not.

2. Read function: All scripts and functions are interconnected so that when one function is called, it includes other functions as well.

3. Update function: In the update function, the patient data to be updated is inputted based on the JKN number. Then, the JKN number is cross-checked to verify if the patient data exists in the system. The update function includes various verifications, such as ensuring that all columns (including the JKN number) contain valid values (e.g., numeric values), otherwise, an error will occur. The functions used for verification include "isalpha," "isalnum," and "isdigit."

4. Delete function: This function allows for the deletion of patient data based on the patient number. First, the patient number to be deleted is searched to determine if it exists in the system. If it exists, all data related to that patient (JKN number to status) will be deleted.

5. Search function: In addition to the CRUD functions, this program also includes a search function. The search function allows for searching data based on the input of the JKN number and patient name. When the program is executed, only the data of the searched patient will be displayed.

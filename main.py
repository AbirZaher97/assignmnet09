# ---------------------------------------------------------- #
# Title: TestHarness
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Abir Zaher, 3.15.2022, Modified code for Assignment 09
# ---------------------------------------------------------- #

# Import Classes

if __name__ == "__main__":
    import ProcessingClasses as P
    from DataClasses import Employee as Emp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# global variables
lstTableEmp = []
strChoice = ""

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee object
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTableEmp.clear()
for line in lstFileData:
    lstTableEmp.append(Emp(line[0], line[1], line[2].strip()))

# display menu to user
while True:
    Eio.print_menu_items()
    str_Choice = Eio.input_menu_options()
    # display current data to user
    if str_Choice == "1":
        Eio.print_current_list_items(lstTableEmp)
    # user can add data to the list
    elif str_Choice == "2":
        lstTableEmp.append(Eio.input_employee_data())
    # save data to file
    elif str_Choice == "3":
        P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTableEmp)
        print("Data Saved to file!")
    # exit program
    elif str_Choice == "4":
        break

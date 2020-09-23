import os
import json
from datetime import datetime

clear = lambda: os.system("cls")


def watermark():
    clear()

    print("STELLARSOL COLLECTOR")
    print("--------------------")
    print()


# Data-entry menu.
def dataMenu():
    watermark()

    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")

    obj = input("Name of Object: ")
    ra = input("Current Right-Ascension: ")
    dec = input("Current Declination: ")

    watermark()

    print("Is this information correct? Y/N")
    print()
    print("Object Name: ", obj)
    print("Current Date: ", date)
    print("RA/Dec: ", ra + " / " + dec)
    print()

    while True:
        choice = input()

        if choice == "Y":
            # Open "data.json" and read it's contents.
            with open("data.json", "r") as json_file:
                json_data = json.load(json_file)
            
            # Append the new data entry to the relevant object.
            json_data[obj].append({"date": date, "ra": ra, "dec": dec})

            # Write the new data with pretty-printing.
            with open("data.json", "w") as json_file:
                json.dump(json_data, json_file, indent=4)
            
            json_file.close()

            clear()
            print("Data written to file.")
            break
        elif choice == "N":
            dataMenu()
            break
        else:
            continue


# Function for viewing collected data for a specific object.
def dataViewer():
    watermark()

    option_dict = {
        "1": "Alpha Centari-A",
        "2": "Alpha Centari-B",
        "3": "Alpha Centari-C",
        "4": "Bernard's Star",
        "5": "Luhman 16",
        "6": "WISE 0855-0714",
        "7": "Wolf 359"
    }

    print("Select an object to view it's collected data.")
    print()
    print("1 - ", option_dict["1"])
    print("2 - ", option_dict["2"])
    print("3 - ", option_dict["3"])
    print("4 - ", option_dict["4"])
    print("5 - ", option_dict["5"])
    print("6 - ", option_dict["6"])
    print("7 - ", option_dict["7"])
    print()

    choice = input()

    # Selected-object the user wishes to view.
    selected_obj = option_dict[choice]

    with open("data.json", "r") as json_file:
        file_contents = json_file.read()
    
    obj_data = json.loads(file_contents)

    json_file.close()

    # data.json is read and the user's object has it's number of indexes counted.
    # If the object has no collected data, exit.
    def indexPrompt():
        watermark()

        if len(obj_data[selected_obj]) == 0:
            watermark()

            print("Object has no collected data.")
            print("Read 'stellarsol.txt' for more information about this.")
            exit()
        else:
            print(selected_obj + " has", str(len(obj_data[selected_obj])) + " entries.")
            print()
        
    indexPrompt()
        
    # The user is prompted to select an entry to view until a valid entry is selected.
    # Relevant data for the entry selected is spit out into the terminal.
    while True:
        entry_selection = input("Select an entry to view: ")

        if int(entry_selection) <= len(obj_data[selected_obj]):
            watermark()

            print("Positional-data for", selected_obj + " on "
            + obj_data[selected_obj][int(entry_selection) - 1]["date"])

            print()

            print("RA/Dec: ", obj_data[selected_obj][int(entry_selection) - 1]["ra"]
            + " / " + obj_data[selected_obj][int(entry_selection) - 1]["dec"])
            break
        else:
            indexPrompt()
            continue


# Main-menu.
watermark()

print("1 - Enter New Object Data")
print("2 - View Collected Object Data")
print("3 - Exit")
print()

while True:
    choice = input()

    if choice == "1":
        dataMenu()
        break
    elif choice == "2":
        dataViewer()
        break
    elif choice == "3":
        clear()
        break
    else:
        continue
import os
import curses
import json
from datetime import datetime

selected_option = ""


# Main-menu.
def mainMenu(menu_win, current_row):
    menu_win.clear()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    menu_win.border()

    menu_h, menu_w = menu_win.getmaxyx()

    menu_options = ["Enter New Object Data", "View Collected Data", "Exit"]

    for idx, element in enumerate(menu_options):
        y = menu_h // 2 + idx - 2
        x = menu_w // 2 - len(element) // 2

        if idx == current_row:
            menu_win.attron(curses.color_pair(1))
            menu_win.addstr(y, x, element)
            menu_win.attroff(curses.color_pair(1))

            # Set the highlighted option to the currently selected option-flag.
            global selected_option
            selected_option = element
        else:
            menu_win.addstr(y, x, element)

    menu_win.refresh()


# Data-entry menu.
def dataMenu(data_win):
    data_win.clear()

    data_win.border()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    data_h, data_w = data_win.getmaxyx()

    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")

    data_win.addstr(data_h // 2 - 2, 2, "Name of Object:")
    data_win.addstr(data_h // 2 - 1, 2, "Current Right-Ascension:")
    data_win.addstr(data_h // 2, 2, "Current Declination:")

    # Object info-input.
    curses.echo()
    data_win.addstr(data_h // 2 - 2, 1, ">")
    data_win.refresh()
    obj = data_win.getstr(data_h // 2 - 2, 18)   # Object name.

    data_win.addstr(data_h // 2 - 2, 1, " ")
    data_win.addstr(data_h // 2 - 1, 1, ">")
    data_win.refresh()
    ra = data_win.getstr(data_h // 2 - 1, 27)    # Object RA value.

    data_win.addstr(data_h // 2 - 1, 1, " ")
    data_win.addstr(data_h // 2, 1, ">")
    data_win.refresh()
    dec = data_win.getstr(data_h // 2, 24)       # Object Dec value.

    data_win.clear()
    data_win.border()
    data_win.refresh()

    # Decode bytes into usable-strings.
    obj_s = str(obj, 'utf-8')
    ra_s = str(ra, 'utf-8')
    dec_s = str(dec, 'utf-8')

    # Info-confirmation prompt.
    data_win.addstr(data_h // 2 - 5, 2, "Is this information correct? Y/N")
    data_win.addstr(data_h // 2 - 4, 2, "Type 'exit' to exit.")
    data_win.addstr(data_h // 2 - 2, 2, "Name of Object: " + obj_s)
    data_win.addstr(data_h // 2 - 1, 2, "RA/Dec: " + ra_s + " / " + dec_s) 

    while True:
        data_win.addstr(data_h // 2 + 2, 2, ">")
        confirmation = data_win.getstr(data_h // 2 + 2, 4)

        if str(confirmation, 'utf-8') == "Y":
            # Open data.json and read it's contents.
            with open("data.json", "r") as json_file:
                json_data = json.load(json_file)
            
            # Append the new data-entry to the relevant json object.
            json_data[obj_s].append({"date": date, "ra": ra_s, "dec": dec_s})

            # Write the new data with pretty-printing.
            with open("data.json", "w") as json_file:
                json.dump(json_data, json_file, indent=4)
            
            json_file.close()

            data_win.clear()
            data_win.addstr(data_h // 2 - 2, 2, "Data written to file.")
            break
        elif str(confirmation, 'utf-8') == "N":
            data_win.clear()
            dataMenu(data_win)
            break
        elif str(confirmation, 'utf-8') == "exit":
            break
        else:
            data_win.addstr(data_h // 2 + 2, 4, " ")
            continue
    
    data_win.clear()
    data_win.refresh()


# Data-viewer.
def dataViewer(viewer_win, root):
    viewer_h, viewer_w = viewer_win.getmaxyx()

    # Small sub-window for displaying short-info and user-input.
    info_win = viewer_win.derwin(3, viewer_w, viewer_h - 3, 0)

    page_1 = ["Alpha Centari-C", "Alpha Centari-A", "Alpha Centari-B", "Barnard's Star",
    "Luhman 16", "WISE 0855-0714", "Wolf 359", "Lalande 21185", "Sirius", 
    "Luyten 726-8", "Ross 154", "Ross 248", "Epsilon Eridani", "Lacaille 9352", "Ross 128",
    "EZ Aquarii", "61 Cygni", "Procyon", "Struve 2398", "Groombridge 34", "DX Cancri",
    "Tau Ceti", "Epsilon Indi"]

    page_2 = ["TON 618", "Holmberg 15A", "IC 1101", "S5 0014+81", "SMSS J215728.21-360215.1",
    "H1821+643", "NGC 6166", "NGC 4889", "Phoenix Cluster Central BH"]

    pages = [page_1, page_2]

    selection_s = 0

    while True:
        # Draw selected list to the data-viewer window.
        def drawLists(selection_s):
            viewer_win.clear()

            for idx, element in enumerate(pages[int(selection_s) - 1]):
                y = 4 + idx
                x = 2

                viewer_win.addstr(y, x, element)

            viewer_win.refresh()
        

        viewer_win.border()
        info_win.border()

        if selection_s == "1":
            viewer_win.addstr(1, 2, "Nearest Stars to Earth")
            viewer_win.addstr(2, 2, "(List decending from nearest)")
        elif selection_s == "2":
            viewer_win.addstr(1, 2, "Most-Massive Black Holes")
            viewer_win.addstr(2, 2, "(List decending from most-massive)")

        page_string = "Scroll pages by typing their page number."

        viewer_win.addstr(1, viewer_w - 9, "Pages: " + str(len(pages)))
        info_win.addstr(1, 3, " " * 20)
        info_win.addstr(1, 1, ">")
        info_win.addstr(1, viewer_w // 2 - len(page_string) // 2, page_string)
        info_win.addstr(1, viewer_w - 16, "'exit' to quit.")
        
        viewer_win.refresh()

        curses.echo()
        selection = info_win.getstr(1, 3)   # User-input
        curses.noecho()

        selection_s = str(selection, 'utf-8')

        if selection_s.isnumeric():
            if int(selection_s) <= len(pages):
                drawLists(selection_s)
        else:
            if selection_s == "exit":
                break
            for alist in pages:
                if selection_s in alist:
                    # Selected-object the user wishes to view.
                    selected_obj = selection_s

                    with open("data.json", "r") as json_file:
                        file_contents = json_file.read()
                    
                    obj_data = json.loads(file_contents)

                    json_file.close()

                    viewer_win.clear()
                    viewer_win.border()
                    info_win.border()
                    info_win.addstr(1, 1, ">")
                    viewer_win.refresh()


                    # 'data.json' is read and the object has it's number of indexes counted.
                    # If the object has no collected data, refer user to text document for more info.
                    def indexPrompt():
                        if len(obj_data[selected_obj]) == 0:
                            print()
                            print("Object has no collected data.")
                            print("Please see 'stellarsol.txt' for more information about this. Sorry!")
                            exit()
                        else:
                            viewer_win.addstr(1, 1, selected_obj+ " has " + str(len(obj_data[selected_obj])) + " entries.")


                    indexPrompt()
                    viewer_win.refresh()

                    # The user is prompted to select an entry until a valid entry is selected.
                    # Relevant data for the selected-object is spit out into the terminal.
                    while True:
                        viewer_win.addstr(viewer_h - 4, 1, "Select an entry to view")
                        viewer_win.refresh()

                        curses.echo()
                        entry_selection = info_win.getstr(1, 3)
                        curses.noecho()

                        entry_selection = str(entry_selection, 'utf-8')

                        if entry_selection.isnumeric():
                            if int(entry_selection) <= len(obj_data[selected_obj]):
                                viewer_win.clear()

                                viewer_win.addstr(1, 1, "Positional data for " + selected_obj + " on "
                                + obj_data[selected_obj][int(entry_selection) - 1]["date"])

                                viewer_win.addstr(3, 1, "RA/Dec: " + obj_data[selected_obj][int(entry_selection) - 1]["ra"]
                                + " / " + obj_data[selected_obj][int(entry_selection) - 1]["dec"])
                                break
                            else:
                                indexPrompt()
                                continue
                        else:
                            info_win.addstr(1, 3, " " * 20)
                            indexPrompt()
                            continue
                else:
                    continue

        viewer_win.refresh()

    viewer_win.clear()
    viewer_win.refresh()


def main(root):
    curses.curs_set(0)

    # Check if terminal is the specified-size.
    term_lines = os.get_terminal_size().lines
    term_cols = os.get_terminal_size().columns

    if term_lines != 32 or term_cols != 115:
        print()
        print("Please resize your terminal to 115 lines, 32 columns.")
        print("Sorry for the inconvience, this will be resolved in the future.")
        print("See 'stellarsol.txt' for more information about this.")
        exit()
    else:
        pass

    h, w = root.getmaxyx()

    menu_win = curses.newwin(h - 1, w // 4, 1, 1)
    data_win = curses.newwin(h - 1, w // 2 + w // 4, 1, w // 4 + 1)
    viewer_win = curses.newwin(h - 1, w // 2 + w // 4, 1, w // 4 + 1)

    current_row = 0

    while True:
        key = root.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < 2:
            current_row += 1
        elif key == ord("e") and selected_option == "Enter New Object Data":
            dataMenu(data_win)
        elif key == ord("e") and selected_option == "View Collected Data":
            dataViewer(viewer_win, root)
        elif key == ord("e") and selected_option == "Exit":
            exit()
        elif key == ord("q"):
            break

        mainMenu(menu_win, current_row)
    
    root.refresh()

curses.wrapper(main)
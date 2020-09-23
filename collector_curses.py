import curses
import json
from datetime import datetime

selected_option = ""


# Main-menu.
def mainMenu(root, current_row, h, w):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    menu_win = curses.newwin(h - 1, w // 4, 1, 1)
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
def dataMenu(root, h, w):
    data_win = curses.newwin(h - 1, w // 2 + w // 4, 1, w // 4 + 1)
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
    data_win.addstr(data_h // 2 - 4, 2, "Type 'Exit' to exit.")
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
            dataMenu(root, h, w)
            break
        elif str(confirmation, 'utf-8') == "Exit":
            exit()
        else:
            data_win.addstr(data_h // 2 + 2, 4, " ")
            continue

    data_win.refresh()


def main(root):
    curses.curs_set(0)

    h, w = root.getmaxyx()

    current_row = 0

    mainMenu(root, current_row, h, w)

    while True:
        key = root.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < 2:
            current_row += 1
        elif key == ord("e") and selected_option == "Enter New Object Data":
            dataMenu(root, h, w)
        elif key == ord("e") and selected_option == "Exit":
            exit()
        elif key == ord("q"):
            break

        mainMenu(root, current_row, h, w)
    
    root.refresh()


curses.wrapper(main)
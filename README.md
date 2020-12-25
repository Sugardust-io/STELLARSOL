# STELLARSOL
A celestial-object tracker in your terminal.

![preview](https://github.com/Sugardust-io/STELLARSOL/blob/master/main/preview.PNG)

**What is STELLARSOL?**

STELLARSOL, a combination of the words 'Stellar' and 'Sol' (referring both to our home solar system, and shorthand for 'console'), is a short passion-project I have been working on and am finally ready to release. In a very short description, it's an object position-tracker for whatever object you wish to track through the night-sky. If you object isn't included, it's fairly easy to include it and it doesn't involve rehashing a ton of code around to do it, meaning STELLARSOL is very expandable.

--

**How are objects tracked?**

Objects are (for the moment) manually tracked via a function included in the program. Users are prompted to input an object's name, it's current Right-Ascension coordinate, and it's current Declination coordinate. This is saved in the 'data.json' file and can be referred back to at any time. An object can have any number of entries, it is not capped in anyway.

For those unfamiliar, RA/Dec coordinates are commonly used by amateur and professional astronomers alike, and it makes tracking objects very easy once you get the hang of it.


--


**How do I use this?**

STELLARSOL is relatively easy to use, but can be confusing for the first time. Below is a short scenario that describes how someone would record and display data for Alpha Centari-C.

* Run 'collector_curses.py' - (give 1 input so the screen refreshes and elements are drawn!)
* Scroll up and down the menu with the arrow keys, select 'Enter New Object Data' with 'e'
  * Input the name of your object, it's current RA and current Dec data.
  * Review your data and confirm if it is correct.
  
* Scroll down to 'View Collected Data', select it with 'e'
* Typing numbers will display various pages showing names of objects, find 'Alpha Centari-C' on page 1.
  * Type 'Alpha Centari-C', hit enter.
  * You will be prompted to select a data entry, the last one will be your new data entry. Select an entry by simply typing it's number.
  * Your data is now on the screen, congratulations! Typing 'exit' will return control to the main menu.
 
Important to note that **ALL** 1st index entries for **ALL** objects are their J2000-epoch coordinates. Any entries which denote an object's position on J2000 will be marked with a 'J2000' tag at the beginning of it's RA/Dec entry. The 1st entry should always be reserved for this though for clarity.

--

**Planned updates**

I have a number of planned updates to STELLARSOL, which will focus mainly on streamlining the process for users, as I am aware it's somewhat clunky at first. Once you get the hang of it, you can very easily navigate STELLARSOL very quickly, but making it more welcoming and easy to use for new users is my main focus.

The following are a number of planned updates, in no particular order, that I wish to make to improve STELLARSOL:

* Improve user-control, fix some issues such as having to give in input at first run.
* Options to manipulate objects from within the program (eg. add new objects, delete, etc.)
* Include various object details along with it's positional-data.
* Eventual real-time position approximation for objects with sufficient data.


That's all I have to say for now really about this project. I will be working on it from this time forward as I very much enjoy pouring time and love into it. I know it's not the best design-wise and likely code-wise, but STELLARSOL is really my first "complex" curses program that is more than a simple main-menu on a screen. You can read more details that I have included about STELLARSOL, including it's history and revisions and other F.A.Q. in the 'stellarsol.txt' document I have included in the repository.

If you wish to contact me directly about this project, I'm always free for contact on Discord: @Chaussettes#8027

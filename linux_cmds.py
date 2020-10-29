import os

def show_linux_menu():
    print("""
    Press 1 to check date
    Press 2 to see calendar
    Press 3 to see RAM usage
    """)
    linux_command=input()
    if int(linux_command)==1:
        date_show()
    elif int(linux_command)==2:
        show_calendar()
    elif int(linux_command)==3:
        ram_usage()


def clear_screen_linux():
    os.system("clear")
    show_linux_menu()

def date_show():
    os.system('date')

def ram_usage():
    os.system('free -m')

def show_calendar():
    os.system('cal')
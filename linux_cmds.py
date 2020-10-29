import os

def show_linux_menu():
    print("""
    Press 1 to check date
    Press 2 to see calendar
    Press 3 to see RAM usage
    """)
    linux_command=input()
    linux_performer(linux_command)

def clear_screen_linux():
    os.system("clear")
    show_linux_menu()

def linux_performer(linux_command):
    if linux_command=='1':
        os.system('date')
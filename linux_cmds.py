import os

def show_linux_menu():
    linux_command=22
    while linux_command!=0:
        print("""
    Press 1 to check date
    Press 2 to see calendar
    Press 3 to see RAM usage
    Press 4 to see the background running process
    Press 5 to check the ip address
    Press 6 to check from which we login
    Press 7 to start the firewall
    Press 8 to stop the firewall
    Press 9 to see about the CPU
    Press 0 to exit
    """)
        linux_command=input()
        if int(linux_command)==1:
            date_show()
        elif int(linux_command)==2:
            show_calendar()
        elif int(linux_command)==3:
            ram_usage()
        elif int(linux_command)==4:
            running_process()
        elif int(linux_command)==5:
            ip_address()
        elif int(linux_command)==6:
            who_am_i()
        elif int(linux_command)==7:
            firewall_start()
        elif int(linux_command)==8:
            firewall_stop()
        elif int(linux_command)==9:
            lscpu()
        elif int(linux_command)==0:
            break
        else:
            print("Incorrect input please try again")

def clear_screen_linux():
    os.system("clear")
    show_linux_menu()

def date_show():
    os.system('date')

def ram_usage():
    os.system('free -m')

def show_calendar():
    os.system('cal')
    
def running_process():
    os.system('jobs')

def ip_address():
    os.system('ifconfig enp0s3')
    
def who_am_i():
    os.system('whoami')
    
def firewall_start():
    os.system('systemctl start firewalld')
    
def firewall_stop():
    os.system('systemctl stop firewalld')
    
def lscpu():
    os.system('lscpu')

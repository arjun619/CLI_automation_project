import os

def load_webserver():
    server_cmd=3
    while server_cmd!=0:
        server_cmd=input("""
        ######################## WEBSERVER SETUP ########################
        1. Press 1 to setup webserver
        2. Press 2 to start server
        3. Press 3 to stop services
        4. Press 4 to create a file
        0. Press 0 to exit
    """)
        if int(server_cmd)==1:
            os.system("yum install httpd")
        elif int(server_cmd)==2:
            os.system("systemctl start httpd")
        elif int(server_cmd)==3:
            os.system("systemctl stop httpd")
        elif int(server_cmd)==4:
            file_name=input("Enter the name of html file you want to create")
            os.system(f"vi /var/www/html/{file_name}.html")
        elif int(server_cmd)==0:
            break
        else:
            print('Invalid Input')

def clear_screen_server():
    os.system("clear")
    load_webserver()
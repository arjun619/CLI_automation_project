import linux_cmds
import aws_cli
import partitioner
import docker_commands
import hadoop_setup
import os
import lvm_script
import webserver_setup
import yum_file

os.system('tput setaf 1')
print("""          ________________________
         |                       |
         |ALL-FOR-ONE Interface  |
         |_______________________|                   """)

def initial_interface():
    a=12
    while a!='0':
        print("""        Press 1 for performing Linux Commands
        Press 2 for Hadoop Setup
        Press 3 for AWS CLI configuration
        Press 4 to use docker
        Press 5 to perform partition
        Press 6 to create LVM partition
        Press 7 to setup httpd server
        Press 8 to configure
        Press 0 to exit
        """)
        a=input()
        if a=='1':
            linux_cmds.clear_screen_linux()
        elif a=='2':
            hadoop_setup.clear_screen_hadoop()
        elif a=='3':
            aws_cli.clear_screen_aws()
        elif a=='4':
            docker_commands.clear_screen_docker()
        elif a=='5':
            partitioner.clear_screen_partition()
        elif a=='6':
            lvm_script.clear_screen_lvm()
        elif a=='7':
            webserver_setup.clear_screen_server()
        elif a=='8':
            yum_file.clear_screen_yum()
        else:
            print("Incorrect Choice\n")         
initial_interface()
print("\n\n\nthanks for visiting  : )")


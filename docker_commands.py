
import linux_cmds
import os
import subprocess
#import interface
def load_docker_cmds():
    docker_c=111
    os.system('tput setaf 3')
   
    while docker_c!='0':
        print(""" 
            ################DOCKER SETUP#################
        


        1. Start Services
        2. See current running containers
        3. View all containers
        4. Create a new Container
        5. Attach a running container
        6. Start of Stop  a container
        7. Stop docker services
        0. To exit Docker TUI
    """)
        docker_c=input()

        if int(docker_c) == 1:
            start_docker()
        if int(docker_c)==2:
            view_instance()
        #load_docker_cmds()
        if int(docker_c) == 3:
            view_all_instance()
        if int(docker_c) == 4:
            create_container()
        if int(docker_c) == 5:
            attach_container()
        if int(docker_c) == 6:
            start_stop_container()
        if int(docker_c)==7:
            stop_service()
        if int(docker_c) == 0:
            print('docker is now exitting .. ..  ..')
        #interface.initial_interface()
  
def clear_screen_docker():
    os.system("clear")
    load_docker_cmds()

def view_instance():
    os.system("docker ps")

def view_all_instance():
    os.system("docker ps -a")

def create_container():
    print("""which container you want to create""")
    img_name = input('name of the docker image: ')
    tag = input('tag of the image: ')
    os_name = input('give a name to the container os: ')
    try:
        os.system('docker run -dit --name {} {}:{}'.format(os_name,img_name,tag))
    except:
        print('Either of the name of the image or the tag is inccorred, ABORT!!')
    finally:
            load_docker_cmds()

def attach_container():
    print('current running containers as:')
    view_instance()
    attach_os = input('name of the ID of the container you want to attach')
    os.system(f'docker attach {attach_os}')

def stop_service():
    os.system("systemctl stop docker")


def start_stop_container():
    ss = input('Do you want to start of stop  a container')
    if ss.lower() == 'stop':
        print('the running containers are : \n')
        view_instance()
        to_stop = input('enter the name or id of the container to stop')
        os.system(f'docker stop {to_stop}')
    if ss.lower() == 'start':
        print('all the stopped containers are: \n')
        view_all_instance()
        to_start = input('enter the name or id of the container to start')
        os.system(f'docker stop {to_start}')
    else:
        print('invalid command')


def exit_docker():
    exit()

def start_docker():
    os.system("systemctl start docker")

def docker_service_commands():
    cmd = input('Enter the service commands,[n] to exit:')
    if cmd =='n':
        return load_docker_cmds()
    status = subprocess.getstatusoutput('systemctl {} docker | grep Active'.format(cmd))
    print(status)
    cmd = input('next service command,[n] to exit:')
    if cmd =='n':
        return load_docker_cmds()
    elif cmd not in ['start','stop','status']:
        print('Ivalid command, please try again')
        return docker_service_commands()
    else:
        return docker_service_commands()


load_docker_cmds()

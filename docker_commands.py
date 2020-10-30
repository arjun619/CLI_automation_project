import os

def load_docker_cmds():
    print("""
        1. See current running containers
        2. View all containers
        3. Create a new Container
    """)
    docker_c=input()
    if int(docker_c)==1:
        view_instance()

def clear_screen_docker():
    os.system("clear")
    load_docker_cmds()

def view_instance():
    os.system("docker ps")

def view_all_instance():
    os.system("docker ps -a")

def create_container():
    print("""which container you want to create""")


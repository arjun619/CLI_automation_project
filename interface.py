import linux_cmds
import aws_cli
import partitioner
import docker_commands
import hadoop_setup
print("""          ________________________
         |                       |
         |One-For-All Interface  |
         |_______________________|                   """)

def initial_interface():
    a=12
    while a!='0':
        print("""        Press 1 for performing Linux Commands
        Press 2 for Hadoop Setup
        Press 3 for AWS CLI configuration
        Press 4 to use docker
        Press 5 to perform partition
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
        else:
            print("Incorrect Choice\n")         
initial_interface()
print("\n\n\nthanks for visiting  : )")


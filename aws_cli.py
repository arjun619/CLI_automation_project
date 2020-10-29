import os

def load_cmds_aws():
    print("""
    Press 1 to login using access key
    Press 2 to setup EC2 instance
    Press 3 to check current EC2 instances
    press 0 to exit AWS menu
    """)
    aws_a=input()
    if int(aws_a)==2:
        create_ec2()
    if int(aws_a)==3:
        check_running_instances()
    if int(aws_a)==0


def clear_screen_aws():
    os.system("clear")
    load_cmds_aws()

def create_ec2():
    ami_type=["ami-0e306788ff2473ccb","ami-052c08d70def0ac62","ami-0b2f6494ff0b07a0e","ami-0cda377a1b884a1bc"]
    machine_size=['t2.nano','t2.micro','t2.small','t2.medium']
    preference=dict()

    print("""select the AMI you want to use
    1.ami-0e306788ff2473ccb           Amazon Linux 2
    2.ami-052c08d70def0ac62           RHEL 8
    3.ami-0b2f6494ff0b07a0e           Windows Server (GUI)
    4.ami-0cda377a1b884a1bc           Ubuntu 20.04
            """)
    machine_type=input()
    preference['machine_type']=ami_type[int(machine_type)-1]

    print("""Select machine type
        1. t2.nano
        2. t2.micro(free tier eligible)
        3. t2.small
        4. t2.medium """
    )
    size=input()
    preference['size']=machine_size[int(size)-1]

    num_of_inputs=int(input("How many instances you want to create \n"))
    preference['number_of_instances']=num_of_inputs
    print(f"aws ec2 run-instances --image-id {preference['machine_type']} --count {preference['number_of_instances']} --instance-type {preference['size']}")
    os.system(f"aws ec2 run-instances --image-id {preference['machine_type']} --count {preference['number_of_instances']} --instance-type {preference['size']}")

def check_running_instances():
    os.system("aws ec2 describe-instances")
    
    

    
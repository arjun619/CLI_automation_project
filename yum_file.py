import os


def load_yum_cmds():
    while True:
        os.system('tput setaf 10')
        
        print("""\n\n\t\t------------ Automated yum -----------------\n\n
            1. Configure yum repository for dvd, docker, httpd and installing epel-release
            2. check the yum repository
            3. check if software is present in yum repository and is installed or not
            4. install any software present in yum repository
            5. remove any software which is installed in the system
            9. return to main menu
        """)
        yum_c = input("Enter your choice here: ")

    
        if int(yum_c) == 1:
            con_yum()
        elif int(yum_c) == 2:
            check_yum_repo()
        elif int(yum_c) == 3:
            check_soft()
        elif int(yum_c) == 4:
            install_yum()
        elif int(yum_c) == 5:
            remove_yum()
        elif int(yum_c) == 9:
            break
        else:
            print("Incorrect input please try again")
            input("Enter to continue")


def clear_screen_yum():
    os.system("clear")
    load_yum_cmds()
def con_yum():
	os.system("clear")
	
	epel = "https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm"
	os.system('dnf install {} -y'.format(epel))
	with open("/etc/yum.repos.d/yash.repo",'w+') as f:
		f.write("[dvd1]\n")
		f.write("baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\n")
		f.write("gpgcheck=0\n\n")
		f.write("[dvd2]\n")
		f.write("baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\n")
		f.write("gpgcheck=0\n\n")
		f.write("[docker]\n")
		f.write("baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\n")
		f.write("gpgcheck=0\n\n")


def check_yum_repo():
	os.system("clear")
	
	os.system("dnf repolist")
	input("Enter to continue")

def check_soft():
	os.system("clear")
	
	soft = input("Enter the name of software you want to check is present and installed or not: ")
	if soft == 'docker' or soft == 'docker-ce':
		os.system('dnf list docker-ce')
	else:
		os.system("dnf list {}".format(soft))	
	input("Enter to continue")

def remove_yum():
	os.system("clear")
	
	soft = input("Enter the name of software you want to remove: ")
	os.system("dnf remove {} -y".format(soft))
	input("Enter to continue")

def install_yum():
	os.system("clear")
	
	soft = input("Enter the name of software you want to install: ")
	if soft == 'docker' or soft == 'docker-ce':
		os.system('dnf install docker-ce --nobest -y')
	else:
		os.system("dnf install {} -y".format(soft))
	input("Enter to continue")
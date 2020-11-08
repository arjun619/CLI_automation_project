import os

def load_partition():
	while True:
		os.system('clear')
		os.system('tput setaf 5')
		print('''
		#################PARTITIONER TOOL#################
        

		
			What action you want to perform!!
			1. create a partition
			2. format a partition
			3. mount a partition
			0. To exit
			''')
		hadoop_input = input()
		hadoop_input = int(hadoop_input)

		if hadoop_input == 1:
			create_partition()
		elif hadoop_input == 2:
			format_partition()
		elif hadoop_input == 3:
			mount_partition()
		elif hadoop_input == 0:
			break
		else:
			print("Incorrect input please try again")
			input("Enter to continue")

def clear_screen_partition():
    os.system("clear")
    load_partition()

def create_partition():
	print("\n\nBelow are the available disk: \n\n")
	os.system('fdisk -l')
	disk_name = input("Enter name of disk you want to make partition: ")
	#print("\n\nAfter this you have to manualy make partition\n\n")
	os.system(f'fdisk {disk_name}')

def format_partition():
	print("\n\nBelow are the available disk with partition: \n\n")
	os.system('fdisk -l')
	partition_name = input("Enter name of partition you want to format: ")
	os.system(f'mkfs.ext4 {partition_name}')

def mount_partition():
	val = input("\t1. if folder is already created\n\t2. to created a new folder\n\t Enter your choice: ")
	fol_name = "temp"
	if int(val) == 1:
		fol_name = input("Enter the name of folder with location: ")
	elif int(val) == 2:
		fol_name = input("Enter the name of folder you want to mount partition: ")
		os.system(f'mkdir {fol_name}')
		print("\n\nBelow are the available disk with partition: \n\n")
		os.system('fdisk -l')
		partition_name = input("\n\nEnter name of partition you want to format: ")
		os.system(f'mount {partition_name} {fol_name}')

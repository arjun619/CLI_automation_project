
import os

def load_cmds_hadoop():
    print("""What do you want to do
    1. Setup the HDFS file
    2. Setup the core-site file
    3. Start datanode
    4. Start namenode
    5. Check DFS admin report
    
    """)
    hadoop_n=input()
    if int(hadoop_n)==1:
        setup_hdfs_file()
    if int(hadoop_n)==2:
        setup_core_file()
    if int(hadoop_n)==3:
        start_datanode()
    if int(hadoop_n)==4:
        start_namenode()

def start_namenode():
    os.system("hadoop namenode format")
    os.system("hadoop-daemon.sh start namenode")

def start_datanode():
    pass
def setup_core_file():
    val=input("Do you wanna configure as namenode or datanode . Press 1 for namenode or 2 for datanode\n")
    if int(val)==1:
        with open("/etc/hadoop/core-site.xml",'w+') as f:
            f.write("<?xml version='1.0'?>\n")
            f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n")
            f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
            f.write("<configuration>\n")
            f.write("<property>\n")
            f.write("<name>fs.default.name</name>\n")
            f.write("<value>hdfs://0.0.0.0:9001</value>\n")
            f.write("</property>\n")
            f.write("</configuration>\n")

def setup_hdfs_file():
    val=input("Do you wanna configure as namenode or datanode . Press 1 for namenode or 2 for datanode\n")
    if int(val)==1:
        with open("/etc/hadoop/hdfs-site.xml",'w+') as f:
            f.write("<?xml version='1.0'?>\n")
            f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n")
            f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
            f.write("<configuration>\n")
            f.write("<property>\n")
            f.write("<name>dfs.name.dir</name>\n")
            f.write("<value>/nn</value>\n")
            f.write("</property>\n")
            f.write("</configuration>\n")
        os.system("mkdir /nn")
        #os.system("hadoop namenode format")


def clear_screen_hadoop():
    os.system("clear")
    load_cmds_hadoop()


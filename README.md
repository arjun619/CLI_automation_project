# CLI_automation_project

This linux based command line interface provides multiple technology integration in a CLI based menu driven program. 
  The technologies include: 
  * AWS
  * docker
  * hadoop
  * Performing LVM partitions
  * Linux

## Dependencies

The program is designed on centos 8 system. So it works best on centos environment. However some of the functionalities are not restricted to the operating system like AWS and docker. `

### AWS

Before using AWS the AWS CLI software needs to be installed on the system. Follow the steps to install AWS CLI    
* *curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"*   
* *unzip awscliv2.zip*    
* *sudo ./aws/install*    

### Docker

Before using the docker option in the menu the docker needs to be installed in the system. If the software is not present in the system then first use the yum option from the menu to configure docker and yum repositories for it.

### Hadoop

Hadoop uses java in the backend and hence for using hadoop the jdk and hadoop software must be present in the system.    
JDK (https://www.oracle.com/in/java/technologies/javase-jdk15-downloads.html)  
Hadoop (https://hadoop.apache.org/releases.html)  





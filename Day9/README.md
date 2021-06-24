### Installing Java 11
```
sudo yum install -y java-11-openjdk-devel
```

### Installing Maven
```
cd Downloads
wget https://mirrors.estointernet.in/apache/maven/maven-3/3.8.1/binaries/apache-maven-3.8.1-bin.tar.gz
tar xvfz apache-maven-3.8.1-bin.tar.gz
cd apache-maven-3.8.1
pwd
```
M2_HOME path is /home/jegan/Downloads/apache-maven-3.8.1

### Find the JAVA_HOME path
```
which javac
ls -l /usr/bin/javac
ls -l /etc/alternatives/javac
```
JAVA_HOME is /usr/lib/jvm/java-11-openjdk-11.0.11.0.9-2.el8_4.x86_64

### Add the below in your bashrc file
```
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.11.0.9-2.el8_4.x86_64
export M2_HOME=/home/jegan/Downloads/apache-maven-3.8.1
export PATH=$JAVA_HOME/bin:$M2_HOME/bin:/usr/local/bin:$PATH
```
To export the environment variables immediately in the current session,
```
source ~/.bashrc
```

### Downloading Jenkins and launching Jenkins
```
cd Downloads
wget https://get.jenkins.io/war-stable/2.289.1/jenkins.war
java -jar ./jenkins.war
```
At that time of launching Jenkins first time, make sure you select "Install Suggested Plugins". Also make sure
you have create an user, don't skip and continue as admin.

### Installing Jenkins Plugins
Navigate Menu --> Manage Jenkins --> Manage Plugins --> Available Tab
Install the below Plugins
1. Docker
2. Maven Integration
3. Ansible
4. Ansible Tower
5. Build Pipeline

Install and Restart Jenkins.
You may access Jenkins dashboard from your favourite web browser at http://localhost:8080

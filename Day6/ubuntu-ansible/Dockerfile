FROM ubuntu:16.04
MAINTAINER Jeganathan Swaminathan <jegan@tektutor.org>

RUN apt-get update && apt-get install -y openssh-server python3 git sudo
RUN ln -s -f /usr/bin/python3 /usr/bin/python
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN useradd -m -p tektutor -s /bin/bash tektutor 
RUN echo 'tektutor:tektutor' | chpasswd

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

RUN mkdir -p /root/.ssh
COPY authorized_keys /root/.ssh/authorized_keys
RUN chmod -R 700 /root/.ssh 

RUN mkdir -p /home/tektutor/.ssh
COPY authorized_keys /home/tektutor/.ssh/authorized_keys
RUN chown tektutor -R /home/tektutor/.ssh
RUN chmod -R 700 /home/tektutor/.ssh 

COPY sudoers /etc/sudoers
RUN chmod -R 700 /etc/sudoers

EXPOSE 22
EXPOSE 80 
CMD ["/usr/sbin/sshd", "-D"]

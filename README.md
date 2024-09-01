# SSH-Bruteforce
This tools used for ssh-bruteforce in during pentesting. This tool os required python and following modules.A simple Python script that performs brute-force attacks on SSH servers to test the strength of passwords. This tool is intended for ethical hacking and security testing purposes only.

**Overview:**

This script attempts to enumerate username's and password's to ssh service. It’s designed to be a straightforward example of how SSH brute-force attacks work, focusing on educational use for security professionals and ethical hackers.

**Features**

1.Customised port (If ssh service running on the other port rather then 22).
2.Customizable target IP, username, and password list.


**Installtion**

1.Clone the repositry and move to the directory using follwoing command.

```
git clone https://github.com/KSK-IN/ssh-bruteforce.git
cd ssh-bruteforce.py
```
2. install requirement follwoing command.
```
pip -r install requirements.txt
```
3.Run the ssh-bruteforce.py file using following commmand.

```
python3 ssh_brute.py --help

  The SSH bruteforcing tool

          
            ░█▀▀░█▀▀░█░█░░░█▀▄░█▀▄░█░█░▀█▀░█▀▀░█▀▀░█▀█░█▀▄░█▀▀░█▀▀
            ░▀▀█░▀▀█░█▀█░░░█▀▄░█▀▄░█░█░░█░░█▀▀░█▀▀░█░█░█▀▄░█░░░█▀▀
            ░▀▀▀░▀▀▀░▀░▀░░░▀▀░░▀░▀░▀▀▀░░▀░░▀▀▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀


          

#Help of the command
1. sshbrute.py -t [ip] -p [port] -u [username] or -U [username-wordlist] -l [password] or -P [password-wordlist]

usage: ssh_brute.py [-h] -t TARGET [-p PORT] [-u USERNAME] [-U USERNAME]
                    [-l PASSWORD] [-P PASSWORD]

SSH brute forceing Tool

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Enter the target ip or name
  -p PORT, --port PORT  Port number
  -u USERNAME, --username USERNAME
                        Enter the username
  -U USERNAME, --Username USERNAME
                        Enter the path of username wordlist
  -l PASSWORD, --password PASSWORD
                        Enter the password
  -P PASSWORD, --Password PASSWORD
                        Enter the path of password wordlist 

```

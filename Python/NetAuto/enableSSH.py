#just for cisco devices CATOS
import getpass
import telnetlib

def configure_ssh_telnet(ip, username, password):
    try:
        print("Configuring SSH on Switch " + ip)
        tn = telnetlib.Telnet(ip)
        tn.read_until(b"Username: ")
        tn.write(username.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

        tn.write(b"conf t\n")
        tn.write(b"ip domain-name f5admin.ir\n")
        tn.write(b"crypto key generate rsa modulus 2048\n")
        tn.write(b"ip ssh version 2\n")
        tn.write(b"line vty 0 15\n")
        tn.write(b"transport input ssh\n")
        tn.write(b"exit\n")
        tn.write(b"wr\n")
        tn.write(b"exit\n")

        print("SSH enabled on " + ip)
    except Exception as e:
        print("Failed to enable SSH on " + ip + ": " + str(e))

def main():
    username = input("Enter your Telnet username: ")
    password = getpass.getpass()

    with open('myswitches') as f:
        for ip in f:
            ip = ip.strip()
            configure_ssh_telnet(ip, username, password)

if __name__ == "__main__":
    main()
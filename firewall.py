import socket

def block_ip(ip, port):
    with open("/etc/hosts.deny", "a") as file:
        file.write(f"ALL: {ip}\n")

def main():
    ip = input("Enter the IP address to block: ")
    port = int(input("Enter the port to block: "))
    block_ip(ip, port)
    print(f"IP {ip} and port {port} have been blocked.")

if __name__ == "__main__":
    main()
import requests
import os


ip_address = None
url = "https://api.particle.io/v1/devices/25002c001147343438323536"
access_token = "71e19336abefabb4bd05254c6975a16c4232fd05"

def main(options):
    opt = menu(options)

    if options[list(options.keys())[opt]]() != -1:
        main(options)

def menu(options):
    print()
    for index,opt in enumerate(options.keys()):
        print("{0}) {1}".format(index, opt))

    user = input("Please select an option through a index: ")

    if len(user) != 1:
        menu(options)
    elif not user.isdigit():
        menu(options)
    elif int(user) > len(options) or int(user) < 0:
        menu(options)

    return int(user)

def getIp():
    global ip_address
    print(access_token)
    r = requests.get(url + "/IpAddr", params = {"access_token": access_token})
    print(r.content)
    ip_address = r.json()["result"]

    print("[*] Recieved ip address: " + ip_address)

    return ip_address

def serverTurnOn():
    print("\n[*] Sending post request")
    r = requests.post(url + "/relay", data = {"access_token": access_token})

    output = r.json()

    print("[*] Connected: " + str(output["connected"]))
    print("[*] Return value: " + str(output["return_value"]) + "\n")


def openSsh():
    ip_address = getIp()
    print("[*] Initiating interactive ssh session")
    os.system("ssh james@" + ip_address)

def exit():
    print("[*] Exiting..")
    return -1

options = {
        "Turn on the server" : serverTurnOn,
        "Open ssh session with server" : openSsh,
        "exit": exit
        }

main(options)

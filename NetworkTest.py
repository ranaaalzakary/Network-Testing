import os
import subprocess
import time
import platform
import re
import socket
import netifaces


print("__________________________________________________________________________________")
#To first startoff with our script we need to clear the termimal to keep it clean
print("Hello friend!, welcome to the ping tester, the screen will be cleared in 2 seconds")
time.sleep(3)
os.system('clear')


#Creating a user-freindly menu that allows them to perform the following tasks
def menu():
	print("Press [1] to find the Default Gateway")
	print("Press [2] to test connectivity to a remote IP Address")
	print("Press [3] to get the IP Address of a DNS server")
	print("Press [0] to exit the program")
	print()

menu()
option = int(input("Enter Your Option:  "))


#Creating a while loop for the menu until the user presses 0 and exists
while option != 0:

	#Option 1: to find the Default Gateway and ping it
	if option == 1:
		print()
		print("Option [1] has been called!")
		gateway_net = netifaces.gateways()
		gateway = gateway_net['default'][netifaces.AF_INET][0]

		#This command pings to the default gateway
		os.system(f'ping -c 4 {gateway}')


	#Option 2: To test connectivity to a remote IP Address
	elif option == 2:
		print()
		print("Option [2] has been called!")

		#This command pings to RIT's DNS
		os.system("ping -c 4 129.21.3.17")


	#Option 3: To get the IP Address of a DNS Server
	elif option == 3:
		print()
		print("Option [3] has been called!")

		#This command pings to google.com
		os.system("ping -c 4 www.google.com")


	else:
		print()
		print("Invalid option")

	print(".")
	print(".")
	print(".")
	menu()
	option = int(input("Enter Your Option: "))

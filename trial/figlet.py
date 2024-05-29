from pyfiglet import Figlet
import sys
import random


figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(figlet.getFonts()))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font = sys.argv[2])

else:
    sys.exit("Invalid Usage")

response = input("Input: ")
print(figlet.renderText(response))



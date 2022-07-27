import os
os.chdir(os.path.dirname(__file__))
import subprocess

# os.popen('discord_bot.py')
subprocess.Popen(['python', 'main_bot.py'])
subprocess.Popen(['python', 'main.py'])

#these process do not close automatically
#list the id of these new python processes
#TODO
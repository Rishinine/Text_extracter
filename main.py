import subprocess
import platform
from os import remove
subprocess.run(["python", "/home/rishi/Documents/image_to_text/screenshot.py"])

# Run the second script
subprocess.run(["python", "/home/rishi/Documents/image_to_text/img_to_text.py"])
def send_notification(message):
    system = platform.system()
    if system == "Darwin":  # macOS
        subprocess.run(['osascript', '-e', f'display notification "{message}" with title "Script Notification"'])
    elif system == "Linux":  # Linux
        subprocess.run(['notify-send', 'Script Notification', message])
    elif system == "Windows":  # Windows
        subprocess.run(['powershell', '-Command', f'New-BurntToastNotification -Text "{message}"'])
remove('sample.png')
send_notification("Message extracted successfully")
import pywhatkit as kit
import datetime

phone_number = "+1234567890"  # Replace with the recipient's phone number, including the country code
message = "Hello, World!"  # Replace with your desired message

now = datetime.datetime.now()
hours = now.hour
minutes = now.minute + 2  # Send the message 2 minutes from now

kit.sendwhatmsg(phone_number, message, hours, minutes)

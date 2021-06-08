import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

email_password = "qgxtrfapiuyxlbbr"
email_address = "adrian.romanov.01@gmail.com"

def send_email(photo_id):
  image_data = open(f'D:/Photos/중요한/---/Python Script Wallpapers/mobile/{photo_id}.jpg', 'rb').read()
  message = MIMEMultipart()
  message['Subject'] = 'This is Your Wallpaper for Today!'
  message['From'] = email_address
  message['To'] = email_address
  
  text = MIMEText('Hi! Good Morning, Adrian!\nThis is Your Wallpaper')
  image = MIMEImage(image_data, name = os.path.basename(f'{photo_id}.jpg'))
  message.attach(text)
  message.attach(image)
  
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  
  server.login(email_address, email_password)
  server.sendmail(email_address, email_address, message.as_string())
  server.quit()
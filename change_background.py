import ctypes
import urllib.request
import requests
import json
import random
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

email_password = "rcrqqmgyhucnafks"
email_adress = "adrian.romanov.00@gmail.com"

key = 'qObf1S9HyrJygxOrQLlQlgTw7KNG5jxqkfSW0PGXlOM'
categories = ['animals','wallpapers','music','piano','sports','landscape','nature','travel','buisness','work','technology','programming','coding','motivation','life','interiors','arhitecture','food','red','design','car','city','home']
page_number = 20

def send_email(photo_id, category):
  image_data = open(f'C:/Users/adria/Pictures/Photos/중요한/---/Python Script Wallpapers/mobile/{photo_id}.jpg', 'rb').read()
  message = MIMEMultipart()
  message['Subject'] = 'This is Your Wallpaper for Today!'
  message['From'] = email_adress
  message['To'] = email_adress
  
  text = MIMEText(f'Hi! Good Morning, Adrian!\nThis is Your Wallpaper from the Category {category.capitalize()}')
  image = MIMEImage(image_data, name = os.path.basename(f'{photo_id}.jpg'))
  message.attach(text)
  message.attach(image)
  
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  
  server.login(email_adress, email_password)
  server.sendmail(email_adress, email_adress, message.as_string())
  server.quit()
  

def changeBackground():
  def filterDesktopFormatPhoto(item):
    if item['w'] > item['h']: return True
    else: return False
    
  def filterMobileFormatPhoto(item):
    if item['w'] < item['h']: return True
    else: return False
    
  def getMostLiked(array, n, orientation):
    intial_array_length = len(array)
    result_array = []
    likes = [item['likes'] for item in array]
    while len(result_array) < n:
      if len(array) == 0:
        print('there are no '+orientation +' photos')
        break
      
      result_array.append(array[likes.index(max(likes))])
      likes[likes.index(max(likes))] = 0
      
      if len(result_array) == intial_array_length:break
    return result_array
  
  page = random.randint(1,page_number)
  find = random.choice(categories)
  response = requests.get(f'https://api.unsplash.com/search/photos?page={page}&per_page=30&query={find}&client_id={key}').json()
  results = response['results']

  my_data = [
    {'id':result['id'],
     'likes':result['likes'],
     'link':result['urls']['full'],
     'w':result['width'],
     'h':result['height']}
     for result in results]
  
  desktop_photos = list(filter(filterDesktopFormatPhoto, my_data))  
  mobile_photos = list(filter(filterMobileFormatPhoto, my_data))
  
  liked_desktop_photos = getMostLiked(desktop_photos, 5,'desktop')
  liked_mobile_photos = getMostLiked(mobile_photos,  5,'mobile')
  
  desktop_final = random.choice(liked_desktop_photos)
  desktop_final_photo = desktop_final['link']
  desktop_photo_id = desktop_final['id']

  os.chdir('C:/Users/adria/Pictures/Photos/중요한/---/Python Script Wallpapers/desktop')

  desktop_photo = urllib.request.urlretrieve(desktop_final_photo, str(desktop_photo_id) + '.jpg')
  
  ctypes.windll.user32.SystemParametersInfoW(0x14, 0, f'C:/Users/adria\Pictures/Photos/중요한/---/Python Script Wallpapers/desktop/{str(desktop_photo_id)}.jpg', 0)
  
  mobile_final = random.choice(liked_mobile_photos)
  mobile_final_photo = mobile_final['link']
  mobile_photo_id = mobile_final['id']
  
  os.chdir('C:/Users/adria/Pictures/Photos/중요한/---/Python Script Wallpapers/mobile')
  
  mobile_photo = urllib.request.urlretrieve(mobile_final_photo, str(mobile_photo_id) + '.jpg')
  
  send_email(mobile_photo_id,find)
  
def main():
  
  changeBackground()

  print('Do You Hate Your Wallpaper?')
  print()
  print()
  print('(for yes write "y", for no write "n")')
  print()
  answer = input("->")

  if answer == 'n':
    return
  else:
    main()
    
main()

import ctypes
import random

from send_email import send_email
from photo_downloader import getIdOfPhoto
from data_parser import *
  
def setWallpaper(id):
  ctypes.windll.user32.SystemParametersInfoW(0x14, 0, f'D:/Photos/중요한/---/Python Script Wallpapers/desktop/{str(id)}.jpg', 0)
  print('set the wallpaper')

def changeBackground():
    
  # get the data from the API
  my_data = getAPIData()
  print('got the data')
  
  desktop_photos, mobile_photos = sortIntoMobileAndDesktopFormat(my_data)
  
  liked_desktop_photos = getMostLiked(desktop_photos, 5, 'desktop')
  liked_mobile_photos = getMostLiked(mobile_photos, 5, 'mobile')
  
  # DESKTOP
  
  desktop_final_photo = random.choice(liked_desktop_photos)
  
  print('downloading desktop photo')
  
  # downloads the photo and returns the id
  desktop_photo_id = getIdOfPhoto(desktop_final_photo, 'desktop')
  
  print('downloaded desktop photo')
  
  setWallpaper(desktop_photo_id)
  
  # MOBILE
  
  mobile_final_photo = random.choice(liked_mobile_photos)
  
  print('downloading mobile photo')
  
  mobile_photo_id = getIdOfPhoto(mobile_final_photo, 'mobile')
  
  print('downloaded mobile photo')
  
  print("begin sending the email")
  send_email(mobile_photo_id)
  print("sent the email")
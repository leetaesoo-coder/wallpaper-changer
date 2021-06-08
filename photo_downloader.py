import os
import urllib.request

# download the photo and returns the id
def getIdOfPhoto(photo, orientation):
  if (orientation != 'mobile' and orientation != 'desktop'):
    print('orientation should be only (\'mobile\' or \'desktop\')')
  
  link = photo['link']
  id = photo['id']

  os.chdir('D:/Photos/중요한/---/Python Script Wallpapers/' + orientation)

  urllib.request.urlretrieve(link, str(id) + '.jpg')
  
  return id
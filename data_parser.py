import random
import requests
import json

categories = ['animals','wallpapers','music','piano','sports','landscape','nature','travel','buisness','work','technology','programming','coding','motivation','life','interiors','arhitecture','food','red','design','car','city','home']
page_number = 20

key = 'qObf1S9HyrJygxOrQLlQlgTw7KNG5jxqkfSW0PGXlOM'

def getAPIData():
  page = random.randint(1,page_number)
  find = random.choice(categories)
  
  print('making the call')
  
  # make the API call
  response = requests.get(f'https://api.unsplash.com/search/photos?page={page}&per_page=30&query={find}&client_id={key}').json()
  
  # returning the data in a comfortable format
  results = response['results']

  return [
    {'id':result['id'],
     'likes':result['likes'],
     'link':result['urls']['full'],
     'w':result['width'],
     'h':result['height']}
     for result in results]
  
def filterDesktopFormatPhoto(item):
    if item['w'] > item['h']: return True
    return False
    
def filterMobileFormatPhoto(item):
    if item['w'] < item['h']: return True
    return False
  
# sorts the photos after the ratio into 2 lists,
# first one - desktop format and the second one - mobile format
def sortIntoMobileAndDesktopFormat(data):
  return [list(filter(filterDesktopFormatPhoto, data)), list(filter(filterMobileFormatPhoto, data))]

# chooses n most liked photos
def getMostLiked(array, n, orientation):
    intial_array_length = len(array)
    result_array = []
    likes = [item['likes'] for item in array]
    while len(result_array) < n:
      if len(array) == 0:
        print('there are no ' + orientation + ' photos')
        break
      
      # get the index of the most liked photo
      index_of_most_liked_photo = likes.index(max(likes))
      
      # append the photo to the result_array
      result_array.append(array[index_of_most_liked_photo])
      
      # set its number of likes to 0
      likes[likes.index(max(likes))] = 0
      
      # checks if there were used all the photos and then break
      if len(result_array) == intial_array_length: break
      
    return result_array
import requests
import os

def download_image(fname, name):
  #Creating new folder for images
  os.makedirs('dog_images', exist_ok=True)
  print("Trying to download "+ fname)
  if fname:
      response = requests.get(fname)
      if response.status_code == 200:
          image_filename = os.path.join('dog_images', f'{name}.jpg')
          with open(image_filename, 'wb') as img_file:
              img_file.write(response.content)
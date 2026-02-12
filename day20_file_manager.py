import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO

url1 = ''
url2 = 'https://www.google.com'
url3 = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
url4='https://dog.ceo/api/breeds/image/random'
response = requests.get(url4)
print(response)
print(response.status_code)
# print(response.headers)
print(response.text)
data = response.json()
print(data['message'])
image_data=data['message']
image_data = requests.get(image_data).content

img = mpimg.imread(BytesIO(image_data), format='jpg')
plt.imshow(img)
plt.axis("off")  # hides the axis
plt.show()
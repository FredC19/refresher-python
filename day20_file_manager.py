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

from mypackage import arithmetic


print(arithmetic.subtract(5,3))


url5 = 'https://www.gutenberg.org/cache/epub/77911/pg77911.txt'
url6 = 'https://api.thecatapi.com/v1/breeds'

# response = requests.get(url5)
# the_json_data = response
# print(the_json_data)
# print(type(the_json_data.text))
# word3="word3"
# print(arithmetic.find_most_common_words(the_json_data.text,40))

min = 5
max = 5
total_average_weight = 0
average_weight_list=[]
cat_breed_response = requests.get(url6)
the_cat_data = cat_breed_response.json()
for catbreed in range(len(the_cat_data)):
    raw_weight_data = the_cat_data[catbreed]['weight']['metric'].split()
    average = (int(raw_weight_data[0])+int(raw_weight_data[2]))/2
    average_weight_list.append(average)
    if int(raw_weight_data[0])<min:
        min = int(raw_weight_data[0])
    if int(raw_weight_data[2])>max:
        max = int(raw_weight_data[2])

print(min,max)
median=average_weight_list[round((len(average_weight_list)/2))]
for x in average_weight_list:
    total_average_weight += int(x)
mean = total_average_weight/len(average_weight_list)
print(f"Median here: {median} and mean here: {mean}")
print(len(the_cat_data))


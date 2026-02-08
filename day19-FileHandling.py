import os
import json
# Syntax
# mode(r, a, w, x, t,b)  could be to read, write, update



f = open('random_file.txt')
txt = f.readline()
line2 = f.readline()
print(type(txt))
print(txt)
print(line2)
all_lines = f.read().splitlines()
print(type(all_lines))
f.close()

with open('random_file.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

with open('fileswriting_fileexample.txt','w') as f:
    f.write('This text will be written in a newly created file')

with open('fileswriting_fileexample.txt','a') as f:
    f.write('This text has to be appended at the end')

os.remove('fileswriting_fileexample.txt')

#more efficient way is

if os.path.exists('fileswriting_fileexample.txt'):
    os.remove('fileswriting_fileexample.txt')
else:
    print('The file does not exist')

# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])


person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)


import csv
with open('csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'{row[0]} is a teacher. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')



def read_speech(file_name):
    with open(file_name) as file:
        lines = file.read().splitlines()
        file.seek(0,0)
        words = file.read().split()
        print(f"Number of lines for this speech: {len(lines)}, and number of words is : {len(words)}, this is the speech for: {file_name}")
        file.seek(0,0)
        print(len(file.read()))


file_name_list = ['donald','obama','melina_trump','michelle_obama']

for f in range(len(file_name_list)):
    file_from_list = str(file_name_list[f] + '_speech.txt')
    if os.path.exists(file_from_list):
        read_speech(file_from_list)
    else:
        print(f"{file_from_list}: File does not exist")






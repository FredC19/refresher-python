import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I) #re.I tells the compiler to ignore if the match has caps
#or not
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0 15
substring = txt[start:end]
print(substring)       # I love to teach


txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first

#Instead of re.I to ignore caps
matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend python for a first programming language
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend python for a first programming language



txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(f"\n{matches}")

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol


regex_pattern = r'apple' # placing a r before the quote turns it from a string type to a regex type
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!

''''''''''''

regex_pattern = r'[n].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[A].+'  # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

''''''''

regex_pattern = r'[a].*'  # . any character, * any character zero or more times
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

''''''''''''

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']


''''''''''''

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] 

''''''

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']

''''''''

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
regex_search = r'[A-Za-z]+'
pattern_matches = re.findall(regex_search,paragraph)
print(pattern_matches)

highest_count = 0
highest_count_word = None 
for word in set(pattern_matches):
    regex_search = re.findall(word,paragraph)
    count=len(regex_search)
    if highest_count < count:
        highest_count = count
        highest_count_word = word

print(highest_count , highest_count_word)

#more efficient version

paragraph = ('I love teaching. If you do not love teaching what else can you love. '
             'I love Python if you do not love something which can give you all the '
             'capabilities to develop an application what else can you love.')

# Extract words
pattern_matches = re.findall(r'[A-Za-z]+', paragraph.lower())

# Count words manually
counts = {}
for word in pattern_matches:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

# Find the highest count
highest_count_word = None
highest_count = 0

for word, count in counts.items():
    if count > highest_count:
        highest_count = count
        highest_count_word = word

print(highest_count, highest_count_word)

sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
answer = sorted_points[-1] - sorted_points[0]
print(answer)

def is_valid_variable(name):
    pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    return bool(re.match(pattern, name))

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name') )# False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname') )# True


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(the_string):
    return re.sub('[^A-Za-z0-9;. !?]', '', sentence)
    
print(clean_text(sentence))
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
#print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]


pattern_matches = re.findall(r'[A-Za-z]+', sentence.lower())

# Count words manually
counts = {}
for word in pattern_matches:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

# Find the highest count
highest_count_word = None
highest_count = 0

for word, count in counts.items():
    if count > highest_count:
        highest_count = count
        highest_count_word = word

print(highest_count, highest_count_word)

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(sentence):
    return re.sub("[^A-Za-z0-9 .!?;]","",sentence)

print(clean_text(sentence))

def most_frequent_words(paragraph):
    word_list = re.findall(r'[A-Za-z]+',paragraph.lower())
    counts = {}
    for word in word_list:
        counts[word] = counts.get(word,0) + 1
    
    highest_word = max(counts, key=counts.get)
    highest_count = counts[highest_word]
    
    return highest_word, highest_count



    
print(clean_text(sentence))
cleaned_text = clean_text(sentence)
print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
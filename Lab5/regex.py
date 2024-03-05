import re

pattern1 = r"ab*"   #Ex1

pattern2 = r"ab{2,3}"   #Ex2

pattern3 = r"[a-z]+_[a-z]+" #Ex3

pattern4 = r"[A-Z][a-z]+"   #Ex4

pattern5 = r"a.*\b" #Ex5 

def match(pattern):

    with open("row.txt", "r", encoding="utf-8") as s:
        text = s.read()
        matches = re.findall(pattern, text)
        return matches

print(match(pattern1))


pattern = r"[ ,.]" #Ex6

text = "Text, for example."

result = re.sub(pattern, ":", text)

print(result)


text = "snake_case_example_string" #Ex7

snake = re.split(r"_", text)

s = snake[0]  
for i in range(1, len(snake)):
    s += snake[i].capitalize()  

print(s)


text = "TextForExample" #Ex8
def splitUp(s):
    return re.findall(r"[A-Z][a-z]+", text)

print(splitUp(text))


text = "TextForExample" #Ex9
def splitUp(s):
    words = re.findall(r"[A-Z][a-z]+", s)
    return " ".join(words)
print(splitUp(text))


text = "TextForExample" #Ex10

def camel_to_snake(camel_case):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()
    return snake_case

print(camel_to_snake(text))
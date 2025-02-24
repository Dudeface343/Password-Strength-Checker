
numbers = "1234567890"
numbers_backwards = "0987654321"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special =  " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


def nextCharacterPredictable(curr_char, next_char):
    if curr_char in numbers:
        curr_char_group = "number"
    elif curr_char in lowercase:
        curr_char_group = "letter"
    else:
        curr_char_group = "special"
        
    if next_char in numbers:
        next_char_group = "number"
    elif next_char in lowercase:
        next_char_group = "letter"
    else:
        next_char_group = "special"
        
    if curr_char_group == next_char_group and curr_char_group != "special":
        chars = curr_char + next_char
        if curr_char_group == "number":
            if chars in numbers or chars in numbers_backwards:
                return True
            else:
                return False
        elif curr_char_group == "letter":
            if chars in lowercase:
                return True
            else:
                return False
    else:
        return False


password = input("Type a password: ")

length = len(password)
score = length
multiplier = 0.0

for char in numbers:
    if char in password:
        multiplier += 0.5
        break
    
for char in lowercase:
    if char in password:
        multiplier += 0.5
        break
    
for char in uppercase:
    if char in password:
        multiplier += 0.5
        break
    
for char in special:
    if char in password:
        multiplier += 0.5
        break

predictable_chars = 0
char_group = "number"
prev_char_group = "number"

for i in range(length - 1):
    if nextCharacterPredictable(password.lower()[i], password.lower()[i + 1]):
        predictable_chars += 1
    else:
        if predictable_chars > 1:
            score -= predictable_chars
        predictable_chars = 0

score *= multiplier

print("score: " + str(score))

if (score < 8):
    print("WEAK")
elif (score < 15):
    print("MEDIUM")
elif (score < 20):
    print("STRONG")
else:
    print("VERY STRONG")

print("Welcome to English to Pig Latin translator")
name = raw_input("What's your name? ")
original = raw_input("What would you like to translate? ")

if len(original) > 0 :
    if original.isalpha():
        pyg = "ay"
        word = original.lower();
        first = word[0]
        if first == "a" or first == "e" or first == "i" or first == "o" or first == "u" :
            new_word = word + pyg
        else :
            new_word = word[1:len(word)] + word[0] + pyg
        print("Hello " + name + ". You're translated word is " + new_word)
    else :
        print("Input must only contain letters")
else :
    print("Input can't be empty")

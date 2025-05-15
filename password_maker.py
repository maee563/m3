import easygui, random

Welcome = easygui.msgbox ("Welcome to the Password maker!")

# lists to use for passwords
nouns = ["cat", "hat", "earpods"]
adjective = ["grumpy", "quiet", "loud"]
number = ["0", "12", "14", "15", "16"]


password = easygui.buttonbox ("Would you like to create a password?", "Another password", choices=["Yes", "No"])

while password == "Yes":
    noun_1 = random.choice (nouns)
    adjective_1 = random.choice (adjective)
    number_1 = random.choice(number)
    anotherpassword = (noun_1 + adjective_1 + number_1)
    easygui.msgbox (anotherpassword)
    password = easygui.buttonbox ("Would you like to create another password?", "Another password", choices=["Yes", "No"])

if password == "No":
    easygui.msgbox ("That's okay! Thank you for using password making.")



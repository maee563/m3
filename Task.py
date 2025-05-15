import easygui

name_1 = easygui.enterbox ("What is your name?")
age_1 = easygui.integerbox ("How old are you?")

while age_1 == "15 - 18" :
    question_1 = easygui.choicebox("Which of these words means under in te reo?", "Question 1", choices=["runga","raro", "roto", "waho"])
    question_2 = easygui.choicebox("What is an english word for pukapuka?", "Question 2", choices["book", "table", "clock", "wall"])
if age_1 == ">15" :
    easygui.msgbox ("Sorry but this program isn't for you. Thank you for your time though!")
print (name_1)

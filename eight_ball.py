import random

#The magic eight ball will intake questions from an end-user and then using the random function, the eight ball will give 
#a pre-determined response at random. The end-users will be prompted for their name and then the adventure will begin after 
#they agree to not sue anyone for the advise of an inadament object, because 'Merica. The user will be able to ask up to eight 
#questions. Should they reach the threshold of eight, magic eight ball will direct them to their local therapist for further 
#advice. 

def magic():

    user_name = input("What is your name trustworthy soul? ")

    welcome_message = f"\nWelcome to the cave of wonders {user_name.title()}, \n\nAlso known as your living room couch. I am no genie, but I" \
    " may be able to guide you along your path. Helping you to decide if you should marry that one night stand, you met in" \
        " the bathroom while on your girls trip to Tijuana. \n\nFor legal purposes, my legal department would like me to inform" \
        " you, I am a toy, and this is for entertainment purposes only. Please don't ascribe to me any form of divinity. It will give my" \
            " creator Teddie a God complex."

    print(welcome_message)

    legal_response = input("\nTo continue, please enter 'yes' to agree to not sue me if you use my advice and it ruins your life: ")
    questions = ["Ask me, Magic Eight Ball, or Q-Tip as I prefer to be called, anything you'd like."]

    if legal_response == 'yes':
        print(f"Let the crazy advice and games begin, {user_name.title()}!")
    else:
        print(f"We are sad to see you go but oh so happy you cannot sue us {user_name}!")

    magic_eight_ball_response = ["Who do I look like, your mom?", "I think that is something you shoudl ask your therapist.",
    "You know I'm not real right?", "Yes, absolutely, do it right now, and if that makes no sense in context what I really meant was no",
    "What would your grandmother think?", "I'm slightly worried that you're leaving that decision to me? Like Linda, listen.",
    "Yes, yes, I think you should ask her out.", "Ask again never.", "No, I do not hate you Kevin. I just feel the same as your mother.", 
    "You only get one life - do what makes you feel content, safe, and proud.", "Of course I'm your friend.", "Yes, yes, I will hug you",
    "Yes, do it, becuase if you asked it means that a part of your wants too, so what's stopping you."]


    questions_asked = 0

    fortune_telling = True

    while fortune_telling:
        if questions_asked >= 8:
            print(input("Are you okay? "))
            if input == "yes" or "no":
                print("I don't believe you. Might be best to seek the advice of a professional human.")
                break
        
        user_questions = input("What would you like to aks me? ")
        questions_asked += 1
        computer_input =  (random.choice(magic_eight_ball_response))
        print(f"{computer_input}\n")

        if user_questions == 'quit':
            print(f"See you during your next life crisis {user_name.title()}!")
            fortune_telling = False

    return "\nTrauma was brought to you today by capitalism."

print(magic())



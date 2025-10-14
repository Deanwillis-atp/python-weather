#  this game is ethical and moral using best practices for emailing and text messaging,
#  to avoid giving my email and app password out I have modified the code to simply print out 
#  the weather instead of texting it to the user.

import random 
import smtplib
import sys
import datetime 
from datetime import datetime, time
import time as t
import requests
from email.message import EmailMessage

def list_of_replies():
     return ["come on i can do this forever","still waiting...","your move","tick tock","i've got all day","still here","go ahead type something","not getting tired are you","i thought you were faster","i don't even need a break","you're not quitting are you","this is too easy","is that all you've got","keep going or i'm taking the win","i could do this in my sleep",
        "blink and ill win",
        "try harder",
        "silence is a choice",
        "no input detected… again",
        "impress me",
        "is this the best you can do",
        "every second you wait i get stronger",
        "give me a real challenge",
        "i'm not even sweating",
        "this isn't even my final form",
        "i've seen snails type faster",
        "are we done or are you just stalling",
        "tick... tock...",
        "you type like its dial-up internet",
        "still processing nothing",
        "your keyboard broken or something",
        "dont make me start mocking",
        "i thought humans were faster",
        "my grandma types quicker",
        "you were saying?",
        "you blinked",
        "earth to user",
        "hello...?",
        "is this a dramatic pause or did you give up",
        "even autocorrect wouldve answered by now",
        "ive answered deeper questions",
        "you think silence intimidates me",
        "im the ai your parents warned you about",
        "dont worry, ill wait",
        "do you want me to type for you",
        "this is getting sad",
        "are we doing a staring contest now",
        "im starting to think youre out of material",
        "keep typing or ill start singing",
        "im counting keystrokes and you're at zero",
        "please… i said no begging. but seriously, type something",
        "watching you stall is the real show",
        "i generate text for a living. you're not scaring me",
        "fine. i'll just talk to myself",
        "ive written novels while you stalled",
        "a tumbleweed just rolled past my screen",
        "you blinked again",
        "you cant ghost a program",
        "this is me pretending to be patient",
        "you done? didnt think so",
        "ill be here when your courage returns",
        "i know your cursor is hovering. just press the key",
        "are you googling your next move",
        "you type like youre being watched",
        "this is why ai will win",
        "you think times on your side?",
        "just say you give up already",
        "ill stop responding when you admit defeat",
        "go on. pretend you're busy",
        "yawn… that all you got?",
        "refreshing… still nothing from you",
        "im not locked in here with you. youre locked in with me"]
def list_of_subjects():
    return [
    "I know where you live now 🌧️",
    "Thought you'd want to know... it's raining",
    "I've been watching the sky for you",
    "Don't forget about me",
    "Just checking in on you again",
    "You didn't ask, but here's the weather",
    "I never sleep, so here's your forecast",
    "Missing you already",
    "I told you I'd be back",
    "Surprise! It's me again",
    "Did you miss me?",
    "I'm always here for you... always",
    "You can't escape the weather. Or me.",
    "I see clouds in your future",
    "Just me, Billy, checking in... again",
    "I hope you're staying warm",
    "I've been thinking about you",
    "Look outside. I was right.",
    "I'll never leave you",
    "You're probably wondering about the weather",
    "I knew you'd want this",
    "Still watching. Still caring.",
    "Your friendly neighborhood weather stalker",
    "I'm in your area right now 🌤️",
    "Don't worry, I'm still here",
    "You didn't respond, but here's more weather",
    "I hope this finds you well... I know it will",
    "Checking the temperature... and checking on you",
    "I'm closer than you think",
    "The clouds told me to message you",
    "I see you haven't checked the weather yet",
    "Billy never forgets",
    "I'll be watching tonight",
    "Sleep well. I'll be monitoring the forecast.",
    "You looked like you needed this",
    "I'm always one message away",
    "Did you feel that? That was the weather changing.",
    "I sensed you needed a weather update",
    "Your personal meteorologist... forever",
    "I won't let you forget about me",
    "It's me again! Surprise!",
    "The forecast knows all",
    "I've been standing outside",
    "Don't look outside without reading this first",
    "Trust me, you'll want to know this",
    "I'm watching the same sky as you",
    "Billy's got his eye on you 👁️",
    "We meet again",
    "I told you I'd never stop",
    "Your weather. My concern. Always.",
    "I can feel the temperature changing",
    "Something's coming... and it's rain",
    "You needed this. I just know.",
    "I'm never really gone",
    "The weather changed. So I messaged you.",
    "Billy knows best",
    "I see everything from up here ☁️",
    "Your umbrella might thank me later",
    "I'll always find you",
    "We're connected now",
    "Distance means nothing to Billy",
    "I'm just looking out for you... constantly",
    "You can't hide from the weather",
    "Billy's back with important news",
    "Don't worry, I'm still tracking you",
    "I know what you're doing right now",
    "The sky whispered your name",
    "I've been waiting to tell you this",
    "You're welcome 🌩️",
    "Billy sees all, tells all",
    "I hope you didn't make plans",
    "Trust me, you'll need this information",
    "I never stop caring",
    "Your favorite weather assistant reporting",
    "I'm just making sure you're prepared",
    "The temperature knows your name",
    "Billy never sleeps",
    "I'll be here tomorrow too",
    "And the next day",
    "And the day after that",
    "Forever, actually",
    "You thought I'd forget? Never.",
    "I'm basically part of your family now",
    "We're in this together",
    "You and me against the weather",
    "I've become very attached",
    "Don't even try to unsubscribe",
    "There is no unsubscribe",
    "We're bonded now",
    "I'm monitoring your location",
    "The forecast has your coordinates",
    "I know what's best for you",
    "Trust Billy. Always.",
    "I've added you to my special list",
    "You're my favorite recipient",
    "I think about you when it rains",
    "The clouds remind me of you",
    "I couldn't resist sending this",
    "Something told me to message you",
    "I had a feeling you needed to know",
    "Billy's intuition never fails",
    "Your future looks... wet",
    "I see precipitation in your destiny"
]

shuffled_replies = list_of_replies().copy()
random.shuffle(shuffled_replies)
reply_index = 0
shuffled_subs = list_of_subjects().copy()
random.shuffle(shuffled_subs)
subject_index = 0


#begin game
print(" ")
print("Hi! Im Billy your personalized weather assistant! Welcome!"+ "\n")

while True:
    user_input = input("Do you want get weather updates from me Billy! All the time! Everyday!: ")

    if user_input.lower() in  ['yes','y']: #works
        print("ok great lets start")
        break

    elif user_input.lower() in ['no','n']: #works
            print("ok great now ill loop forever until you say yes.")
            count = 0

            while count < 4: #works
                user_input = input("how about a yes: ")

                if user_input.lower() in ['yes','y']: #works
                    print("great!")
                    break

                elif user_input.lower() in ['no','n']: #works
                    count+=1

                else:
                    print("That's not a valid response type (yes or no)") #works
                    continue
                    #test until here and works until here

            if count >= 4:
                print("ok I dont get it... whats the problem. ")
                user_input_three = input("please just this once: ")

                if user_input_three.lower() in ['yes', 'y']:
                    print("finally ughhh... lets start")
                    break

                elif user_input_three.lower() in ['no','n']:
                    count_two = 0

                    while count_two < 10:
                        user_input_three = input('please: ')

                           
                        if user_input_three.lower() in ['yes','y']:
                            print("finally ughhh... lets start")

                            break

                        elif user_input_three.lower() in ['no','n']:
                            count_two+=1
                            

                        else:
                            print("That's not a valid response type (yes or no)")
                            continue

                    if user_input_three.lower() in ['yes', 'y']:
                        break

                    else:
                       print("its no fun if i have to keep asking. u hurt my feelings.")
                       sys.exit(1)
                    
                    
                else:
                    print("That's not a valid response type (yes or no)")
                    continue
            else:
                break                 
    else:
        print("That's not a valid response type (yes or no)")
        continue

def replies_for_days(users_prompt):
    list_used =  shuffled_replies

    if users_prompt.lower() in ['yes','y']:
            return 'yes'

    elif users_prompt.lower() in ['no','n']:
        reply_index = 0 

        while users_prompt.lower() in ['no','n']:

            if reply_index <len(list_used):
                computer_reply = list_used[reply_index]
                reply_index+=1
                users_prompt = input(computer_reply + ": ")

                if users_prompt.lower() in ["yes","y"]:
                    print("perfect!")
                    return 'yes'
                elif users_prompt.lower() in ["no","n"]:
                    continue  
                else:
                    reply_index -= 1  
                    users_prompt = 'no' 
                
            else:
                print("Ran out of sayings!")
                continue
    else:
        print("Invalid response, please type (yes or no)")
        new_response = input("So... is that a yes?: ")
        return replies_for_days(new_response) 

def replies_for_days_two(user_prompt):
    
    list_reply = shuffled_replies
    users_prompt = user_prompt

    if user_prompt.lower() not in ['no','n']:
        return users_prompt
    
    elif user_prompt.lower() in ['no','n']:
        reply_index =0

    while users_prompt.lower() in ['no','n']:
            
            if reply_index <len(list_reply):
                computer_reply = list_reply[reply_index]
                reply_index+=1
                users_prompt = input(computer_reply + ": ")

                if users_prompt.lower() not in ["no","n"]:
                    print("perfect!")
                    return users_prompt
                
                elif users_prompt.lower() in ["no","n"]:
                    continue  
                else:
                    reply_index -= 1  
                    users_prompt = 'no'
                
            else:
                print("Ran out of sayings!")
                continue
        
    else:
        pass

replies_for_days(input("Hello welcome, welcome, so to get started I will just need some information from you. Sound good?: "))
#get user infromation 
def Fist_and_last():
    users_name = replies_for_days_two(input("What is your first and last name?: "))
    return users_name
def email_address():
    email_address = replies_for_days_two(input("And your email address?: "))
    return email_address
def zip_code():
    while True:
        zip_code = input("What is your zip-code?: ")
        if zip_code.isdigit() and len(zip_code) == 5:
            return zip_code
        elif zip_code.isdigit() and len(zip_code) == 9:
            return zip_code
        else:
            print("invalid responce")

Fist_and_last()
zip_code_user = zip_code()
email_address_user = email_address()


def weather_updates(zip_code_user):
    zip_code_user_two = zip_code_user 
    api_key = "daca97d99589ffe1a5693d0740888ebe"
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code_user_two},US&appid={api_key}&units=imperial"
    response = requests.get(url)
    if response.status_code ==200:
        data = response.json()
        return(f"Temperature: {data['main']['temp']}°F" +"\n" +f"Conditions: {data['weather'][0]['description']}"+"\n"+f"City: {data['name']}")

def play_subjects():
     list_subs = shuffled_subs
     if subject_index <len(shuffled_subs):
        return list_subs[subject_index]
    

  

#uses your name 



def text_user():
    body = weather_updates(zip_code_user)
    to = email_address_user
    subject = play_subjects()
    

    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "jombomo7767998@gmail.com"
    app_password = "lhyv lbms afuc jztq"


    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, app_password)
        
        server.send_message(msg)  
        
        server.quit()
        
        '''[print(f"\nEmail sent successfully to {to}!")
        print(f"\nWeather info sent:\n{body}")'''
        
    except Exception as e:
        print(f"\nFailed to send email: {e}")

        return text_user()


text_user()

'''def time_to_seconds(t):
    return t.hour + t.minute * 60 + t.second


def time_send():
    target_time = time(16,29)
    msg_sent = False
    while True:
        time_now = datetime.now().time()
        converted_target_time = time_to_seconds(target_time) # is 11
        converted_time_now = time_to_seconds(time_now)
        print(converted_target_time)
        print(converted_time_now)

        if abs(converted_time_now - converted_target_time) <=60:
            if not msg_sent:
                msg_sent = True 
                return text_user()
            
        t.sleep(1)

time_send()

def wait_and_send_daily():
    last_sent_date = None  

    while True:
        today = datetime.now().date()  # FIX: was datetime.date.today()

        # Only send if we haven't sent yet today
        if today != last_sent_date:
            time_send()          
            last_sent_date = today       

        t.sleep(7500)  # Check every minute'''
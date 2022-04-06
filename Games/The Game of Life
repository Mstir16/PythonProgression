# its pretty bad XD first python thing!
from pyfiglet import Figlet
from random import randint
import time
import os
os.system('cls')

c_text = Figlet(font="slant")

print(c_text.renderText("The Game Of Life"))
print("(turn on capslock for best experience)\n\n")
time.sleep(3)
print('Choose your Gender')
time.sleep(1)

stats = {
    "isgirl": False,
    "karmalvl": 0,
    "bbygender": randint(1,2),
    "idkgen": False,
    "Health": 100,
    "chosenToy": None,
    "Graduated": False,
    "Dropout": False,
    "CS": False,
    "RE": False,
}

curgender = input("""
---------------------
[B] - Boy
[G] - Girl
[IDK] - i don't know yet bruh
---------------------\n\n""")

if curgender == "B":
    curgender = "Boy"
    print(curgender+" Selected")
    time.sleep(1)
elif curgender == "G":
    curgender = "Girl"
    stats["isgirl"] = True
    print(curgender+" Selected")
    time.sleep(1)
elif curgender == "IDK":
    stats["idkgen"] = True
    randomgender = randint(1,2)
    print('You are discovering yourself!')
    time.sleep(1)
    if randomgender == 1: curgender = "Boy"
    elif randomgender == 2: curgender = "Girl"
    print('But you were born as a '+curgender)

os.system('cls')
print(c_text.renderText("Womb"))


startlife = input("""
Are you sure you want to start your life? It might be shit.
[Y] - Yes
[N] - No XD
\n\n
""")

if startlife == "Y":
    print('Good luck young one.')
    time.sleep(1)
elif startlife == "N":
    print('You commit suicide while still in the womb')
    time.sleep(0.5)
    print(c_text.renderText("YOU DIED"))
    time.sleep(2)
    os.system('cls')
    exit()

os.system('cls')
print(c_text.renderText("Birth"))

print('You now see a bright light in the distance.')
time.sleep(1)
print('you get closer to it.')
time.sleep(1)
print('You are now in the presence of your mother and father')
time.sleep(1)
print('they start making faces at you what will you do.\n')
actionbirth = input("""
---------------------
[S] - Spit at them
[P] - Poke
[C] - Cry
---------------------\n\n""")

if actionbirth == "S":
    print('You tried to spat at your parents.')
    time.sleep(1)
    print("But it didn't go far, you spat on yourself.")
    time.sleep(1)
    print('You cry anyways.')
elif actionbirth == "P":
    print('Your dad got close to make faces')
    time.sleep(1)
    print('You poked him in the eye.')
    time.sleep(1)
    print('it hurt alot for him')
    stats["karmalvl"] += 1
elif actionbirth == "C":
    print('You cried like a little bitch.')
    time.sleep(1)
    print('Your parents embraced you.')

input("\n--press enter to continue--\n")
os.system('cls')
print(c_text.renderText("Home"))

print("You are brought back home.")
time.sleep(1)
print("There are toys everywhere, what are you playing with?")
time.sleep(1)
actionHome = input("""
---------------------
[C] - Vroom Vroom
[D] - RAWRRRRRRRRRR
[S] - Big Stick
---------------------\n\n""")

if actionHome == "S":
    print('You pick up the big stick')
    time.sleep(1)
    print('You swing it around.')
    time.sleep(1)
    print('Its so fun!')
    time.sleep(1)
    print('but you break something')
    if stats['karmalvl'] == 1:
        print('Your parents sigh')
        stats['karmalvl'] += 1
if actionHome == "D":
    print('You pick up the dinosaur')
    time.sleep(1)
    print('You destroy your lego set with pride.')
if actionHome == "C":
    print('You pick up the car')
    print('You wind-up the nob')
    print("It goes away, But doesn't come back")
    print('You cry like a bitch.')

input("\n--press enter to continue--\n")
os.system('cls')
print(c_text.renderText("Home"))

print('(Timeskip, You are now age 2)')
stats['Health'] -= 2
time.sleep(1)
print('You are learning how to walk!')
time.sleep(1)
print('Your parents are waiting for you on the otherside of the hallway')
time.sleep(1)
print('What will you do?')
actionWalking = input("""
---------------------
[S] - sit
[W] - walk
[R] - run
---------------------\n\n""")

if actionWalking == "S":
    print('You sit your fat ass down.')
    time.sleep(1)
    if stats["karmalvl"] == 1:
        print('Your parents have a short chuckle.')
        stats["karmalvl"] += 1
    elif stats["karmalvl"] == 2:
        print('Your parents are getting annoyed..')
        stats["karmalvl"] += 1
    else:
        print('Your parents look at you, then laugh.')

elif actionWalking == "W":
    print('You try your best to balance and walk')
    time.sleep(1)
    print('You successfully make it!')
    time.sleep(1)
    print('Your Parents are happy.')

elif actionWalking == "R":
    print('Instead of Walking, You attempt to run.')
    time.sleep(1)
    print('Getting halfway there...')
    time.sleep(1)
    print('You fall and gash your head a bit')
    time.sleep(1)
    print('You go to the doctor.')
    time.sleep(1)
    print('The doctor says it will cut your lifespan')
    time.sleep(1)
    print('But he can fix the gash in the head!')
    stats['Health'] -= 10
    time.sleep(1)
    print('You return home with a lolipop')

input("\n--press enter to continue--\n")
os.system("cls")
print(c_text.renderText("Kindergarden"))

print('(Timeskip, You are now age 5)')
stats['Health'] -= 3
time.sleep(1)
print('You are preparing for your first day of kindergarden!')
time.sleep(1)
print('Your parents tell you to pick a toy to take.')
time.sleep(1)
print('ONLY ONE, what are you taking?')
actionKinderStart = input("""
---------------------
[B] - Buzz Lightyear
[W] - Woody
[A] - Both
---------------------\n\n""")

if actionKinderStart == "B":
    print("You grab Buzz")
    stats["chosenToy"] = "Buzz Lightyear"
elif actionKinderStart == "W":
    print('You grab Woody')
    stats["chosenToy"] = "Woody"
elif actionKinderStart == "A":
    print('You take both.')
    time.sleep(1)
    print("You think you're slick. But get caught")
    time.sleep(1)
    print("You take nothing.")

input("\n--press enter to continue--\n")
os.system("cls")
print(c_text.renderText("Show & Tell"))

print('Turns out the first day was show and tell.')
if stats['chosenToy'] == None:
    print('But you chose to be greedy.')
    time.sleep(1)
    print('Now you have nothing to show!')
else:
    print('Luckily you brought '+stats["chosenToy"])
    time.sleep(1)
    print('You talked about how cool he is.')

input("\n--press enter to continue--\n")

os.system("cls")
print(c_text.renderText("4th Grade"))

print('(Timeskip, You are now age 9)')
stats['Health'] -= 4
time.sleep(1)
print('Two bullies push you against your locker')
print('what will you do?')
action4thBully = input("""
---------------------
[F] - Fight Back
[L] - Let it happen
[R] - Run
---------------------\n\n""")

if action4thBully == "L":
    print('You let it happen.')
    time.sleep(1)
    print('the bullies beat the shit out of you')
    time.sleep(1)
    print('your body is smeared against your locker with your blood')
    time.sleep(1)
    print('you are left there to die...')
    time.sleep(1)
    stats['Health'] = 0
    print(c_text.renderText("YOU DIED"))
    print("Could've done something lol")
    time.sleep(2)
    os.system('cls')
    exit()
if action4thBully == "F":
    print('You choose to fight back!')
    time.sleep(1)
    print('Meanwhile fighting, Security comes!')
    time.sleep(1)
    print('You are sent to detention!')
    time.sleep(1)
    print('You have some minor internal injuries.')
    stats['Health'] -= 5
elif action4thBully == "R":
    print('You run! (wow pussy)')
    time.sleep(1)
    print('You escape without a scratch!')

input("\n--press enter to continue--\n")

os.system("cls")
print(c_text.renderText("Growing up?"))

print('(Timeskip, You are now age 14)')
stats['Health'] -= 5
time.sleep(1)
print('You are seeing pimples on your face')
print('what will you do?')
action14yr = input("""
---------------------
[P] - Pop it like bubble wrap
[N] - nothing
---------------------\n\n""")

if action14yr == "P":
    print("You pop your pimples")
    time.sleep(1)
    print("A liquid starts oozing.")
    time.sleep(1)
    print('EW!')
elif action14yr == "N":
    print('You did absolutely nothing lol')

input("\n--press enter to continue--\n")

os.system("cls")
print(c_text.renderText("Graduation"))

print('(Timeskip, You are now age 17)')
stats['Health'] -= 3
time.sleep(1)
print('You are at graduation')
time.sleep(1)
print('What will your speech be about?')
actiongrad = input("""
---------------------
[H] - How hard life was
[E] - How easy it is XD
---------------------\n\n""")

if actiongrad == "H":
    print('You speak about how hard life was.')
    time.sleep(1)
    print('everyone pitys you.')
elif actiongrad == "E":
    print('You talk about how easy it is')
    time.sleep(1)
    print('everyone hates you.')

input("\n--press enter to continue--\n")
os.system("cls")
print(c_text.renderText("The Park"))

print('After graduation, you head to the park')
time.sleep(1)
print('You then see your 4th grade bully')
time.sleep(1)
print('What do you want to do...')
actionpark = input("""
---------------------
[A] - Attack
[N] - Nothing
---------------------\n\n""")

if actionpark == "A":
    print('You chose to attack your bully')
    time.sleep(1)
    print("They're sight seeing, then you jumped them")
    time.sleep(1)
    print('You punched them repeatedly')
    time.sleep(1)
    print('They died from their injuries...')
    stats["karmalvl"] += 2
elif actionpark  == "N":
    print('You chose to do nothing.')
    time.sleep(1)
    print('it probably was for the best..')

input("\n--press enter to continue--\n")
os.system("cls")

print(c_text.renderText("College"))

print('(You start College. At age 19)')
time.sleep(1)
print('You are picking your classes.')
time.sleep(1)
print('What are you going to major in')
time.sleep(1)
actioncollege = input("""
---------------------
[C] - Computer Science
[H] - Health/Human Body
[D] - Dropout
---------------------\n\n""")

if actioncollege == "C":
    print('You decided to major in Computer Science')
    stats['CS'] = True
elif actioncollege == "H":
    print('You decided to major in Human Physiology')
    stats["RE"] = True
elif actioncollege == "D":
    stats["Dropout"] = True
    print('You decided to dropout of college')
    time.sleep(1)
    print('Why?')

input("\n--press enter to continue--\n")
print(c_text.renderText("Four Years Later.."))
stats['Health'] -= 4

if stats["Dropout"] == True:
    print('For the next 4 years you did nothing')
    time.sleep(1)
    print('While your friends went to college...')
    time.sleep(1)
    print('nice one..')
elif stats['Dropout'] == False:
    print('You graduated with your Bachelors!')

input("\n--press enter to continue--\n")
os.system("cls")

print(c_text.renderText("Finding a Job"))

if stats['Graduated'] == True:
    print("With your Bachelors, its time to pick a job")
elif stats['Dropout'] == True:
    print('With your Diploma, its time to pick a job')
time.sleep(1)

if stats['RE'] == True:
    print('Since your major is Human Physiology')
    time.sleep(1)
    print('You settled with a job at a hospital')
    time.sleep(1)
    print('That pays 60k a year')
elif stats['CS'] == True:
    print('Since your major is Computer Science')
    time.sleep(1)
    print('You settled with a corporation named Stame')
    time.sleep(1)
    print('That pays 85k a year')

input("\n--press enter to continue--\n")
os.system("cls")

print(c_text.renderText("A problem!"))

print('(Timeskip! You are age 27)')
stats["Health"] -= 4
time.sleep(1)
print('You are walking out the grocery store')
time.sleep(1)
print('When you see that a lady is being robbed at gunpoint!')
time.sleep(1)
print('What do you do?')
actionproblem1 = input("""
---------------------
[C] - Call the cops
[I] - Intervene
[R] - Run away
---------------------\n\n""")

if actionproblem1 == "C":
    print('You call the cops!')
    time.sleep(1)
    print('The robber with a gun sees you')
    time.sleep(1)
    print('They shoot..')
    time.sleep(1)
    print(c_text.renderText("YOU DIED"))
    time.sleep(2)
    os.system('cls')
    exit()
elif actionproblem1 == "R":
    print('You run out of there!')
    time.sleep(1)
    print('The robber with a gun sees you')
    time.sleep(1)
    print('They shoot..')
    time.sleep(1)
    print(c_text.renderText("YOU DIED"))
    time.sleep(2)
    os.system('cls')
    exit()
elif actionproblem1 == "I":
    print('You intervene!')
    time.sleep(1)
    print('The robber with a gun sees you')
    time.sleep(1)
    print('He takes you down to the ground')
    time.sleep(1)
    print('He puts a gun to your head')
    time.sleep(1)
    print('He tells you to shoot the lady...')

input("\n--press enter to continue--\n")
os.system("cls")

print(c_text.renderText("A problem!"))

print('What are you going to do...')

actionproblem2 = input("""
---------------------
[S] - Shoot the Lady
[L] - Let the robber end you.
[T] - Try to struggle
---------------------\n\n""")

if actionproblem2 == "S":
    print('The lady looks at you in horror')
    time.sleep(1)
    print('You shoot the lady..')
    time.sleep(1)
    print('The robber applauds you')
    time.sleep(1)
    print("They say: It's your turn now..")
    time.sleep(1)
    print(c_text.renderText("YOU DIED"))
    time.sleep(2)
    os.system('cls')
    exit()
if actionproblem2 == "L":
    print('You close your eyes and relax yourself.')
    time.sleep(1)
    print('You put your hands up')
    time.sleep(1)
    print('You hear the lady shout')
    time.sleep(1)
    print('You hear the gun struggle')
    time.sleep(1)
    print('Two shots go off..')
    time.sleep(1)
    print('The robber is dead and the lady is bleeding out..')

input("\n--press enter to continue--\n")
os.system("cls")

print(c_text.renderText("A problem!"))

print('The lady is bleeding out what will you do..')

actionproblem3 = input("""
---------------------
[S] - Call 911
[P] - Perform first-aid
[K] - Put her out of her misery
---------------------\n\n""")

if actionproblem3 == "S":
    print('You call 911.')
    time.sleep(1)
    print('The ambulance arrives..')
    time.sleep(1)
    print('The lady is pronounced dead.')
elif actionproblem3 == "K":
    print('You decide to put the lady out of her misery..')
    time.sleep(1)
    print('The lady is surprised and starts to hit you in the end')
    time.sleep(1)
    print('You raise the gun and pull the trigger..')
    time.sleep(1)
    print('You animal...')
    stats["karmalvl"] += 3
    if stats["karmalvl"] > 5:
        print('You go insane..')
        time.sleep(1)
        print('And you kill yourself')
        time.sleep(1)
        print('Your insanity is too much..')
        time.sleep(1)
        print('You got the..')
        time.sleep(2)
        print(c_text.renderText("MANIAC ENDING"))
        exit()
elif actionproblem3 == "P":
    print('You try to perform first aid')
    if stats['RE'] == False:
        print("But you didn't study Human Physiology..")
        time.sleep(1)
        print('The lady still dies..')
    else:
        print('You are able to get her to steady her breathing')
        time.sleep(1)
        print('You then call 911')
        time.sleep(1)
        print('The ambulance arrives')
        time.sleep(1)
        print('The lady makes a full recovery')
        time.sleep(1)
        print('You are pronounced a hero in your town!')
        time.sleep(1)
        print('And receive a cash prize of')
        time.sleep(1)
        print('1.5 million dollars!')
        time.sleep(1)
        print('You got the..')
        time.sleep(2)
        print(c_text.renderText("HERO ENDING"))
        exit()

print('You quit your job..')
time.sleep(1)
print('And retire..')

input("\n--press enter to continue--\n")
os.system("cls")

print(c_text.renderText("Mid Life Crisis"))

print('(Timeskip, you are now age 35)')
stats["Health"] -= 7

print('You are annoyed with yourself')
time.sleep(1)
print("You could've done something..")
time.sleep(1)
print("But you didn't")
time.sleep(1)
print('Make a decision for yourself... now')
actionmidlifecrisis = input("""
---------------------
[S] - Start something new...
[K] - Kill yourself
---------------------\n\n""")

if actionmidlifecrisis == "K":
    if stats['karmalvl'] > 1:
        print('You can feel all the sins you commited')
        time.sleep(1)
        print('So only one way to pay for those sins')
        time.sleep(1)
        print('You fire the gun..')
        time.sleep(1)
        time.sleep(1)
        print('You got the..')
        time.sleep(2)
        print(c_text.renderText("SORROW ENDING"))
        exit()
    print('You shoot yourself.')
    time.sleep(1)
    print('For the pain of others.')
    time.sleep(1)
    print('You got the..')
    time.sleep(2)
    print(c_text.renderText("BAD ENDING"))
    exit()

if actionmidlifecrisis == "S":
    print('You decide to start something new..')
    time.sleep(1)
    print('To be continued...')
    time.sleep(1)
    print('You got the..')
    time.sleep(2)
    print(c_text.renderText("NORMAL ENDING"))
    exit()

# Tell me what u think on my discord bily#8072
# Just friend me
# This python project is a game
# I tried to make this in java but I took a break
# and forgot my code structure

# fellow programmers learn from my mistake
def tutorial ():
  print(f"Welcome to the tutorial /n If you want to see what commands you can type type opt\n That will show you your options \n If you want to see your stats type stats\n and if you want to see your weapon stats type the weapons name and its stats")

input("At the end of these if you see / hit enter/")
input("When you see : at the end I want you to type something/")
name = input("What is your name: ")
print(f"Welcome {name}")

print("")
tutOrN = input(f"{name} This is adventure game would you like to go through \nthe tutorial? If so type t else just hit enter: ")

if (tutOrN == "t"):
  tutorial()
else:
  print(" ")
input("Are you ready to start? /")

input("Welcome to Gothland this city is known for being racist/")
input("You have come from the city of Hothland and are coming here to fight racism/")

input("It is now in the story you choose your race and class/")

print(
  "Here are all of the races there is... \n" +
  "1.) Goblin: Type g to pick \n" +
  "2.) Warlock: Type w to pick \n" +
  "3.) Human: Type h to pick \n" +
  "\n" +
  "These are your choices pick wisely..."
)
race = input("race: ")

if (race=="g"):
  input("You've chosen goblin\n" +
  "These creatures are hated in the city/"
  )
if (race=="w"):
  input("You have chosen Warlock smart..." +
  "These creatures are very repected in the city/")
if (race=="h"):
  input("You have chosen human this creature" +
  "Is banned from the city for being your kind trying to destroy racism/"
  )


print("DM: You are riding on a hourse on your way to the city as you go you have a \nconversation with the rider/")
namee = input("Rider: Wats ur name?\n :  ")

input("Rider: Nice to meet ye i'm grant")

if (race=="g"):
  input(f"Grant: ye might wanna keep your head down you know as a goblin.../")
if (race=="h"):
  input("Grant: Just lettin ye know ur kinda banned from the city so ill take you close\n"+ 
  "im not gonna take ye thru the gates/"
  )
input(f"DM: He takes you to the front gated and says(good luk {namee})/")

readyToApproachGate = input("DM: Are you ready to get to the gate?(yes,no) : ")

if (readyToApproachGate=="yes"):
  input("OK lets go")
else:
  input("Too bad")

def goblinPortionGates():
  print("DM: ")


class Colors:
    yellow = '\u001b[33m'
    green = '\u001b[32m'
    blue = '\u001b[34m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


# Functions called from Mad_Libs.py; inserts user-input lists and prints a short story.
def ml_0(noun, verb, adjective):
    ml_0_string = (
        f"\nToday, every student has a computer small enough to fit into his or her "
        f"{Colors.yellow}{str(noun[0])}{Colors.reset}.\nHe or she can solve any math problem by simply pushing "
        f"the computer's little "
        f"{Colors.yellow}{str(noun[1])}{Colors.reset}.\nComputers can add, multiply, divide, and "
        f"{Colors.green}{str(verb[0])}{Colors.reset}.\nThey can also "
        f"{Colors.green}{str(verb[1])}{Colors.reset} better than a human. Some computers are "
        f"{Colors.blue}{str(adjective[0])}{Colors.reset}.\nOthers have a/an "
        f"{Colors.blue}{str(adjective[1])}{Colors.reset} screen that shows all kinds of "
        f"{Colors.blue}{str(adjective[2])}{Colors.reset} and {Colors.blue}{str(adjective[3])}{Colors.reset} figures.\n"
    )

    print(ml_0_string)


def ml_1(noun, verb, adjective):
    ml_1_string = (
        f"\nOur school cafeteria has really "
        f"{Colors.blue}{str(adjective[0])}{Colors.reset} food. Just thinking about it makes my stomach "
        f"{Colors.green}{str(verb[0])}{Colors.reset}.\nThe spaghetti is "
        f"{Colors.blue}{str(adjective[1])}{Colors.reset} and tastes like "
        f"{Colors.yellow}{str(noun[0])}{Colors.reset}. One day, I swear one of my meatballs started to "
        f"{Colors.green}{str(verb[1])}{Colors.reset}!\nThe turkey tacos are totally "
        f"{Colors.blue}{str(adjective[2])}{Colors.reset} and look kind of like old "
        f"{Colors.yellow}{str(noun[1])}{Colors.reset}.\nMy friend Dana actually likes the meatloaf, even though it's "
        f"{Colors.blue}{str(adjective[3])}{Colors.reset} and "
        f"{Colors.blue}{str(adjective[4])}{Colors.reset}.\n"
        f"I call it \"Mystery Meatloaf\" and think it's really made out of "
        f"{Colors.yellow}{str(noun[2])}{Colors.reset}.\n"
        f"My dad said he'd make my lunches, but the first day, he made me a sandwich out of "
        f"{Colors.yellow}{str(noun[3])}{Colors.reset} and peanut butter!\nI think I'd rather take my chances with the "
        f"cafeteria!\n"
    )

    print(ml_1_string)


def ml_2(noun, pl_noun, place, verb, pt_verb, adjective):
    ml_2_string = (
        f"\nOn the {Colors.blue}{str(adjective[0])}{Colors.reset} trip to "
        f"{Colors.yellow}{str(place[0])}{Colors.reset}, my "
        f"{Colors.blue}{str(adjective[1])}{Colors.reset} "
        f"friend and I decided to invent a game.\nSince this would be a rather "
        f"{Colors.blue}{str(adjective[2])}{Colors.reset} trip, it would need to be a game with "
        f"{Colors.yellow}{str(pl_noun[0])}{Colors.reset} and "
        f"{Colors.yellow}{str(pl_noun[1])}{Colors.reset}.\nUsing our "
        f"{Colors.yellow}{str(noun[0])}{Colors.reset} to "
        f"{Colors.green}{str(verb[0])}{Colors.reset}, we tried to get the "
        f"{Colors.yellow}{str(noun[1])}{Colors.reset} next to us to play too, but they just\n"
        f"{Colors.green}{str(pt_verb[0])}{Colors.reset} at us and "
        f"{Colors.green}{str(pt_verb[1])}{Colors.reset} away. After a few rounds, we thought the game could use some "
        f"{Colors.yellow}{str(pl_noun[2])}{Colors.reset},\n so we turned on the "
        f"{Colors.yellow}{str(noun[2])}{Colors.reset} and started "
        f"{Colors.green}{str(verb[1])}{Colors.reset}ing to the "
        f"{Colors.yellow}{str(noun[3])}{Colors.reset} that came on. Soon I got \n"
        f"{Colors.blue}{str(adjective[3])}{Colors.reset} and decided to "
        f"{Colors.green}{str(verb[2])}{Colors.reset}. I'll never "
        f"{Colors.green}{str(verb[3])}{Colors.reset} that trip for the rest of my life.\n"
    )

    print(ml_2_string)


def ml_3(noun, pl_noun, verb, adjective, number):
    ml_3_string = (
        f"\nOne of the best places to visit is the "
        f"{Colors.blue}{str(adjective[0]).title()}{Colors.reset} Natural History Museum. There are lots of\n"
        f"{Colors.blue}{str(adjective[1])}{Colors.reset} things to see there, but my favorite is the "
        f"dinosaur exhibit! As soon as you\n"
        f"{Colors.green}{str(verb[0])}{Colors.reset} in, you're greeted by a/an "
        f"{Colors.blue}{str(number[0])}{Colors.reset}-foot-tall statue of a/an "
        f"{Colors.yellow}{str(noun[0])}{Colors.reset} rex. It looks pretty scary, but my\n"
        f"{Colors.yellow}{str(noun[1])}{Colors.reset} promised that it's not going to come alive and "
        f"{Colors.green}{str(verb[1])}{Colors.reset} me! "
        f"{Colors.green}{str(verb[2]).title()}{Colors.reset} on to the next exhibit and\n"
        f"you'll see that there are more than "
        f"{Colors.blue}{str(number[1])}{Colors.reset} displays of "
        f"{Colors.blue}{str(adjective[2])}{Colors.reset} dinosaur bones and "
        f"{Colors.yellow}{str(pl_noun[0])}{Colors.reset}!\nAnd don't forget to look up, because there are "
        f"{Colors.yellow}{str(pl_noun[1])}{Colors.reset} hanging from the ceiling, too!\n"
    )

    print(ml_3_string)


# List of dictionaries. Format:
# "name" = title of story
# "function" = name of function
# "noun" = number of user-input nouns
# "pl_noun" = number of plural nouns
# "verb" = number of user-input verbs
# "pt_verb" = past-tense verb
# "adjective" = number of user-input adjectives
# "number" = just a number
mad_list = [
    {
        "name": "Today's Computers",
        "function": ml_0,
        "noun": 3,
        "pl_noun": 0,
        "place": 0,
        "verb": 2,
        "pt_verb": 0,
        "adjective": 4,
        "number": 0
    },
    {
        "name": "Our Cafeteria",
        "function": ml_1,
        "noun": 4,
        "pl_noun": 0,
        "place": 0,
        "verb": 2,
        "pt_verb": 0,
        "adjective": 5,
        "number": 0
    },
    {
        "name": "Road Trip",
        "function": ml_2,
        "noun": 4,
        "pl_noun": 3,
        "place": 1,
        "verb": 4,
        "pt_verb": 2,
        "adjective": 4,
        "number": 0
    },
    {
        "name": "A Day at the Museum",
        "function": ml_3,
        "noun": 2,
        "pl_noun": 2,
        "place": 0,
        "verb": 3,
        "pt_verb": 0,
        "adjective": 3,
        "number": 2
    }
]

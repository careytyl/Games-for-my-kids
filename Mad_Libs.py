import ml_library as ml
from random import randint


def mad_libs(randoms):
    """Mad Libs game. Picks a random Mad Lib story and takes user input for missing values."""

    # Initialize/reset lists for user-input words
    noun = []
    pl_noun = []
    place = []
    verb = []
    pt_verb = []
    adjective = []
    number = []

    # Setup for function call
    # None value will make function call not pass associated key
    # Done so that only relevant arguments are passed (makes functions look prettier)
    kwargs = dict(
        noun=None,
        pl_noun=None,
        place=None,
        verb=None,
        pt_verb=None,
        adjective=None,
        number=None
    )

    # Random number generated to determine Mad Lib choice
    # Allows for any number of additional Mad Libs to be created in ml_library
    # without changing code. len()-1 to account for index 0
    i = randint(0, len(ml.mad_list)-1)

    while True:

        # Verifies random pick is not in randoms list,
        # tries another random number if it is,
        # and resets the list if it's full
        if i not in randoms:
            randoms.append(i)

            # Prints the title of the selected Mad Lib
            # & the number of nouns/verbs/adjectives needed
            print(f"{ml.mad_list[i]['name']}\n"
                  f"(Nouns: {ml.mad_list[i]['noun'] + ml.mad_list[i]['pl_noun'] + ml.mad_list[i]['place']} // "
                  f"Verbs: {ml.mad_list[i]['verb'] + ml.mad_list[i]['pt_verb']} // "
                  f"Adjectives: {ml.mad_list[i]['adjective']} // "
                  f"Other: {ml.mad_list[i]['number']})")

            # User inputs
            # Updates kwargs if values are present (default: None)
            for nouns in range(ml.mad_list[i]['noun']):
                noun.append(input(f"Enter a {ml.Colors.yellow}noun{ml.Colors.reset}: "))
                kwargs.update(noun=noun)

            for pl_nouns in range(ml.mad_list[i]['pl_noun']):
                pl_noun.append(input(f"Enter a {ml.Colors.yellow}plural noun{ml.Colors.reset}: "))
                kwargs.update(pl_noun=pl_noun)

            for places in range(ml.mad_list[i]['place']):
                place.append(input(f"Enter a {ml.Colors.yellow}place{ml.Colors.reset}: "))
                kwargs.update(place=place)

            for verbs in range(ml.mad_list[i]['verb']):
                verb.append(input(f"Enter a {ml.Colors.green}verb{ml.Colors.reset}: "))
                kwargs.update(verb=verb)

            for pt_verbs in range(ml.mad_list[i]['pt_verb']):
                pt_verb.append(input(f"Enter a {ml.Colors.green}past-tense verb{ml.Colors.reset}: "))
                kwargs.update(pt_verb=pt_verb)

            for adjectives in range(ml.mad_list[i]['adjective']):
                adjective.append(input(f"Enter an {ml.Colors.blue}adjective{ml.Colors.reset}: "))
                kwargs.update(adjective=adjective)

            for numbers in range(ml.mad_list[i]['number']):
                number.append(input(f"Enter a {ml.Colors.blue}number{ml.Colors.reset}: "))
                kwargs.update(number=number)

            # Function call to print the story
            # Sends arguments only if a value is present
            ml.mad_list[i]['function'](**{k: v for k, v in kwargs.items() if v is not None})
            break

        # Compares randoms list (appended per run) to number of story options
        # Allows for any number of additional Mad Libs to be created in ml_library
        # without changing code
        elif i in randoms and len(randoms) < len(ml.mad_list):
            i = randint(0, len(ml.mad_list)-1)
            continue

        else:
            randoms = []
            continue

    exit_check(randoms)


def exit_check(randoms):
    """Simple exit/continue loop."""

    while True:
        again = input("Try again? y/n: ")
        if again.lower() == 'y':
            print("\n")
            mad_libs(randoms)
            break
        elif again.lower() == 'n':
            break
        else:
            print(f"Please enter {ml.Colors.bold}y{ml.Colors.reset} or {ml.Colors.bold}n{ml.Colors.reset}.")
            continue


def main():
    # List initialized and passed here to prevent it from resetting on mad_libs function call
    randoms = []
    mad_libs(randoms)


main()

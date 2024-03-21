# preventing duplicate entries
voted = {}

def check_voter(name):
    if name in voted:
        print("kick them out")
    else:
        voted[name] = True
        print("let them vote")

check_voter("Tom")
check_voter("Mike")
print(voted)
check_voter("Mike")
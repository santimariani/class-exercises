instructions = """Please fill in the blanks below:
____(name)____\'s favorite subject in school is ____(subject)____."""
print(instructions)
ask_name = input("What is your name? ")
ask_subject = input("What is your favorite subject? ")
print("%s's favorite subject is %s." % (ask_name, ask_subject))
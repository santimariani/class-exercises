greeting = "Hello %s, it is very nice to meet you and your friend %s!"

name_of_user = input("What is your name? ")
name_of_friend = input("What is your friend's name? ")

length_of_name = len(name_of_user)
length_of_friend_name = len(name_of_friend)

if length_of_name > 0 and length_of_friend_name > 0:
    print(greeting % (name_of_user, name_of_friend))
else:
    print("OK, I'll ask again some other time.")
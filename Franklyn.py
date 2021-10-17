print("Hello Franklyn")
print("I'm glad to see you <3")

meds=input("Have you taken your meds? (yes/no)")

if meds=="yes":
    tea_coffee=input("well done, would you like a cup of tea or coffee?:")
else:
    meds=="no"
    print("Please go and take your medication Franklyn")

if tea_coffee=="tea":
    print("Make yourself a cup of tea :)")
else:
    print("make yourself a cup of bean juice :)")

busy=input("are you busy today? (yes/no):")

if busy=="yes":
    print("enjoy your day :)")
else:
    print("roll yourself a scoobert,get some water, a lighter, and get dressed, its time to get your 10,000 steps in")
    exit()

def main():
    while True:
        half_way = input("have you got half way through your walk yet? Enter y/n: ")

        if half_way == "y":
            print ("Light up your scoobert and enjoy, don't forget to drink water!")
            return
        elif half_way == "n":
            print ("come back when you have got halfway :)")
        else:
            print ("You should enter either \"y\" or \"n\".")

if __name__ == "__main__":
    main()

pretty_girl=input("Franklyn may I tell you something? (y/n):")

if pretty_girl=="y":
    print("you are the bestest, prettiest, sexiest, most beautiful and kindest girl in the whole world :)")
else:
    print("Okay I'm sorry :(")

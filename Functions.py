def say_hello():
    name = input("What is your name? \n")
    insert_seperator()
    print("Hello, " + name + "!", sep="")


def insert_seperator():
    print("======================================")

def recite_poem():
    print("How about a Monty Python poem?")
    insert_seperator()
    print("Much to his Mum and Dad's dismay")
    print("Horace ate himself one day.")
    print("He didn't stop to say his grace,")
    print("He just sat down and ate his face.")

def say_goodbye():
    print("Goodbye!")


def main():
    say_hello()
    insert_seperator()
    recite_poem()
    say_goodbye

main()
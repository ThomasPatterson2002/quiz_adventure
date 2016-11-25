# An adventure game
from time import sleep
def room1():

    print("You wake up in the attic of an old house")
    sleep(2)
    print("You see a door")
    sleep(2)
    print("You also see a window")
    sleep(2)
    print("You also also see a stairway down")
    sleep(2)
    print("Which one do you choose")
    sleep(2)
    print("A. go though door")
    sleep(2)
    print("B. go through the window (not the best choice)")
    sleep(2)
    print("C. go down the stairs")
    answer = input("?")

    if answer.lower() == "b":
        print("You idiot, you fall to your death")
        sleep(2)
        print("Your character: no actualy im fine")
        sleep(2)
        print("You are then ripped apart by the guard dogs")
        sleep(2)
        print("Now you dead")
        sleep(1)
        print("GAME OVER")
        sleep(3)
        quit()
    elif answer.lower() == "c":
        print ("You tumble to your death like granny")
        sleep(2)
        print("R.I.P")
        sleep(3)
        quit()
    elif answer.lower() == "a":
        print("the door is locked")
    room2()
def room2():
    print("what do you do")
    sleep(2)
    print("A. look for key(waste of time)")
    sleep(2)
    print("B. stare at door for eternity(even bigger waste of time)")
    answer = input("?")

    if answer.lower() == "b":
        print("why did you choose that!")
        sleep(2)
        print("After 60 years of staring at the door(the best years of your life)you die")
        sleep(3)
        quit()
    elif answer.lower() == "a":
        print("you could not find the key(told you it was a waste of time)")
        sleep(2)
        print("Your character: i found a flash light!")
        sleep(2)

        print("Oh")
        sleep(2)
    room3()
def room3():
    print("what do you want to do with the flash light?")
    sleep(2)
    print("A. shine it at the stairs so you can see were your going")
    sleep(2)
    print("B. throw it out the window(why is this an option)")
    answer = input("?")

    if answer.lower() == "a":
        print("you discover that it was never a stairway but instead a shear drop")
        sleep(2)
        print("and die for some reason")
        sleep(3)
        quit()
    elif answer.lower() == "b":
        print("you idiot, the only thing left to do is jump out after it")
        sleep(2)
        print("but wait")
        sleep(10)
        print("that was a long wait")
        sleep(2)
        print("the flash light has distracted the guard dog")
        sleep(2)
        print("if you didnt choose option B for question 1 you wont know what im talking about")
        sleep(2)
        print("you manage to escape while the guard dog is distracted")
        sleep(2)
        print("Oh...wait its coming back")

    room4()
def room4():
    print("your about to die again what do you do")
    sleep(1)
    print("A. run for your life")
    sleep(2)
    print("B. insert stupid option here")
    answer = input("?")

    if answer.lower() == "a":
        print("you hurt you legs from the fall")
        sleep(2)
        print("once again you are inevitably killed in a horific way")
        sleep(2)
        print("so close")
        sleep(2)
        print("im sorry but...")
        sleep(2)
        print("here it comes...")
        sleep(2)
        print("any minute now...")
        sleep(2)
        print("and...")
        sleep(2)

        print("GAME OVER")
        sleep(3)
        quit()
    elif answer.lower() == "b":
        print("you fly away or somthing im to lazy to think of an ending")
        sleep(2)
        print("well done your not dead")
        sleep(3)
        for i in range(1, 100):
            print("bendog")
        print("420")
    
        quit()
        








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()

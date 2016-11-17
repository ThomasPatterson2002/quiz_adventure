# Our quiz!
score = 0
def quiz():
    
    q1()
def q1():
    global score
    
    print("Gandalf or Dumbledore????????")
    print("A. Gandalf")
    print("B. Dimpledoor")
    answer = input("CHOOSE ONE!!!!!!!:")

    if answer.lower() == "a":
        print("Run you fools!")
        print("Score is")
        score = score + 1
        print (score)
    q2()
def q2():
    
    global score
    
    print("NEXT QUESTION!!!!!")
    print("Golom or Smegle")
    print("A. Golom")
    print("B. Smegle")
    answer = input("CHOOSE ONE!!!!!!!:")

    if answer.lower() == "a" or "b":
        print ("IT DOESNT MATTER THEY'RE BOTH THE SAME!")
        score("Score is")
        score = score +1
        print(score)
    q3()
def q3():
    global score

    print("LAST QUESTION!")
    print("THIS IS THE MOST IMPORTANT QUESTION")
    print("was this the best quiz ever made")
    print("A. YES!!!!!")
    print("B. less enthusiastic yes")
    answer = input("CHOOSE ONE!!!!!!!:")

    if answer.lower() == "a":
        print ("THATS WHAT I THOUGHT")
        print ("Score is")
        score = score +9999998
        print(score)
    elif answer.lower() == "b":
        print ("I did'nt think anyone would pick that one")
        print ("Score is")
        score = score - score
        print (score)
        
        
    
          
    
    

    





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()

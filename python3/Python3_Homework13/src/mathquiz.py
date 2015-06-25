"""
mathquiz homework
"""

from random import randint
from datetime import datetime

NUM_QUEST = 5
MAX_INT = 10

def get_ints(mx):
    # returns a pair of ints between on a given max
    i1 = randint(1,mx)
    i2 = randint(1,mx)
    return(i1,i2)

if __name__ == "__main__":

    score = {}
    times = []
    start = datetime.now()
    for i in range(NUM_QUEST):
        # iterate over questions.
        #n1 = randint(1,MAX_INT)
        #n2 = randint(1,MAX_INT)
        n1, n2 = get_ints(MAX_INT)
        total = n1 + n2
        qstart = datetime.now()
        guess = int(input("What is the sum of "+str(n1)+" and "+str(n2)+"? "))
        #print(type(guess))
        if guess == total:
            print(str(guess),"is right!")
            score[i] = "right"
        else:
            print(str(guess),"is wrong!")
            score[i] = "wrong"
        duration = datetime.now() - qstart
        times.append(duration.seconds)
            
    end = datetime.now()
    
    for i in score.keys():
        print("Question #",str(int(i)+1),"took about",times[i],"seconds to complete and was",score[i])
        
    ttime = end - start
    print("You took",ttime.seconds,"seconds to finish the quiz")
    print("Your average time was",str(sum(times)/NUM_QUEST),"seconds per question")
    
        
        
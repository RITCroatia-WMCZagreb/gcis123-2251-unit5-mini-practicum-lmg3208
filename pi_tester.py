'''
@ASSESSME.USERID: lmg3208
@ASSESSME.AUTHOR: Lorena
@ASSESSME.DESCRIPTION: MiniPractical
@ASSESSME.ANALYZE: YES
'''

# The  thecima values of PI
PI_VALUE = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

def pi_tester():
    print("Please enter the first 100 decimal digits of pi in order.")
    num = 1
    write = input()
    loopCounter = 99
    piCounter = 2
    while loopCounter >= 0:
        loopCounter -= 1
        num += 1
        piCounter += 1
        if write == PI_VALUE[piCounter]:
            print("Enter the",num ,"-th digit of pi:")
        elif write != PI_VALUE[piCounter]:
            print("Incorrect digit. The correct digit is", PI_VALUE[piCounter])
        elif write != int:
            print("Please enter an integer.")
        
def display_score(score)->int:
    if score >= 0 and score <= 4:
        print("PI Neophyte")
    elif score >= 5 and score <= 9:
        print("PI Novice")
    elif score >= 10 and score <= 24:
        print("PI Journeyman")
    elif score >= 25 and score <= 49:
        print("PI Enthusiast")
    elif score >= 50 and score <= 96:
        print("PI Connoisseur")
    elif score >= 97 and score <= 100:
        print("PI Expert")
    elif score > 100:
        print("PI Imposter")
        
        
        

def main():
    pi_tester()
    #display_score(3)
    #display_score(110)

if __name__ == "__main__":
    main()
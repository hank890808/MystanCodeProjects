"""
File: class_reviews.py
Name: 蕭承瀚 Hank
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


EXIT = -1


def main():
    """
    As the user inputs the class number and the scores,
    the program will help calculate the max, min, avg of
    the scores.
    """
    total_001 = 0
    total_101 = 0
    n_001 = 0
    n_101 = 0
    while True:
        which_class = input("Which class? ")
        if which_class == str(EXIT):
            break
        which_class = which_class.upper()
        score = int(input("Score: "))
        if which_class == "SC001":
            if n_001 == 0:
                tmp_h_001 = score
                tmp_l_001 = score
            elif score > tmp_h_001:
                tmp_h_001 = score
            elif score < tmp_l_001:
                tmp_l_001 = score
            total_001 += score
            n_001 += 1
        elif which_class == "SC101":
            if n_101 == 0:
                tmp_h_101 = score
                tmp_l_101 = score
            elif score > tmp_h_101:
                tmp_h_101 = score
            elif score < tmp_l_101:
                tmp_l_101 = score
            total_101 += score
            n_101 += 1
    if n_001 == 0 and n_101 == 0:
        print("No class scores were entered")
    else:
        print("=============SC001=============")
        if n_001 == 0:
            print("No score for SC001")
        else:
            print("Max (001): "+str(tmp_h_001))
            print("Min (001): "+str(tmp_l_001))
            print("Avg (001): "+str(total_001/n_001))
        print("=============SC101=============")
        if n_101 == 0:
            print("No score for SC101")
        else:
            print("Max (101): "+str(tmp_h_101))
            print("Min (101): "+str(tmp_l_101))
            print("Avg (101): "+str(total_101/n_101))




# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()

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
    stat_001 = []
    stat_101 = []
    while True:
        which_class = input("Which class? ")
        if which_class == str(EXIT):
            break
        which_class = which_class.upper()
        if which_class != "SC001" and which_class != "SC101":
            print("There's no this class number.")
        else:
            score = int(input("Score: "))
            if which_class == "SC001":
                stat_001.append(score)
            elif which_class == "SC101":
                stat_101.append(score)
    if len(stat_001) == 0 and len(stat_101) == 0:
        print("No class scores were entered")
    else:
        print("=============SC001=============")
        stat(stat_001, "001")
        print("=============SC101=============")
        stat(stat_101, "101")


def stat(stat_list, which_class):
    """
    To calculate the maximum, minimum, and the average of the scores.
    :param stat_list: list, all scores of SC001 or SC101
    :param which_class: string, indicates which class it is
    """
    if len(stat_list) == 0:
        print("No score for SC"+which_class)
    else:
        tmp_h = stat_list[0]
        tmp_l = stat_list[0]
        total = 0
        for i in range(len(stat_list)):
            if stat_list[i] > tmp_h:
                tmp_h = stat_list[i]
            elif stat_list[i] < tmp_l:
                tmp_l = stat_list[i]
            total += stat_list[i]
        avg = total / len(stat_list)
        print("Max ("+which_class+"): "+str(tmp_h))
        print("Min ("+which_class+"): "+str(tmp_l))
        print("Avg ("+which_class+"): "+str(avg))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()

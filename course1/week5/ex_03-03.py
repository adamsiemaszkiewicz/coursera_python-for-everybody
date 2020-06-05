score = input("Enter score between 0.0 and 1.0: ")
score_f = float(score)
if score_f<1:
    if score_f>0:
        if score_f>=0.9:
            print("A")
        elif score_f>=0.8:
            print("B")
        elif score_f>=0.7:
            print("C")
        elif score_f>=0.6:
            print("D")
        else :
            print("F")
    else :
        print("The value is out of range")    
else :
    print("The value is out of range")
exit()

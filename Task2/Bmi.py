Height=float(input("Enter your Height in centimeters: "))
Weight=float(input("Enter your Weight in Kg:"))
Height = Height/100
BMI=Weight/ (Height*Height)
print("Your Body Mass Index is: ",BMI)
if(BMI>0):
    if(BMI<=16):
        print("you are heavily underweight")
    elif(BMI<=18.5):
        print("you are underweight")
    elif(BMI<=25):
        print("you are Healthy")
    elif(BMI<=30):
        print("you are Overweight")
    else: print("you are  heavily Overweight")
else: ("Enter Valid details")
## if condition(1 condition)

s_age=25

if s_age>=18:
    print("eligible to vote")

    
## else condition( 2 conditions)

s_age=17

if s_age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")

    
##if , elif and else condition (multiple conditions)

mark=82

if mark>=90:
    print("Grade S")
elif mark>=80:
    print("Grade A")
elif mark>=70:
    print("Grade B")
elif mark>=60:
    print("Grade C")
elif mark>=50:
     print("Grade D")
else:
     print("Fail")
 

## Nested if condition

age=25
drivinglicense="yes"
if age>=18:
    if drivinglicense=="yes":
        print("you are allowed to drive")
    else:
         print("please apply for driving license")
else:
    print("you are even not allowed to apply for driving lincense and drive")

    


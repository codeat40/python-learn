score = int(input("Enter your score: "))

#version 1 if statements
# this version is more informative than the second version because it tells us if the score is a letter grade, but it is less concise than the second version because it requires more lines of code.

# if score >= 90 and score <= 100:
#     print("Your grade is A.")
# elif score >= 80 and score < 90:
#     print("Your grade is B.")
# elif score >= 70 and score < 80:
#     print("Your grade is C.")
# elif score >= 60 and score < 70:
#     print("Your grade is D.")
# elif score >= 0 and score < 60:
#     print("Your grade is F.")
# else:
#     print("Invalid score.") 

# version 2 if statements
# this version is more concise, but it is less informative than the first version because it only tells us if the score is a letter grade or not, but it doesn't tell us what letter grade

# if 90 <= score <= 100:
#     print("Your grade is A.")
# elif 80 <= score < 90:
#     print("Your grade is B.")
# elif 70 <= score < 80:
#     print("Your grade is C.")
# elif 60 <= score < 70:
#     print("Your grade is D.")
# elif 0 <= score < 60:
#     print("Your grade is F.")
# else:
#     print("Invalid score.")

# this is replacing the code above, but it is not as concise as the second version because it requires more lines of code, but it is more informative than the second version because it tells us if the score is a letter grade, but it is less concise than the first version because it requires more lines of code.

if score >= 90:
    print("Your grade is A.")
elif score >= 80:
    print("Your grade is B.")
elif score >= 70:
    print("Your grade is C.")
elif score >= 60:
    print("Your grade is D.")
elif score >= 0:
    print("Your grade is F.")
else:
    print("Invalid score.")


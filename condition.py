# # input - name, math, science, english
# # process - average
# # output - passed or failed
#
# name = input("Enter name: ")
# math = input("Enter grade in Math: ")
# science = input("Enter grade in Science: ")
# english = input("Enter grade in English: ")
#
# average = (int(math) + int(science) + int(english)) / 3
#
# if average >= 75:
#     print("Congratulations! You passed the semester.")
#     if int(math) < 75:
#         print("But you need to re-enroll the Math subject!")
#     if int(science) < 75:
#         print("But you need to re-enroll the Science subject!")
#     if int(english) < 75:
#         print("But you need to re-enroll the English subject!")
#     else:
#         print("You passed all subjects.")
# else:
#     print("You failed the semester.")
#
# ######################

# input - years in service, office
# process - payment
# output - payment based on years in service and office

years = input("Enter the number of years in service: ")
office = input("Enter the office: ")

if office == "IT" and int(years) < 10:
    payment = 5000
elif office == "IT" and int(years) >= 10:
    payment = 10000
elif office == "acct" and int(years) < 10:
    payment = 6000
elif office == "acct" and int(years) >= 10:
    payment = 12000
elif office == "hr" and int(years) < 10:
    payment = 7500
elif office == "hr" and int(years) >= 10:
    payment = 15000

print("Payment is equal to " + str(payment))

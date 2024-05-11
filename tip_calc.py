bill_amount = float(input("Total bill amount? "))

service_question_answered = False

while service_question_answered == False:
    service_question_answered = input("Was the service bad, good, or great? ").lower()
    if service_question_answered == "bad":
        bad = True
        if bad:
            tip = .1
        service_question_answered = True
    elif service_question_answered == "good":
        good = True
        if good:
            tip = .15
        service_question_answered = True
    elif service_question_answered == "great":
        great = True
        if great:
            tip = .20
        service_question_answered = True
    else:
        print("STICK TO THE OPTIONS, BONZO! Let's try again... ")
        service_question_answered = False
total_tip = bill_amount * tip
total_amount = bill_amount + total_tip
print("Tip amount: $%.2f " % total_tip)
print("Total amount: $%.2f " % total_amount)
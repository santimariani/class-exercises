bill_amount = float(input("Total bill amount? "))
service_level = input("Was the service bad, good, or great? ").lower()
if service_level == "bad":
    bad = True
    if bad:
        tip = .1
elif service_level == "good":
    good = True
    if good:
        tip = .15
elif service_level == "great":
    great = True
    if great:
        tip = .20
else:
    print("STICK TO THE OPTIONS, BONZO! Let's try again... ")
    service_level = input("Was the service bad, good, or great? ").lower()
total_tip = bill_amount * tip
total_amount = bill_amount + total_tip
print("Tip amount: $%.2f " % total_tip)
print("Total amount: $%.2f " % total_amount)
times_split = int(input("Split how many ways? "))
amount_per_person = total_amount / times_split
print("Amount per person: %.2f" % amount_per_person)
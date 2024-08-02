bill_thickness = 0.11
tower_height = 442
no_of_bills = 1
days = 1

while(no_of_bills*bill_thickness < tower_height):
    days+=1
    no_of_bills*=2

print("no of days to reach tower height - ",days)
print("no of bills to reach tower height - ",no_of_bills)
print("Height of bills - ",no_of_bills*bill_thickness)
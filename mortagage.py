import math
principal = 500000
op = 500000
interest_rate = 0.05
mprem = 2684.11
total_paid = 0
while principal > 0:
    principal = principal * (1+interest_rate/12) - mprem
    total_paid += mprem
print("Total Payment for principal: ",op, " with interest rate " , interest_rate , "is ",
      total_paid);
print("Total Payment for principal: ",op, " with interest rate " , interest_rate , "is ",
      math.ceil(total_paid));
print("Total Payment for principal: ",op, " with interest rate " , interest_rate , "is ",
      math.floor(total_paid));
print("Total Payment for principal: ",op, " with interest rate " , interest_rate , "is ",
      round(total_paid,3));
print("Total Payment for principal: ",op, " with interest rate " , interest_rate , "is ",
      round(total_paid,9));

type_of_accounts = ("savings","current","credit","fixed","fixed","current")
print(type(type_of_accounts), type_of_accounts)
print("no of values in tuple ",len(type_of_accounts))

for acc in type_of_accounts:
    print(acc)
print("*"*65)

print(type_of_accounts.count("current"));
print(type_of_accounts.index("current"));
print(type_of_accounts[::-1]);

print(type_of_accounts[1:3]);
print(tuple(sorted(type_of_accounts)))
s_acc = tuple(sorted(type_of_accounts))
print(s_acc[::-1]);
t_acc = ("saving",)
t_acc[1] = "current"
print(type(t_acc))
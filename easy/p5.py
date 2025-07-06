n=int(input('Enter number of employees: '))
names=[]#For storing names
print('Enter name:')
for i in range(n):
    name=input()
    names.append(name)
count={} #To keep track of how many times each base email is used
emails=[] #Final email list
for name in names:
    first,last=name.lower().split() #Convert to lowercase and split
    email_name=first+ "." + last #Create base email
    if email_name not in count:
        email=email_name+"@company.com"
        count[email_name]=1#Initialize count
    else:
        email=email_name+str(count[email_name]) + "@company.com"
        count[email_name]+=1 #Increase the count
    emails.append(email)
# Print the final emails
print("\nFinal email addresses:")
for email in emails:
    print(email)

    




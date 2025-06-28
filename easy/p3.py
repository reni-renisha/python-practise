n =int(input()) #number of people
c =int(input()) #tank capacity
A =[int(input()) for _ in range(n)] #actions
tank=0
min_req=0 #Minimum tank level
for action in A:
    tank += action  # Add 1 if sell, subtract 1 if buy
    if tank < min_req:
        min_req = tank # Store the lowest tank level
X = -min_req  # Initial oil needed 
print(X)#print result



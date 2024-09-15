print("Welcome to python's pizza!\n")
bill = 0 
size = input("Enter the size of pizza you want? S, M or L\nFor small pizza (S)\nFor Medium pizza (M)\nFor large pizza (L)\n")
pepperoni = input("Do you need pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you need extra cheese? Y or N: ")
size = size.lower()
pepperoni = pepperoni.lower()
extra_cheese = extra_cheese.lower()

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill +=25
else: print("uff!! You pressed wrong key kindly restart the programe")        

if pepperoni == "y":
    bill += 2
elif pepperoni == "n": 
    bill = bill   
else: print("uff!! You pressed wrong key")

if extra_cheese == "y":
    bill+= 1
elif extra_cheese == "n": 
    bill = bill   
else: print("uff!! You pressed wrong key")    

print(f"Your final bill is ${bill}.")
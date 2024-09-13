print (" * * *        This is Ethiopia Bank          * * *  ")

saving_money = 1000 

print ("1. To see the money you have")
print ("2. To save (add) money")
print ("3. To withdraw the money")
print ("4. Exit")

option = input ( "       Please Insert your option number : " )

if option =="1":
    print (f" your saving amount is ${saving_money}")
    
elif option =="2":
    add_money = int (input ("Insert the amout of money you want to add:  "))
    money_added = saving_money + add_money
    
    print (f"You have {money_added} amount of money")
elif option =="3":
    withdraw_money = input ("Insert the amout of money you want to withdraw :  ")
    
    remaing_money = int (saving_money - withdraw_money)
    print (f"Your remaning amout of money is {remaing_money}")
    
else:
        print ("Good bye")

print("<3 <3 <3  Thanks for choosing us come back again! <3 <3 <3 ")



name=raw_input("What is your name little boy? ")
food=raw_input("What do you want to eat today {}? ".format(name))
pizzatype=raw_input('What kind of {0} do you want? '.format(food))
print "*********************************************************************************************"
print "\n\t\t\tHey Mr.%s, here is your {0} - %s \n".format(food.upper()) %(name.upper(),pizzatype.upper())
print "*********************************************************************************************"

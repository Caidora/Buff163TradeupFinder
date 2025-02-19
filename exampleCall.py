from controller import main_controller, adjust_controller, another_output


collection = "Prisma Case" 
grade = "Restricted"
floatTarget = 0.07 #This tells the controller to look for an outcome where all outputs are below 0.07/Factory new
#REMOVE MUST BE FILLED IN WITH OUTCOMES THAT ARE UNABLE TO BE ACHIEVED AT TARGET FLOAT.
remove = ['XM1014 | Incinegator','R8 Revolver | Skull Crusher'] #remove outcomes from float calculation 
statty = False




main_controller(collection, grade, remove, floatTarget,statty=statty)

new_float = 0.202

#adjust_controller is identical to main_controller but assumes buff has already been scraped and data in output.csv is correct

#adjust_controller(collection, grade, new_float, statty=statty)


#Performs the same as adjust_controller except it allows you to remove items if you have bought them.

#last_output = [ 227,  241,  268,  529,  967,  988, 1321, 1338, 2776, 2826]
#another_output(collection, grade, floatTarget, statty, last_output=last_output) 
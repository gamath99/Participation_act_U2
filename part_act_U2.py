"""creation of a program that return all the sandwiches that ave been made and return a list of each sandwich """
#List of sandwich orders in a sandwich menu
sandwich_orders = ["Ham", "Turkey", "Tuna", "Italian Sub", "chicken"]

#creation of an empty list to stock the completed sandwiches 
finished_sandwiches = []

#Prepare a sandwich 
#create a while loop to select the ordered sandwich and added to the finished sandwiches
while sandwich_orders:
    #use of the method pop to remove the last sandwich and to assign it to the variable   
    chosen_sandwich = sandwich_orders.pop(0)

    #Display the confirmation that the sandwich is ready 
    print(f"I made your {chosen_sandwich} sandwich.")
    #use of Method append for list to add the variable chosen_sandwich      
    finished_sandwiches.append(chosen_sandwich)

#Return all finished sandwiches
print("\nFinished Sandwiches:\n")
#create a for loop to pick a variable from the finished sandwich and display it.
for bread in finished_sandwiches:
    print(f"* {bread}")



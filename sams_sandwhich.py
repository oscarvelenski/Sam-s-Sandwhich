#sams sandwhich

#this is my code todfay

def bread_selection():
    bread_list = ["White", "Brown", "Italian", "Granary"]
    count=0
    print("We have the following breads:")
    while count < len(bread_list):
        print(count + 1, " ", bread_list[count])
        count += 1
    bread_selected=int(input("Which bread did you want? Enter a number"))
    return bread_list[bread_selected]

def meat_selection():
    meat_list = ["Tahr", "Rabbit", "Alligator", "Michael", "No Meat"]
    count = 0
    print("We have the following meat:")
    while count < len(meat_list):
        print(count + 1, " ", meat_list[count])
        count+=1
    meat_selection=int(input("Which meat do you want? Enter a number"))
    return meat_list[meat_selection]

def cheese_selection():
    cheese_list = ["Tahr cheese", "Blue cheese", "Feta", "Cheese wheel", "No cheese"]
    count = 0
    print("We have the following cheese:")
    while count < len(cheese_list):
        print(count + 1, " ", cheese_list[count])
        count+=1
    cheese_selection=int(input("Which cheese do you want? Enter a number"))
    return cheese_list[cheese_selection]

def salads_selection():
    salad_list = ["Lettuce", "Carrot", "Pumpkin pie", "Liam", "Onion", "Toyota carolla"]
    count = 0
    print("We have the following salads, you can have as many as you want")
    while count <len(salad_list):
        print("")


#main program
print("Welcome to Sam's Sandwhich Shop")
bread_choice = bread_selection()
print(f"Your selected bread: {bread_choice}")
meat_choice = meat_selection()
print(f"Your selected meat: {meat_choice}")
cheese_choice = cheese_selection()
print(f"Your selected cheese: {cheese_choice}")
#sams sandwhich

#this is my code todfay
import datetime

def first_name(message,lower,upper):
    while True: #this is an infinite loop
        name=str(input(message)).title()
        if len(name)>=lower and len(name)<=upper and name.isalpha(): 
            break
        else:
            print("invalid name")
    return name

def cell_number(message, lower, upper):
    while True: 
        cell=str(input(message))
        if len(cell) >= lower and len(cell) <= upper and cell.isnumeric():
            break
        else:
            print(f"ERROR!, please enter between a {lower} - {upper}")
    return cell 

def bread_selection():
    bread_list = ["White", "Brown", "Italian", "Granary"]
    count=0
    print("We have the following breads:")
    while count < len(bread_list):
        print(count + 1, " ", bread_list[count])
        count += 1
    bread_selected=int(input("Which bread did you want? Enter a number"))
    return bread_list[bread_selected-1]

def meat_selection():
    meat_list = ["Tahr", "Rabbit", "Alligator", "Michael", "No Meat"]
    count = 0
    print("We have the following meat:")
    while count < len(meat_list):
        print(count + 1, " ", meat_list[count])
        count+=1
    meat_selection=int(input("Which meat do you want? Enter a number"))
    return meat_list[meat_selection-1]

def cheese_selection():
    cheese_list = ["Tahr cheese", "Blue cheese", "Feta", "Cheese wheel", "No cheese"]
    count = 0
    print("We have the following cheese:")
    while count < len(cheese_list):
        print(count + 1, " ", cheese_list[count])
        count+=1
    cheese_selection=int(input("Which cheese do you want? Enter a number"))
    return cheese_list[cheese_selection-1]

def sauce_selection():
    sauce_list = ["Smorgaskaviar", "Black sauce", "Soy sauce", "Kai's special sauce", "No sauce"]
    count = 0
    print("We have the following sauce:")
    while count < len(sauce_list):
        print(count + 1, " ", sauce_list[count])
        count+=1
    sauce_selection=int(input("Which sauce do you want? Enter a number"))
    return sauce_list[sauce_selection-1]

def salads_selection():
    salad_list = ["Lettuce", "Carrot", "Pumpkin pie", "Liam", "Onion"]
    count = 0
    print("We have the following salads, you can have as many as you want")
    while count <len(salad_list):
        print(count+1, " ", salad_list[count])
        count+=1
    print("Press ENTER when you have finished choosing your salads")
    salads_added = ""
    selected_salad = " "

    while selected_salad != "":
        selected_salad = input(f"What number salad do you want?\nYou have selected: {salads_added}")
        if selected_salad != "":
            selected_salad = int(selected_salad)
            salads_added = salads_added + " " + salad_list[selected_salad-1]
    return salads_added.strip()

def output_textfile(first_name,cell_number,sandwich_order):
    date_time=datetime.datetime.now()
    outFile=open("sams_sandwich.txt","a")
    print(f"\n***Order for {first_name} - {cell_number}:***")

#main program
first_name=str(input("What is your first name?"))
cell_number=str(input("What is your cellphone?"))
bread_choice = bread_selection()
meat_choice = meat_selection()
cheese_choice = cheese_selection()
sauce_choice = sauce_selection()
salad_choice=salads_selection()
sandwich_order=[]
sandwich_order.append(first_name)
sandwich_order.append(cell_number)
sandwich_order.append(f"Bread: {bread_choice}")
sandwich_order.append(meat_choice)
sandwich_order.append(cheese_choice)
sandwich_order.append(sauce_choice)
sandwich_order.append(salad_choice)
output_textfile(first_name,cell_number,sandwich_order)
time_now = datetime.datetime.now()
print(time_now) 
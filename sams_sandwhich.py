#sams sandwhich

#this is my code todfay
#import datetime
import datetime

def first_name(message,lower,upper):
    while True: #this is an infinite loop
        name=str(input(message)).title()
        if len(name)>=lower and len(name)<=upper and name.isalpha(): 
            break
        else:
            print("invalid name")
    return name

def phone_number(message, lower, upper):
    while True: 
        cell=str(input(message))
        if len(cell) >= lower and len(cell) <= upper and cell.isnumeric():
            break
        else:
            print(f"ERROR!, please enter between a {lower} - {upper}")
    return cell 

def force_number(message,lower,upper):
    while True:
        try:
            num=int(input(message))
            if num>=lower and num<=upper:
                break
            else:
                print(f"ERROR!, please enter between a {lower} - {upper}")
        except:
            print("Error, please enter in a number not text")
    return num

def print_lists(list, item):
    count=0
    print(f"We have the following {item}:")
    while count < len(list):
        print(count + 1, " ", list[count])
        count += 1
    return

def bread_selection():
    #function for use to pick bread option
    bread_list = ["White", "Brown", "Italian", "Granary"]
    print_lists(bread_list, "breads")
    bread_selected=force_number("Which bread did you want? Enter a number",1,len(bread_list))
    return bread_list[bread_selected-1]

def meat_selection():
    #function for use to pick meat option
    meat_list = ["Tahr", "Rabbit", "Alligator", "Michael", "No Meat"]
    print_lists(meat_list, "meats")
    meat_selection=force_number("Which meat do you want? Enter a number",1,len(meat_list))
    return meat_list[meat_selection-1]

def cheese_selection():
    #function for use to pick cheese option
    cheese_list = ["Tahr cheese", "Blue cheese", "Feta", "Cheese wheel", "No cheese"]
    print_lists(cheese_list, "cheese")
    cheese_selection=force_number("Which cheese do you want? Enter a number",1,len(cheese_list))
    return cheese_list[cheese_selection-1]

def sauce_selection():
    #function for use to pick sauce option
    sauce_list = ["Smorgaskaviar", "Black sauce", "Soy sauce", "Kai's special sauce", "No sauce"]
    print_lists(sauce_list, "sauce")
    sauce_selection=force_number("Which sauce do you want? Enter a number",1,len(sauce_list))
    return sauce_list[sauce_selection-1]

def salads_selection():
    #function for use to pick salad option(s)
    salad_list = ["Lettuce", "Carrot", "Pumpkin pie", "Liam", "Onion"]
    print_lists(salad_list, "salad")
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
    #writes everything into a new text file
    date_time=datetime.datetime.now()
    outFile=open("sams_sandwich.txt","w")
    print(f"\n***Order for {first_name} - {cell_number}:***")
    outFile.write(f"\nDate of booking:{date_time}")
    for item in sandwich_order:
        print (item)
        outFile.write(f"\n {item}")
    outFile.write(f"\nEnd of order: {date_time}")
    print(f"***End of order : {date_time}***")
    outFile.write("\n")
    outFile.write("\n")
    outFile.close()

def main_program():
    print("Welcome to Sam's Sandwich Shop")
    first_name = first_name("What is your first name?", 2, 15)#asks for first name and set the boundary 
    cell_number = phone_number("What is your cellphone?", 9, 12)#ask for the cellphone and set the boundary 
    bread_choice = bread_selection() 
    meat_choice = meat_selection()
    cheese_choice = cheese_selection()
    sauce_choice = sauce_selection()
    salad_choice=salads_selection()
    sandwich_order=[]
    sandwich_order.append(first_name)#adds first name to the list
    sandwich_order.append(cell_number)#adds cell number to the list
    sandwich_order.append(f"{bread_choice} Bread")#adds bread choice to the list
    sandwich_order.append(f"{meat_choice} Meat")#adds meat choice to the list
    sandwich_order.append(f"{cheese_choice} Cheese")#adds cheese choice to the list
    sandwich_order.append(f"{sauce_choice} Sauce")#adds sauce choice to the list
    sandwich_order.append(salad_choice)#adds salad choice to the list
    output_textfile(first_name,cell_number,sandwich_order)
    time_now = datetime.datetime.now()#gets current timeline
    print(time_now)

#main program
main_program()
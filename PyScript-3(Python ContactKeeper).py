print("**** Contact Book ****")
print("1. Add contact number")
print("2. Search a number")
print("3. Show all the numbers")
print("4. Exit")
contact={}

while True:
    a=int(input("Enter the choice: "))
    if a==1:
        name=input("Name: ")
        number=input("Number: ")
        contact[name]=number
    elif a==2:
        test=input("substring: ")
        name2 = [i for i in contact if i[0].lower() == test.lower()]
        print("The contact names with this substring are "+str(name2))
        name1=input("name of the person you want to search from above: ")
        print("The contact number of ",name1," is ",contact[name1])
    elif a==3:
        print("The numbers in this contact book is: ")
        contact_1=sorted(contact)
        sorted_contact={number:contact[number] for number in contact_1}
        print(sorted_contact)
    elif a==4:
        break


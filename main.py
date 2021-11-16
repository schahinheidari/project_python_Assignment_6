from pyfiglet import Figlet
from termcolor import colored
import qrcode

PRODUCTS = []
print("Loading...")
myfile = open('/home/shahin/Desktop/sajjad/store/database.txt', 'r+')
data = myfile.read().lower()
products_list = data.split('\n')
for i in range(len(products_list)):
    products_info = products_list[i].split(',')
    myDictionary = {}
    myDictionary['id'] = int(products_info[0])
    myDictionary['name'] = products_info[1]
    myDictionary['price'] = float(products_info[2])
    myDictionary['count'] = int(products_info[3])
    PRODUCTS.append(myDictionary)

def show_menu():
    print("1- Add product")
    print("2- Edit product")
    print("3- Delete product")
    print("4- Search product")
    print("5- Show All list product")
    print("6- Buy product")
    print("7- Exit")

def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])

def add_new_product():
    while True:
        Add_Request = input("Do You Want Add Product to Database?  y/n: ")
        if(Add_Request == "y"):
            myfile = open('/home/shahin/Desktop/sajjad/shahinStore/database.txt', 'a')
            myfile.write("\n")
            myfile.write(str(input("please input new ID: ")))
            myfile.write(",")
            myfile.write(str(input("please input name of new product: ")))
            myfile.write(",")
            myfile.write(str(input("please input price of new product: ")))
            myfile.write(",")
            myfile.write(str(input("please input count of product: ")))
            myfile.close()
        elif(Add_Request == "n"):
            break

def edit_product():
    while True:
        myfile = open('/home/shahin/Desktop/sajjad/store/database.txt', 'r+')
        Edit_product = input("Do you want to edit the product? if yes please input y else n: ")
        if (Edit_product == "y"):
            print("1- Edit Id product")
            print("2- Edit Name product")
            print("3- Edit Price product")
            print("4- Edit Count product")
            choice_a_number = input("please choose one of the number: ")
            Id_edit = input("Please Enter Product Id: ")
            for i in range(len(PRODUCTS)):
                if(PRODUCTS[i]["id"]) == Id_edit:
                    if (choice_a_number == "1"):
                        PRODUCTS[i]["id"] == myfile.write(str(input("please input new ID as you want: "))) 
                    elif (choice_a_number == "2"):
                        PRODUCTS[i]["name"] == myfile.write(str(input("please input name of new product as you want: ")))
                    elif (choice_a_number == "3"):
                        PRODUCTS[i]["price"] == myfile.write(str(input("please input price of new product as you want: ")))
                    elif (choice_a_number == "4"):
                        PRODUCTS[i]["count"] == myfile.write(str(input("please input count of product as you want: ")))
                    else:
                        print("We don't have this product")
                        break
        elif(Edit_product == "n"):
            break

def delete_product():
    while True:
        Delete_product = input("Do you want to remove the product? if yes please input y else n: ")
        if (Delete_product == "y"):
            Id_delete = input("Please Enter Product Id: ")
            for i in range(len(PRODUCTS)):
                if(PRODUCTS[i]["id"]) == Id_delete:
                    PRODUCTS.pop(i)
                    print("product removed")
                else:
                    print("We don't have this product")
                    break
        elif(Delete_product == "n"):
            break

def search_in_list():
    print(PRODUCTS)
    while True:
        Search_product = input("Do you want to search for the product? if yes please input y else n: ")
        if (Search_product == "y"):
            search_name = input("What are you looking for? ")
            for i in range(len(PRODUCTS)):
                if(PRODUCTS[i]["name"] == search_name):
                    print("Product founded", {"id":PRODUCTS[i]["id"],"name":PRODUCTS[i]["name"],"price":PRODUCTS[i]["price"],"count":PRODUCTS[i]["count"]}) 
                    break
            else:
                print("Not match")
        elif (Search_product == "n"):
            break

def buy_product():
    pass

def exit():
    file = open('/home/shahin/Desktop/sajjad/store/database.txt', 'r+')
    for i in range(len(PRODUCTS)):
        rows = PRODUCTS[i]["id"] + ',' + PRODUCTS[i]["name"] + ',' + PRODUCTS[i]["price"] + ',' + PRODUCTS[i]["count"] + '\n'
        file.write(rows)
    file.close()
    exit()

def qr_code():
    while True:
        Qr_product = input(" Do you want QR Code product? if yes please input y else n: ")
        if Qr_product == "y" or "Y":
            Qr_id = input("Please enter id of product: ")
            for i in range(len(PRODUCTS)):
                if PRODUCTS[i]["id"] == Qr_id:
                    myFile = {"id": PRODUCTS[i]["id"], "name": PRODUCTS[i]["name"], "price": PRODUCTS[i]["price"], "count": PRODUCTS[i]["count"]}
                    img = qrcode.make(myFile)
                    img.save('qrcode.png')
                    print("QR code created seccessfully!")
                    break
            else:
                print("There is no ID exist")
        elif Qr_product == "n" or "N":
            break

f = Figlet(font='standard')
print (f.renderText('Store Market'))

while True:
    show_menu()
    choice = int(input("please choose a number: "))

    if choice == 1:
        add_new_product()
    elif choice == 2:
        edit_product()
    elif choice == 3:
        delete_product()
    elif choice == 4:
        search_in_list()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy_product()
    elif choice == 7:
        exit()

    show_menu()
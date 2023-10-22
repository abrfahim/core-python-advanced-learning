# shipping costs app
area = ['Mirpur','Badda','Gulshan','Uttara','Mohakhali','Agargaon']
area1 =['Mohammadpur','Banani','Jatrabari', 'Shyamoli','New Market']
area2= ['Chittagong','Khulna', 'Sylhet','Cumilla']

user_area = input('Location:')
product_price = int(input('Selected Product Price:'))

if(user_area in area):
    if(product_price>=1000):
        print("No Shipping charges")
    else: print("Shipping charges: 50/-")
elif(user_area in area1):
    if (product_price<1500):
        print("Shippiing Charage: 80/-")
    else:print("Shipping charges: 60/-")
elif(user_area in area2):
    if (product_price<2000):
        print("Shippiing Charage: 150/-")
    else:print("Shipping charges: 120/-")
else: print('Your area is not available in our service')
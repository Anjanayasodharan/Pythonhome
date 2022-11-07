import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'homeautomationdb')
mycursor = mydb.cursor()
while True:

    print("select an option from the menu")
    print("1 add ")
    print("2 view all book")  
    print("3 search a book")
    print("4 exit")
    
    choice = int(input('enter an option:'))
    if(choice==1):
        print('book enter selected')
      

    temperature = input("enter the temperature")

    humidity = input("enter the humidity")

    moisture = input("enter the moisture")

    sql = 'INSERT INTO `sensorvalues`(`temperature`, `humidity`, `moisture`, `date`) VALUES (%s,%s,%s,now())'

    data = (temperature,humidity,moisture)

    mycursor.execute(sql , data)

    mydb.commit()

    print("value inserted succesfully")
    break
    if (choice==2):
        print ('view')
        break
    if(choice==3):
        print('search')
        break
    if(choice==4):
        print('exit')
        break

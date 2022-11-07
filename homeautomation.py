import mysql.connector



mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'homeautomationdb')

mycursor = mydb.cursor()

while True:



    print("select an option from the menu")



    print("1 add ")



    print("2 view all ")  



    print("3 search ")



    print("4 update ")    



    print("5 delete ")



    print("6 exit")



    choice = int(input('enter an option:'))



    if(choice==1):



        print("add selected")



        temperature = input("enter the temperature")



        humidity = input("enter the humidity")



        moisture = input("enter the moisture")



        sql = 'INSERT INTO `sensorvalues`(`temperature`, `humidity`, `moisture`, `date`) VALUES (%s,%s,%s,now())'



        data = (temperature,humidity,moisture)



        mycursor.execute(sql , data)



        mydb.commit()



        print("value inserted succesfully")

       

    elif(choice==2):



        sql = 'SELECT * FROM `sensorvalues`'

        mycursor.execute(sql)

        result = mycursor.fetchall()

        for i in result:

            print(i)
    elif(choice==3):



        print('search ')



    elif(choice==4):



        print('update ')



    elif(choice==5):



        print('delete ')



    elif(choice==6):



        break



 
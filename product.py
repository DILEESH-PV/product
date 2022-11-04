import requests
import json
import mysql.connector

try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='productdb')
except mysql.connector.Error as e:
    print("db connection error")
mycursor=mydb.cursor()
data=requests.get("https://dummyjson.com/products").text
data_info=json.loads(data)
for j in data_info['products']:
    #print(str(j['title']))
    pri=str(j['price'])
    dis=str(j['discountPercentage'])
    rat=str(j['rating'])
    stoc=str(j['stock'])
    sql='INSERT INTO `product`(`title`, `description`, `price`, `discount`, `rating`, `stock`, `brand`, `category`) VALUES ("'+j['title']+'","'+j['description']+'","'+pri+'","'+dis+'","'+rat+'","'+stoc+'","'+j['brand']+'","'+j['category']+'")'
        #sql="INSERT INTO `product`(`title`, `description`, `price`, `discount`, `rating`, `stock`, `brand`, `category`) VALUES ('"+i['title']+"','"+i['description']+"','"+pri+"','"+dis+"','"+rat+"','"+stoc+"','"+i['brand']+"','"+i['category']+"')"
    mycursor.execute(sql)
    mydb.commit()
    print("Data inserted successfully",j['title'])
        
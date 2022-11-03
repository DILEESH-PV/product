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
user_list=[]
for i in data_info:
    user_list.append(i)
test=user_list[0]
pre=data_info[test]
for i in pre:
    #user_list.append([i["title"],i["description"],i["price"]])
    pri=str(i['price'])
    dis=str(i['discountPercentage'])
    rat=str(i['rating'])
    stoc=str(i['stock'])
    sql='INSERT INTO `product`(`title`, `description`, `price`, `discount`, `rating`, `stock`, `brand`, `category`) VALUES ("'+i['title']+'","'+i['description']+'","'+pri+'","'+dis+'","'+rat+'","'+stoc+'","'+i['brand']+'","'+i['category']+'")'
    #sql="INSERT INTO `product`(`title`, `description`, `price`, `discount`, `rating`, `stock`, `brand`, `category`) VALUES ('"+i['title']+"','"+i['description']+"','"+pri+"','"+dis+"','"+rat+"','"+stoc+"','"+i['brand']+"','"+i['category']+"')"
    mycursor.execute(sql)
    mydb.commit()
    print("Data inserted successfully",i["title"])
    #print(i['title'],"\n",i['description'],"\n",i['price'],"\n",i['discountPercentage'],"\n",i['rating'],"\n",i['stock'],"\n",i['brand'],"\n",i['category'])
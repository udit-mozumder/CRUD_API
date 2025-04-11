from flask import Flask,request,jsonify
import mysql.connector
app= Flask(__name__)

#connecting to the database
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mysql_crud"
)

mycursor= mydb.cursor(dictionary=True)

# To fetch all records

@app.route('/get_all_records',methods=['GET'])
def get_all_record():
    mycursor.execute("SELECT * FROM books")
    x=mycursor.fetchall()
    return jsonify (x)

# to insert data

@app.route('/create_records', methods=['POST'])
def create_record():
    data=request.get_json()
    query="INSERT INTO books(title,author) VALUES(%s,%s)"
    val=(data['title'],data['author'])
    mycursor.execute(query,val)
    mydb.commit()
    return jsonify({"message": "Books added Successfully"})

#to edit data

@app.route('/update/<int:id>',methods=['PUT'])
def update_record(id):
    data=request.get_json()
    query="UPDATE books SET title=%s,author=%s WHERE id=%s"
    val=(data['title'],data['author'],id)
    mycursor.execute(query,val)
    mydb.commit()
    return jsonify({"message":"Updated Successfully"})

#delete record

@app.route('/delete_record/<int:id>',methods=['DELETE'])
def delete_record(id):
    mycursor.execute("DELETE FROM books WHERE id=%s",(id,))
    
    mydb.commit()
    return jsonify({"message": "Record successfull deleted"})

if __name__ == '__main__':
    app.run(debug=True)
from pymysql import connections
import os
#import boto3
#from config import *
from flask import Flask,render_template

db_conn = connections.Connection(
    host=mysqldbemployee.cmyrfs8fssae.ap-south-1.rds.amazonaws.com,
    port=3306,
    user=mysqldbadmin,
    password=admin1234,
    db=mysqldbemployee

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
return render_template('getemp.html')

@app.route("/Getamp", methods=['POST'])
def Getemp():
    Employee_id = request.form['Empid']
    select_sql = "select Emp_fname, Emp_lname from employee where Emp_id= Employee_id"
    sql_cursor = mysql.connection.cursor()

    result_value = sql_cursor.execute(select_sql)
#   if result_value > 0 
    emp_details = cur.fetchall()
    Employee_id    = emp_details.Emp_id ,     Employee_fname = emp_details.Emp_fname  ,     Employee_lname = emp_details.Emp_lname 
              
    except Exception as e:
    return str(e)

    finally:
        cursor.close()

    print("all modification done...")
    return render_template('GetEmpOutput.html',Empid=Employee_id,Empfname=Employee_fname,Empname=Employee_lname)

if __name__ =='__main__':
	app.run(host='0.0.0.0',port=8080,debug=True)

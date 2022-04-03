from flask import Flask, request, render_template
import sqlite3
from sqlite3 import Error
import Tools.Books as BK
import Tools.Customers as CR

con = sqlite3.connect('Library.db', check_same_thread=False)

api = Flask(__name__)
cur = con.cursor()

def initDB():
    try:
        cur.execute('''CREATE TABLE Books
               (BookID int, Name text, Author text, YearPublished int, Type (1/2/3) int''')
        cur.execute('''CREATE TABLE Customers
               (CustomerId int, Name text, City text, age int)''')
        cur.execute('''CREATE TABLE Loans
               (CustomerID int, BookID int, LoanDate int, ReturnDate int)''')

    except:
        print("Table already exist")
  
    con.commit()
initDB()

@api.route("/", methods=['GET', 'POST'])
def homepage():
    return render_template("mainHomepage.html")


@api.route("/Books/bookHomepage", methods=['GET', 'POST'])
def bookHomepage():
    return render_template("/Books/bookHomepage.html")


@api.route("/Books/addBook", methods=['GET', 'POST'])
def addBook():
    return BK.Book.addBook(BK.Book)


@api.route("/Books/displayBooks", methods=['GET', 'POST'])
def displaybooks():
    return BK.Book.displayBooks(BK.Book)


@api.route("/Books/findBook", methods=['GET','POST'])
def findBook():
    return BK.Book.findBook(BK.Book)


@api.route("/Books/removeBook", methods=['GET', 'POST'])
def removeBook():
    return BK.Book.removeBook(BK.Book)

@api.route("/Customers/CustHomepage", methods=['GET', 'POST'])
def CustHomepage():
    return render_template("/Customers/CustHomepage.html")


@api.route("/Customers/addCustomers", methods=['GET', 'POST'])
def addCustomer():
    return CR.Customers.addCustomers(CR.Customers)


@api.route("/Customers/removeCustomers", methods=['GET', 'POST'])
def removeCustomer():
    return CR.Customers.removeCustomers(CR.Customers)


@api.route("/Customers/displayCustomers", methods=['GET', 'POST'])
def showAllCustomers():
    return CR.Customers.displayCustomers(CR.Customers)

@api.route("/Customers/findCustomers", methods=['GET', 'POST'])
def findCustomer():
    return CR.Customers.findCustomers(CR.Customers)

if __name__ == '__main__':
    api.run(debug=True,port=9000)
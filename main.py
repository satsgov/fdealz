import pymongo
from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient

app = Flask ( __name__ )

# Connect to the MongoDB server
client = pymongo.MongoClient ( 'mongodb://localhost:27017/' )

# Access the 'users' collection in the 'mydatabase' database
db = client['student-api']
users_collection = db['students']


@app.route ( '/' )
def show_login():
    return render_template ( 'login.html' )


@app.route ( '/login', methods=['GET', 'POST'] )
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again.'
        else:
            return render_template ( 'welcome.html' )
    return render_template ( 'login.html', error=error )


@app.route ( "/register" )
def register():
    return render_template ( "registration.html" )


@app.route ( '/users' )
def get_users():
    # Find all user documents in the 'users' collection
    users = list ( users_collection.find () )

    # Create a new list with only the fields you want to include in the response
    response = []
    for user in users:
        new_user = {
            'name': user['name'],
            'email': user['email']
        }
        response.append ( new_user )

    # Return the response as a JSON array
    return jsonify ( response )


app.run ( debug=True )

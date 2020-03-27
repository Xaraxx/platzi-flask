import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()
default_app = firebase_admin.initialize_app()

db = firestore.client()

def get_users():
    return db.collection('users').get()

def get_things_to_do(user_id):
    return db.collection('users').document(user_id).collection('things_to_do').get()

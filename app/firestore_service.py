import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore




credential = credentials.ApplicationDefault()
default_app = firebase_admin.initialize_app()

db = firestore.client()

def get_users():
    return db.collection('users').get()

def get_user(user_id):
    return db.collection('users').document(user_id).get()


def create_new_user(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})


def get_things_to_do(user_id):
    return db.collection('users').document(user_id).collection('things_to_do').get()


def create_new_task(user_id, description):

    task_ref = db.collection('users').document(user_id).collection('things_to_do')
    task_ref.add({
        'description': description, 
        'done': False})


def delete_task(user_id, task_id):
    task_ref = _get_task_ref(user_id, task_id)
    task_ref.delete()
    # task_ref = db.collection('users').document(user_id).collection('things_to_do').document(task_id)


def update_task(user_id, task_id, done):
    task_done = not bool(done)
    task_ref = _get_task_ref(user_id, task_id)
    task_ref.update({'done': task_done})


def _get_task_ref(user_id, task_id):
    return db.document('users/{}/things_to_do/{}'.format(user_id, task_id))

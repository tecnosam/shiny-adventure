from app.utils.database import main_database as db
from app.utils.responses import (
    update_success_response,
    create_success_response,
    create_failure_response,

    login_success_response,
    login_failure_response
)

from app.utils.security import hash_password, verify_password


def register(body: dict):

    collection = db['users']

    body['id'] = collection.count_documents({}) + 1

    body['password'] = hash_password(body['password'])

    response = collection.insert_one(body)

    if response.acknowledged:
        return create_success_response("User created successfully", response)

    return create_failure_response("User creation failed")


def get_user(user_id: int):

    collection = db['users']

    user = collection.find_one({'id': user_id})

    return user


def login(email, password):

    collection = db['users']

    user = collection.find_one({'email': email})

    if user:
        if verify_password(password, user['password']):
            return login_success_response(user)

        return login_failure_response("Incorrect password")

    return login_failure_response("User not found")


def change_password(user_id, new_password):

    collection = db['users']

    new_password = hash_password(new_password)

    response = collection.update_one(
        {'_id': user_id},
        {'$set': {'password': new_password}}
    )

    return update_success_response(response)


def update_user(user_id, body: dict):

    collection = db['users']

    response = collection.update_one(
        {'_id': user_id},
        {'$set': body}
    )

    return update_success_response(response)

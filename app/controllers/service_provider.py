from app.utils.database import main_database as db

from app.utils.responses import update_success_response


def get_profile(user_id: int):

    collection = db['users']

    profile = collection.find_one(
        {'_id': user_id},
        {'_id': 1, 'name': 1, 'service_provider': 1}
    )

    return profile


def get_skills(user_id: int):
    # Fetch skills associated with a particular user
    collection = db['users']

    skills = collection.find_one(
        {'_id': user_id},
        {'_id': 0, 'service_provider.skills': 1}
    )

    return skills


def create_service_provider(service_provider: dict):

    collection = db['users']

    response = collection.update_one(
        {'_id': service_provider['user_id']},
        {'service_provider': service_provider}
    )

    return update_success_response(response)


def add_skill(user_id, skill_id: int):

    collection = db['users']

    response = collection.update_one(
        {'_id': user_id},
        {'$push': {'service_provider.skills': skill_id}}
    )

    return update_success_response(response)


def remove_skill(user_id, skill_id: int):
    collection = db['users']

    response = collection.update_one(
        {'_id': user_id},
        {'$pull': {'service_provider.skills': skill_id}}
    )

    return update_success_response(response)

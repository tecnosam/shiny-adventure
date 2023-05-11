from pymongo.results import InsertOneResult, UpdateResult

from app.utils.security import generate_token


class BaseAPIResponse:
    def __init__(self, status_code, message, data=None):
        self.status_code = status_code
        self.message = message
        self.data = data

    def to_dict(self):
        return {
            "status_code": self.status_code,
            "message": self.message,
            "data": self.data,
        }


# Generic API Responses #


def create_success_response(message, mongo_response: InsertOneResult):

    success = mongo_response.acknowledged

    data = {
        "success": success,
        "id": str(mongo_response.inserted_id)
    }

    return BaseAPIResponse(200, message, data).to_dict()


def create_failure_response(message):

    data = {"success": False}

    return BaseAPIResponse(400, message, data).to_dict()


def update_success_response(mongo_response: UpdateResult):

    success = mongo_response.acknowledged and \
          mongo_response.modified_count == 1

    data = {"success": success}

    message = "Update successful" if success else "Update failed"

    return BaseAPIResponse(200, message, data).to_dict()


# Auth API Responses #


def login_success_response(user):

    user['_id'] = str(user['_id'])

    data = {
        "success": True,
        "accessToken": generate_token(user['id']),
        "userData": user
    }

    message = "User Logged in successfully"

    return BaseAPIResponse(200, message, data).to_dict()


def login_failure_response(message):

    data = {
        "success": False,
        "userData": None
    }

    return BaseAPIResponse(401, message, data).to_dict()

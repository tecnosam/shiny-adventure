from app.forms.job import JobForm, ApplicationForm

from app.utils.database import mongo_client as client


db = client.get_database('jobify')


def get_job_list(skills=[], location=[], language=[]):
    collection = db['jobs']

    query = {}

    return list(collection.find(query))


def get_job(job_id):

    collection = db['jobs']

    return collection.find_one({'_id': job_id})


def create_job(body: JobForm):
    collection = db['jobs']

    response = collection.insert_one(body.dict())

    if response.acknowledged:
        return {"id": response.inserted_id}


def apply_job(
    application: ApplicationForm,
    job_id: int
):
    collection = db['jobs']

    data = application.dict()

    return collection.update_one(
        {'_id': job_id},
        {'$push': {'applications': data}}
    )


def delete_job(job_id: int):

    collection = db['jobs']

    collection.delete_one({'_id': job_id})

    return {"status": "success"}

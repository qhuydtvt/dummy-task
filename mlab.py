import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds151141.mlab.com:51141/dummy-task
host = "ds151141.mlab.com"
port = 51141
db_name = "dummy-task"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
import json

class BasicJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__
        #return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4)
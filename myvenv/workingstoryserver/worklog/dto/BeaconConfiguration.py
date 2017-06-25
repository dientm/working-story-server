import json

class BeaconConfiguration():
    def __init__(self, **kwargs):
        params = ['name', 'uuid', 'minor', 'major', 'location']
        for key in params:
            self.key = kwargs[key]

    def __int__(self, beacon):
        self.name = beacon.name
        self.uuid = beacon.uuid
        self.minor = beacon.minor
        self.major = beacon.major
        self.location = beacon.location

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
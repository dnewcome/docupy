import json

class JSONRecordEncoder(json.JSONEncoder):
    """JSON encoder that can handle RestObjects"""
    def default(self, obj):
        try:
            return obj._asdict()
        except:
            return json.JSONEncoder.default(self, obj)

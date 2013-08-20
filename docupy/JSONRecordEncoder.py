import json

class JSONRecordEncoder(json.JSONEncoder):
    """JSON encoder that will serialize recordtypes"""
    def default(self, obj):
        try:
            return obj._asdict()
        except Exception as e:
            print e
            return json.JSONEncoder.default(self, obj)

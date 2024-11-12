import json

class SingatureModel:
    def __init__(self,decryptedData):
        object = json.loads(decryptedData)
        self.data = object["data"]
        self.signature = object["signature"]

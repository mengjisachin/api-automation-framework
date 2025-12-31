import requests

class APIBase:

    #initialize base_url and headers
    def __init__(self, base_url, header=None):
        self.base_url = base_url
        self.header = header

    def get(self, endpoint):
        return requests.get(self.base_url+endpoint, headers=self.header)
    
    def post(self, endpoint, payload):
        return requests.post(self.base_url+endpoint, json=payload, headers=self.header)
    
    def put(self, endpoint, payload):
        return requests.put(self.base_url+endpoint, json=payload, headers=self.header)
    
    def delete(self, endpoint):
        return requests.delete(self.base_url+endpoint, headers=self.header)
    

    
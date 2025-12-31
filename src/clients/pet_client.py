from src.utils.api_base import APIBase
from src.config.config import base_url, header


class Petclient(APIBase):

    def __init__(self):
        super().__init__(base_url, header)

    #create Pet using ID
    def add_petbyID(self, payload):
        return self.post("/pet", payload)
    


    

class Result:
    def __init__(self, id = None, success = None, message = None, url = None, data = None) -> None:
        self.id = id
        self.success = success
        self.message = message
        self.url = url
        self.data = data

    def to_json(self):
        json_data = None

        if (self.data and hasattr(self.data, '__dict__')):
           json_data = vars(self.data) 
           
        return {
            "id": self.id,
            "success": self.success,
            "message": self.message,
            "url": self.url,
            "data": json_data  
        }
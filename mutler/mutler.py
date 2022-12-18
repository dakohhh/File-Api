import os

class Mutler():
    def __init__(self, _folder_name:str="upload", def_file_size:int=None):
        self.folder_name = _folder_name
        self.def_file_size = def_file_size

        try:
            os.makedirs(self.folder_name)
        except OSError:
            pass


    async def put(self ,file_id:str, data:bytes)-> None:
        try:
            with open(os.path.join(os.getcwd(), f"{self.folder_name}/{file_id}"), "wb") as f:
                f.write(data)
                f.close()
        except:
            raise Exception

    async def get(self, file_id:str):
        try:
            data = None
            with open(os.path.join(os.getcwd(), f"{self.folder_name}/{file_id}"), "rb") as f:
                data = f.read()

            return data
        except FileNotFoundError:
            return False






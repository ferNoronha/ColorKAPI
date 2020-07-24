from fastapi import FastAPI, File, UploadFile, Body
from pallet import Pallet
import base64
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    data: str
    k: int

#data: str = Body(...)
@app.post("/clustering")
async def process(item: Item):
    centers = []
    error = []
    #print(item.data)
    if item is not None and item.data is not None and item.data!="":
        try:
            if item.k == 0:
                k = 5
            else:
                k = item.k
            colors = Pallet(k)
            #file64 = item.data.split(',')
            #print(len(file64))
            #if len(file64)>1:
            file64 =  item.data.encode()
            b64_string = file64.decode()
            centers,error = colors.process(b64_string)
            #else:
            #    error.append('split error')
        except ValueError:
            error.append(ValueError)
    else:
        error.append("data is none")
    
    return {"data":centers, "errors":error}

@app.get("/")
async def root():
    return {"message": 200}


# if __name__ == '__main__':
#     uvicorn.run(app,host='127.0.0.1',port='8000')
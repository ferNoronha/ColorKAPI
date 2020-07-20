# ColorKAPI

ColorKAPI was develop to clustering and return the five top colors of an image.
Was develop by Fernando Noronha and Murilo Paulino.


## Installation

For this example, we used conda enviroment with python version 3.7.8.
```bash
conda create myenv python=3.7.8
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install requirements.txt
```
Note: If you are in Linux Machine, you have to install some packeges for opencv:
```bash
sudo apt-get update
sudo apt-get isntall libsm6 libxrender1 libfontconfig1 libice6
```

## Usage

This API have two methods, one method root and another with image process:
```python
@app.post("/clustering/")
async def process(item: Item):
     ...

@app.get("/")
async def root():
     ...
```

To clustering image, you have to send a post request json with the base64 image format to the process method, you can call this method with your {server ip + /clustering} or call the heroku url {https://colork.herokuapp.com/clustering}. The base64 format is splited by "data:image/{format};base64,{base64 encoded string}":
```json
{
     "data":"data:image/png;base64,....."
}
```

This will return a json object with the five top color cluster and the list of errors:
```json
{
     "message":[{"R":R,"G":G,"B":B},{"R":R,"G":G,"B":B},{"R":R,"G":G,"B":B},{"R":R,"G":G,"B":B}],
     "errors":[]
}
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

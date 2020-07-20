import cv2
import numpy as np
import base64
import io
from imageio import imread


class Pallet:
    def __init__(self):
        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        self.K = 5
    
    def process(self,encode):
        error = []
        try:
            img = imread(io.BytesIO(base64.b64decode(encode)))
            cv2_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            #pltimg = cv2.resize(img,(416,416))
            center = self.Kmeans(cv2_img)
        except ValueError:
            error.append(ValueError)
        return center, error
    


    def Kmeans(self, img):
        try:
        image = cv2.resize(img, (200,200))
        np_image = image.reshape((-1,3))
        np_image = np.float32(np_image)
        ret,label,center = cv2.kmeans(np_image, self.K,None,self.criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        
        
        colors, count = np.unique(label.flatten(),return_counts= True)
        
        union = dict(zip(colors,count))
        
        center = np.uint8(center)
        #print(center)
        centers = []
        for key,value in sorted(union.items(), key= lambda x : x[1]):
            centers.append(center[key].tolist())
        
        cent = []
        for i in centers:
            obj = {
                'R':i[2],
                'G':i[1],
                'B':i[0]
            }
            cent.append(obj)
        
        return cent


if __name__ == "__main__":
    colors = Pallet()
    #img = cv2.imread(r'D:\Documentos\DiscoC\brincadeira\ocean.jpg')
    #with open(r'D:\Documentos\DiscoC\brincadeira\ocean.jpg', "rb") as fid:
    #    data = fid.read()
    #b64_bytes = base64.b64encode(data)
    #print(b64_bytes)
    
    #teste = 'data:image/png;base64,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'
    #teste = 
    
    #print(type(teste))
    # b64_string = teste.decode()
    # img = imread(io.BytesIO(base64.b64decode(b64_string)))
    # cv2_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # cv2.imshow('teste',cv2_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    
    #jpg_as_text = base64.b64encode(buffer)
    #centers,error = colors.process(img)    
    #print(centers)
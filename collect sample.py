import cv2
import numpy as np
from os import listdir
from os.path import isfile,join

path= './Nehal/'

#We use listdir to get all fles and directories of the path.
#We use isfile to take only files and not directories.
photos= [f for f in listdir(path) if isfile(join(path,f))]

type(photos)      #list
type(photos[0])   #string

#Now create empty arrays to store the photos and labels.
Training_data,Labels = [],[]

for i,files in enumerate(photos):    #Enumerate used to store counter and files
    photo_path= path + files
    photo = cv2.imread(photo_path,cv2.IMREAD_GRAYSCALE)
    
    Training_data.append(np.asarray(photo))
    Labels.append(i)
    
#Convert Labels to numpyarray
Labels= np.asarray(Labels,dtype= np.int32)

type(photo)

Labels

type(Labels)

type(Training_data)

Training_data

Training_data = np.asarray(Training_data)

#Now train the model using LBPH function

sudeep_model= cv2.face_LBPHFaceRecognizer.create()

sudeep_model.train(Training_data,Labels)
print('Model trained successfully')
import cv2, os

folderPath = os.getcwd()

list1 = os.listdir(folderPath +"/Image Buffer")
print('Proses',len(list1),"gambar")
count = 1
for l in list1:
    img = cv2.imread("Image Buffer/"+l,1)
    img2 = cv2.resize(img,(1536,1024))
    cv2.imwrite("Output Image/"+ l,img2)
    print(count,"/",len(list1))
    count+=1
print("Selesai gais")
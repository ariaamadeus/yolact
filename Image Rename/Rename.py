import cv2, os

folderPath = os.getcwd()

list1 = os.listdir(folderPath +"/Image Buffer")
print('Proses',len(list1),"gambar")
count = int(input('Start From:'))+1
forname = ''
for l in list1:
    if count<=10:
        forname = "00000"+str(count-1)
    elif count<=100:
        forname = "0000"+str(count-1)
    elif count<=1000:
        forname = "000"+str(count-1)
    elif count<=10000:
        forname = "00"+str(count-1)
    elif count<=100000:
        forname = "0"+str(count-1)
    else:
        forname = str(count-1)
    img = cv2.imread("Image Buffer/"+l,1)
    cv2.imwrite("Output Image/"+forname+".JPG",img)
    print(l,">>>",forname+".JPG")
    count+=1
print("Selesai gais")
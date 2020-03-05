import numpy as np
import cv2

#read in the image
path="Resources/book.jpg"
img=cv2.imread(path)
#declare the variables of circles and counter
circles=np.zeros((4,2),np.int)
counter=0
#creat a function for the mousepoints
def mousepoints(event,x,y,flags,params):
    global counter
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)

        circles[counter]=x,y
        counter = counter + 1
        print(circles)


#creat a while loop for getting the actual points
while True:
    if counter==4:

        #declare the second points(the crossponding points)
        width,height=400,355
        pts1=np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2=np.float32([[0,0],[width,0],[0,height],[width,height]]) #be sure to follow that order while clincking on image
        # creat a matrix that allow us to get the prespective
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        # creat output image:
        output = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("output",output)
    #creating a for loop for drawing the circles on the img
    for x in range (0,4):
        cv2.circle(img,(circles[x][0],circles[x][1]),2,(0,0,255),8,cv2.FILLED)

    #showing the image with clicks
    cv2.imshow("books",img)
    cv2.setMouseCallback("cards",mousepoints)#this function takes two params, the first one is the image the 2nd is the mousepoint function
    cv2.waitKey(1)



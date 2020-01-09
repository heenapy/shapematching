# _______________________shapematching mini project_________________________
import cv2
image = cv2.imread('sh1.png')
gary = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('Identifying shape',image)
cv2.waitKey()

ret, thresh = cv2.threshold(gary,127,255,1)

contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

    if len(approx)==3:
        shape_name = 'Triangle'
        cv2.drawContours(image,[cnt],0,(0,255,0),-1)
        m=cv2.moments(cnt)
        cx=int(m['m10']/m['m00'])
        cy=int(m['m01']/m['m00'])
        cv2.putText(image,shape_name,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)

    elif len(approx)==4:
        x,y,w,h = cv2.boundingRect(cnt)
        m = cv2.moments(cnt)
        cx = int(m['m10'] / m['m00'])
        cy = int(m['m01'] / m['m00'])

        if abs(w-h)<=3:
            shape_name = 'Square'
            cv2.drawContours(image, [cnt], 0, (0, 125, 255), -1)
            cv2.putText(image, shape_name, (cx - 50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        else:
            shape_name = 'Rectangle'
            cv2.drawContours(image, [cnt], 0, (0, 0, 255), -1)
            m = cv2.moments(cnt)
            cx = int(m['m10'] / m['m00'])
            cy = int(m['m01'] / m['m00'])
            cv2.putText(image, shape_name, (cx - 50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    elif len(approx)==10:
        shape_name = 'Star'
        cv2.drawContours(image, [cnt], 0, (255, 255, 0), -1)
        m = cv2.moments(cnt)
        cx = int(m['m10'] / m['m00'])
        cy = int(m['m01'] / m['m00'])
        cv2.putText(image, shape_name, (cx - 50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    elif len(approx)>=15:
        shape_name = 'circle'
        cv2.drawContours(image, [cnt], 0, (0, 255, 255), -1)
        m = cv2.moments(cnt)
        cx = int(m['m10'] / m['m00'])
        cy = int(m['m01'] / m['m00'])
        cv2.putText(image, shape_name, (cx - 50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
cv2.imshow('Identifying shape',image)
cv2.waitKey()
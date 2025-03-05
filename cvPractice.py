import cv2 as cv
import sys
 
img = cv.imread(cv.samples.findFile(r"C:\Users\azizb\Documents\CSCI270\myenv\Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg.webp"))
 
if img is None:
 sys.exit("Could not read the image.")
 
cv.imshow("Display window", img)
k = cv.waitKey(0)
 
if k == ord("s"):
 cv.imwrite("starry_night.png", img)
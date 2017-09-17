
import sys 
import os 
import datetime
import cv2 
import imutils
import logging 
logger = logging.getLogger(__name__)

def split_into_folders(path):
    folders = []
    while 1:
        path, folder = os.path.split(path)

        if folder != "":
            folders.append(folder)
        else:
            if path != "":
                folders.append(path)
            break
    return folders 
    
def rotate(input_img_path, output_img_path, degrees):
    rotated_img = imutils.rotate_bound(cv2.imread(input_img_path), degrees)
    cv2.imwrite(output_img_path, rotated_img)

def tif_to_jpg(input_img_path, output_img_path):
    cv2.imwrite(output_img_path, cv2.imread(input_img_path), [int(cv2.IMWRITE_JPEG_QUALITY), 60])

def process_image_post_stitching(input_img_path, output_img_path):
    try:
        tif_to_jpg(input_img_path, output_img_path)
    #stiching 
    except:
        print("Did not find image in 
    # only rotate 90 degrees for the Powell street parking mission 
    if "1" in split_into_folders(output_img_path):
        rotate(output_img_path, output_img_path, -90)

def process_mission_post_stitching(mission, ymd, hms):
    base_path_str = "static,images,{0},{1},{2}".format(mission, ymd, hms).split(",")
    base_path = os.path.join(*base_path_str)
    input_img_path = os.path.join(base_path, "stitched.tif")
    output_img_path = os.path.join(base_path, "compressed.jpeg")
    
    print("Processing from {0} ==>\n  {1}".format(input_img_path, output_img_path))
    process_image_post_stitching(input_img_path, output_img_path)    
    
def resize(input_img_path, output_img_path):
    input_image = cv2.imread(input_img_path)
    
    #compress 
    cv2.imwrite(output_img_path, input_image, [int(cv2.IMWRITE_JPEG_QUALITY), 70])

def resize_raw_directory(dir_path):
    raw_dir_path = os.path.join(dir_path, "raw")
    all_files = os.listdir(raw_dir_path)
    for file_name in all_files:
        file_path = os.path.join(raw_dir_path, file_name)
        resize(file_path, os.path.join(dir_path, file_name))

        import cv2

def count_cars(input_img_path, output_img_path, xml_file):        
    # Trained XML classifiers describes some features of some object we want to detect
    car_cascade = cv2.CascadeClassifier(xml_file) #cloned from https://github.com/andrewssobral/vehicle_detection_haarcascades/blob/master/cars.xml
    
    img = cv2.imread(input_img_path)
    # convert to gray scale of each frames
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     
 
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(img_gray, 1.1, 1)
     
    # To draw a rectangle in each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(img_gray,(x,y),(x+w,y+h),(0,0,255),2)
 
 
    cv2.imwrite(output_img_path, img_gray, [int(cv2.IMWRITE_JPEG_QUALITY), 70])

if __name__ == '__main__':
    '''
    process_mission_post_stitching("1", "20170913", "130000")
    process_mission_post_stitching("1", "20170913", "131500")
    process_mission_post_stitching("1", "20170914", "191500")
    process_mission_post_stitching("1", "20170914", "193000")
    
    process_mission_post_stitching("2", "20170914", "184500")
    process_mission_post_stitching("2", "20170914", "190000")
    process_mission_post_stitching("2", "20170914", "191500")
    
    process_mission_post_stitching("3", "20170914", "184500")
    process_mission_post_stitching("3", "20170914", "190000")
    process_mission_post_stitching("3", "20170914", "191500")
    '''
    '''
    resize_raw_directory("C:\\Users\\daniel.cheng\\Downloads\\MasterDocuments\\AllOther\\3_Programming\\danielmcheng1_repos\\drone\\static\\images\\1\\20170913\\130000")
    resize_raw_directory("C:\\Users\\daniel.cheng\\Downloads\\MasterDocuments\\AllOther\\3_Programming\\danielmcheng1_repos\\drone\\static\\images\\1\\20170913\\131500")###diff exposures is bad--and diff quality in images ==> COPIED IN FILE MANUALLY
    #resize_raw_directory("C:\\Users\\daniel.cheng\\Downloads\\MasterDocuments\\AllOther\\3_Programming\\danielmcheng1_repos\\drone\\static\\images\\1\\20170914\\190000")###too little overlap? (threw too much overlap warning...) ==> DELETE
    resize_raw_directory("C:\\Users\\daniel.cheng\\Downloads\\MasterDocuments\\AllOther\\3_Programming\\danielmcheng1_repos\\drone\\static\\images\\1\\20170914\\191500")###too dark
    resize_raw_directory("C:\\Users\\daniel.cheng\\Downloads\\MasterDocuments\\AllOther\\3_Programming\\danielmcheng1_repos\\drone\\static\\images\\1\\20170914\\193000")###too dark
    
    resize_raw_directory("C:\\Users\\daniel.cheng\\Downloads\\MasterDocuments\\AllOther\\3_Programming\\danielmcheng1_repos\\drone\\static\\images\\2\\20170914\\184500")#aligned for me!
    resize_raw_directory("C:\\Users\\daniel.cheng\\Downloads\\MasterDocuments\\AllOther\\3_Programming\\danielmcheng1_repos\\drone\\static\\images\\2\\20170914\\190000")###too dark
    resize_raw_directory("C:\\Users\\daniel.cheng\\Downloads\\MasterDocuments\\AllOther\\3_Programming\\danielmcheng1_repos\\drone\\static\\images\\2\\20170914\\191500")###too dark
    
    resize_raw_directory("C:\\Users\\daniel.cheng\\Downloads\\MasterDocuments\\AllOther\\3_Programming\\danielmcheng1_repos\\drone\\static\\images\\3\\20170914\\184500")#too dark and need more pics
    resize_raw_directory("C:\\Users\\daniel.cheng\\Downloads\\MasterDocuments\\AllOther\\3_Programming\\danielmcheng1_repos\\drone\\static\\images\\3\\20170914\\190000")#too dark and need more pics
    resize_raw_directory("C:\\Users\\daniel.cheng\\Downloads\\MasterDocuments\\AllOther\\3_Programming\\danielmcheng1_repos\\drone\\static\\images\\3\\20170914\\191500")#too dark and need more pics
    '''
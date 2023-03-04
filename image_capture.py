import cv2
import numpy as np

from pathlib import Path

# Settings
file_num = 0
save_path = "./new_images/"      # Save images to subfolders of current directory
file_suffix = ".png"  # Extension for image file
TO_COUNTDOWN = 3


def validate_folder(folderPath):
    
    Path(folderPath).mkdir(parents=True, exist_ok=True)


def file_exists(filepath):
   #Returns true if file exists, false otherwise.
  
    try:
        f = open(filepath, 'r')
        exists = True
        f.close()
    except:
        exists = False
    return exists
 
def get_filepath(folder):
    #    Returns the next available full path to image file
    
    global file_num
    # Loop through possible file numbers to see if that file already exists
    filepath = folder + str(file_num) + file_suffix
    while file_exists(filepath):
        file_num += 1
        filepath = folder + str(file_num) + file_suffix
    
    return filepath
 
def main():
    quitAllTheWay = False
    num_images = 0
    countdown = TO_COUNTDOWN
    image_classes = 0 
    while image_classes <= 0:
        try:
            image_classes = int(input("How many different classes of image would you like to train today? "))
            
        except:
            print("That wasn't a number")

        if image_classes < 0 :
            raise SystemExit
        
    class_names = list()

    for i in range(0,image_classes,1):
        class_names.append(input("What is the name of class %s? " % i))

    cam = cv2.VideoCapture(0)

    for thisClass in class_names:
        if quitAllTheWay :
            break
        
        tFolder = save_path + str(thisClass) + "/"
        validate_folder(tFolder) 

        
    
        # Figure out the name of the output image filename
        filepath = get_filepath(tFolder) 
        
    
        # Set smaller resolution
        #cam.set(cv2.CAP_PROP_FRAME_WIDTH, 160) # 640
        #cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 120) # 480
    
        # Initial countdown timestamp
        countdown_timestamp = cv2.getTickCount()
    
        while cam.isOpened():
            # Read camera
            ret, frame = cam.read()
    
            # Get timestamp for calculating actual framerate
            
            # Frame resolution
            frame_height = frame.shape[0]
            frame_width = frame.shape[1]
    
            # Crop center of image
            new_size = 720
            start_y = 0
            end_y = 720
            start_x = 0
            end_x = 720
            # Crop
            cropped = frame[start_y:end_y, start_x:end_x]
    
            # Rezise to 96*96
            resized = cv2.resize(cropped, (720,720), interpolation=cv2.INTER_CUBIC)
    
            # Put text only on copied image
            copy = resized.copy()
            # Draw count of images shot on image
            cv2.putText(copy, thisClass,(10,50), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255),2)
            cv2.putText(copy, 
                        str(num_images),
                        (round(resized.shape[1] / 2) - 15, round(resized.shape[0] / 2)+10),
                        cv2.FONT_HERSHEY_PLAIN,
                        4,
                        (255, 255, 255),2)
            
    
            # Display raw camera image
            cv2.imshow('Kaamera', copy)
    
            keyPressed = cv2.waitKey(10)
            if keyPressed == ord('n'):
                # Press 'n' to move to next image type
                break
            elif keyPressed == ord('q'):
                # Press 'q' to exit
                quitAllTheWay = True
                break

            timestamp = cv2.getTickCount()
    
            # Each tenth second, decrement countdown
            if (timestamp - countdown_timestamp) / cv2.getTickFrequency() > 0.1: # switching this to tenths of a second to up framerate to 10fps
                countdown_timestamp = cv2.getTickCount()
                countdown -= 1
                
                # When countdown reaches 0, break out of loop to save image
                if countdown <= 0:
                    # Get new image file name
                    filepath = get_filepath(tFolder)
                    # Save image
                    outputSize = cv2.resize(resized,[214,214])
                    cv2.imwrite(filepath, outputSize)
                    # Start new count down
                    countdown = TO_COUNTDOWN
                    num_images += 1
                    #break
 
 
    # Clean up
    cam.release()
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    print('To move to the next class activate the camera window and press "n"')
    print('To Quit press "q"')
    main()
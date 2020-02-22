'''
PYTHON CODE TO DETECT BLUR IMAGES AND MOVE THEM INTO SEPARATE FOLDER
'''

# import the necessary packages
from imutils import paths
import cv2
import shutil

# compute the Laplacian of the image and then return the focus measure (result), which is simply the variance of the Laplacian
def variance_of_laplacian(image):
	
	return cv2.Laplacian(image, cv2.CV_64F).var()
	
def blur():
	images_dir= r'M:\\Tericsoft\\ashish\\blur_detection_of_images\\images\\'
	blur_folder = r'M:\\Tericsoft\\ashish\\blur_detection_of_images\\blur_folder\\'
	non_blur_folder = r'M:\\Tericsoft\\ashish\\blur_detection_of_images\\non_blur_folder\\'
	threshold= 100 #declare descent threshold for detecting blur images

	# loop over the input images
	for each_image in paths.list_images(images_dir):
		# load the image, convert it to grayscale, and compute the focus measure (result) of the image using the Variance of Laplacian method
		image = cv2.imread(each_image)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		result = variance_of_laplacian(gray)
		text = "Not Blurry"

		if result < threshold:
			text = "Blurry"
			print(each_image)
			shutil.copy(each_image, blur_folder)
		else:
			shutil.copy(each_image, non_blur_folder)

		# put the result text on the image for better UI
		cv2.putText(image, "{}: {:.2f}".format(text, result), (10, 30),
			cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
		cv2.imshow("Image", image) #visualise the resultant image with its text
		key = cv2.waitKey(0)
blur()
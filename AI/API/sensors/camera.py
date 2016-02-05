# need this for camera
import cv2

class camera: 

	# may not need a constructor here
	def __init__(self): pass

	def read(self):

		# set camera?
		self.camera = cv2.VideoCapture(0)

		# ret and frame? what does read return?
		ret, frame = self.camera.read()

		# write to a file, why do we need frame?
		cv2.imwrite("image1.jpeg", frame)

		# release the camera
		self.camera.release()

		# close cv2?
		cv2.destroyAllWindows()

cam = camera()
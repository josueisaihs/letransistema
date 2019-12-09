#!/urs/bin/env python
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import sys
import cv2
import zbar
from PIL import Image
import gpio_control_led as led
from middle import Analisis
import re

print '\n\n.:. Esperando ...'
time.sleep(5)

# Raspberry Name
raspberry = sys.argv[1]

# Server
server = sys.argv[2]

# Local
local = sys.argv[3] == "True"

# Mode
DEBUG = True
SCREEN = False
if len(sys.argv) > 1:
	if sys.argv[-1] == "DEBUG":
		DEBUG = sys.argv[-1] == "DEBUG"
	else:
		SCREEN = sys.argv[-1] == 'SCREEN'

# Configuration options
FULLSCREEN = not DEBUG
if not DEBUG:
	RESOLUTION = (640, 480)
else:
	RESOLUTION = (480, 270)

# Initialise Raspberry Pi camera
camera = PiCamera()
camera.resolution = RESOLUTION
#camera.framerate = 10
#camera.vflip = True
#camera.hflip = True
#camera.color_effects = (128, 128)
# set up stream buffer
rawCapture = PiRGBArray(camera, size=RESOLUTION)
# allow camera to warm up
time.sleep(0.1)
print "\n\n.:. PiCamera lista"

# Initialise OpenCV window
if SCREEN:
	if FULLSCREEN:
		cv2.namedWindow("Lector de Codigo de Barras y QR", cv2.WND_PROP_FULLSCREEN)
 		cv2.setWindowProperty("Lector de Codigo de Barras y QR", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
	else:
		cv2.namedWindow("Lector de Codigo de Barras y QR")

# print "Version del OpenCv: %s" % (cv2.__version__)
print "\n\n.:. ElijoSoft"
print "\n\n.:. Presiona q para salir ...\n\n"

scanner = zbar.ImageScanner()
scanner.parse_config('enable')

analisis = Analisis(raspberry)
# time.sleep(1)
# analisis.start()

led.encender(18)
# Capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    led.apagar()
    # as raw NumPy array
    output = frame.array.copy()

    # raw detection code
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY, dstCn=0)
    pil = Image.fromarray(gray)
    width, height = pil.size
    raw = pil.tobytes()

    # create a reader
    image = zbar.Image(width, height, 'Y800', raw)
    scanner.scan(image)

    # extract results
    for symbol in image:
        # do something useful with results
        # print 'Dato: "%s"' % symbol.data
	# led.encender()
	cod = re.compile(r'\d{11}')
	cod = cod.findall("%s" % symbol.data)
	if len(cod) > 0:
		if analisis.addStock(cod[0]):
			led.encender()


    # show the frame
    if SCREEN:
    	cv2.imshow("Camara", output)

    # clear stream for next frame
    rawCapture.truncate(0)

    # Wait for the magic key
    keypress = cv2.waitKey(1) & 0xFF
    if keypress == ord('q'):
    	break

# When everything is done, release the capture
led.apagar(18)
camera.close()
analisis.close()
if SCREEN:
	cv2.destroyAllWindows()

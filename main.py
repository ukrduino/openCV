import camera
import driver

driver.init()
driver.light(True)
driver.forward(1)
camera.capture_image('image.jpg')
driver.light(False)
driver.clean()

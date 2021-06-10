from pypresence import Presence # The simple rich presence client in pypresence
import time
from datetime import datetime
import pystray
from pystray import Menu as menu, MenuItem as item
from PIL import Image
import threading
import os
import sys



#icon = pystray.Icon('Coco Countdown')

client_id = "852064961655865395"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client


#bye = False

#icon.icon = img

RPC.connect()
def rpc():
   while True: 
    
            #while True:  # The presence will stay on as long as the program is running
    time.sleep(3) # Can only update rich presence every 15 seconds
    later = datetime(2021, 7, 1, 19, 0, 0)        # Random date in the past
    now  = datetime.now()                         # Now
    duration = later - now                         # For build-in functions
    duration_in_s = duration.total_seconds()

    days    = divmod(duration_in_s, 86400)        # Get days (without [0]!)
    hours   = divmod(days[1], 3600)               # Use remainder of days to calc hours
    minutes = divmod(hours[1], 60)                # Use remainder of hours to calc minutes
    seconds = divmod(minutes[1], 1)               # Use remainder of minutes to calc seconds
    print("%d:%d:%d:%d" % (days[0], hours[0], minutes[0], seconds[0]))
    RPC.update(state="%02d:%02d:%02d:%02d" % (days[0], hours[0], minutes[0], seconds[0]), details="Time until Coco's graduation:", large_image="coco") # Updates our presence
   else:
    exit()

def exit_action(icon):
    print('exit!')
    icon.visible = False
    icon.stop()
    #bye=True
    exit()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
  
def run_icon():

    #icon.run()
   
    img = Image.open(resource_path("coco.png"))
    icon = pystray.Icon('test')
    icon.menu =menu(
        item('Exit', lambda : exit_action(icon)),
    )
    icon.icon = img
    icon.title = "Coco Countdown"
    icon.run()
    print('icon running')
  
if __name__ == "__main__":
    print("ID of process running main program: {}".format(os.getpid()))
  
    # print name of main thread
    print("Main thread name: {}".format(threading.current_thread().name))
    # creating thread
    t1 = threading.Thread(target=rpc)
    t2 = threading.Thread(target=run_icon)

    t1.daemon = True
     
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
  
    # wait until thread 1 is completely executed
    # wait until thread 2 is completely executed
    t2.join()
    sys.exit()
    # both threads completely executed
    print("Done!")






    










# Update the state in `on_clicked` and return the new state in
# a `checked` callable
#icon('test', img, menu=menu(
 #   item(
  #      'Enable Discord Presence',
   #     lambda icon, item: icon.notify('Hello World!')))).run()






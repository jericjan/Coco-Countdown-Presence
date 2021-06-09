from pypresence import Presence # The simple rich presence client in pypresence
import time
from datetime import datetime
client_id = "852064961655865395"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client

RPC.connect() # Start the handshake loop










while True:  # The presence will stay on as long as the program is running
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

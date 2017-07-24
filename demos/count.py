###########################################################################
# Setup code goes below, this is called once at the start of the program: #
###########################################################################
import time
print('Hello world! I can count:')
i = 1

while True:
    ###################################################################
    # Loop code goes inside the loop here, this is called repeatedly: #
    ###################################################################
    print(i)
    i += 1
    time.sleep(1.0)  # Delay for 1 second.


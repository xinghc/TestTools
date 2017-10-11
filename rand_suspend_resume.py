import os
import time
import random
import sys
import signal
test_terminate = False

def sigint_signal_handler(signal, frame):
    global test_terminate
    sys.stdout.write("\t\t ...... Quitting from the test")
    sys.stdout.flush()
    test_terminate = True

if len(sys.argv) != 2:
    print("Usage: %s [debug tool command]" % sys.argv[0])
    sys.exit(2)
signal.signal(signal.SIGINT, sigint_signal_handler)
test_cnt = 1

while True:
    sys.stdout.write("\rTarget board suspend:\t%s" % str(test_cnt))
    sys.stdout.flush()
    os.system("echo \"========= %s => %s ========\" > /dev/ttyUSB2"%
            (time.ctime(), str(test_cnt)) )
    resume_pause = random.uniform(0.5, 6.0)
    os.system("echo \"======== pause: %s =======\" > /dev/ttyUSB2"%
            str(resume_pause) )
    time.sleep(1)
    sys.stdout.write("\rTarget board resume :\t%s" % str(test_cnt))
    sys.stdout.flush()
    os.system("echo \"echo mem > /sys/power/state\" > /dev/ttyUSB2")
    if test_terminate:
        print "\nUser terminated the test\n"
        break
    time.sleep(random.uniform(1.0, 5.0))
    os.system("%s onkey" % sys.argv[1] )
    time.sleep(resume_pause)
    test_cnt += 1

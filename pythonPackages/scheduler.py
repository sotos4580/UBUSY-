#Main python module for executing scheduling tasks
from twisted.internet import task, reactor

#----- Multi File Integration -----#
import firebasenet
#----- End Multi File Integration -----#


#Set scheduling timeout
_timeout = 1.0

def runMainThread():
    firebasenet.pushData()
    pass

l = task.LoopingCall(runMainThread)
l.start(_timeout) # Call Timeout Code

reactor.run()

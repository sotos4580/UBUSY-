#Networking integration to firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time

#----- Multi File Integration -----#
#----- End Multi File Integration -----#


# Function for current time in minutes from timestamp
current_min_time = lambda: int(round(time.time()) / 60)


#----- Initialize Credentials -----#
cred = credentials.Certificate('serviceWorker.json') #Pull hashed data from service worker
firebase_admin.initialize_app(cred)

db = firestore.client() #Init. firestore as admin
#----- End Credential Init. -----#

def pushData():
    import netscanning

    count = netscanning.count_active_hosts()
    doc_ref = db.collection('postProcessed').document('collection')
    doc_ref.set({
        'Time': current_min_time(),
        'People': count
    })

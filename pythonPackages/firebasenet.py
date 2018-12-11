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

def pushData(docCount):
    import netscanning
    docName = "doc" + str(docCount)

    count = netscanning.count_active_hosts()
    doc_ref = db.collection('preProcessed').document(docName)
    doc_ref.set({
        'Time': current_min_time(),
        'People': count
    })

def getCount():
    peopleLists = []
    timeLists = []
    docs = ["doc0", "doc1", "doc2", "doc3", "doc4", "doc5", "doc6", "doc7", "doc8", "doc9"]
    for i in range(10):
        doc_ref = db.collection('preProcessed').document(docs[i])
        try:
            doc = doc_ref.get()
            docData = (u'Document data: {}'.format(doc.to_dict()))
            docData = docData.split()
            for i in range(len(docData)):
                if docData[i] == "{'People':":
                    peopleLists.append(docData[i + 1])
                if docData[i] == "'Time':":
                    timeLists.append(docData[i + 1])
        except google.cloud.exceptions.NotFound:
            print(u'No such document!')

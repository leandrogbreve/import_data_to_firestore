import sys
import getopt
import json
import firebase_admin
from firebase_admin import credentials, firestore

# SUBCOLLECTIONS ARE NOT SUPPORTED

cred = credentials.Certificate("config/access_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# read file "data.json" which must contain the json with collection and docs to be imported.
# check readme for example

def main(argv):
    with open('./data.json') as file:
        data = json.load(file)

        # first level of file refers to a collection
        for collection in data:
            # second level refers to each doc to be inserted in a collection
            for doc in data[collection]:
                # If needed, add fields into the doc being imported here,

                # If --timestamps flag was passed by the user, the fields "createdAt" 
                # and "uploadedAt"  will be inserted in the doc with the current server timestamp
                if('--timestamps' in argv):
                    doc['createdAt'] = firestore.SERVER_TIMESTAMP
                    doc['uploadedAt'] = firestore.SERVER_TIMESTAMP

                # adds the doc to the firestore database
                db.collection(collection).document().set(doc)


if __name__ == '__main__':
    main(sys.argv)

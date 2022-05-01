## Easily insert data into Firestore

This simple python program intends to help import data to Google Firestore database in order to facilitate excersises and to input data for test environment, instead of having to input each doc and field manually in the Firebase console UI.

1. The key file must be in "config" folder with name "access_key.json" ( config/access_key.json)
2. The json file with data to be imported must be in the root folder named as "data.json", the structure is: { collection: [ docs ], collection: [ docs ], collection: [ docs ] }

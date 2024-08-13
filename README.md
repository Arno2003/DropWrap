
# DropWrap

A Hierarchical clustering based analysis for dropouts of various regions, with impressions of factors resulting in dropouts calculated using RNN.


## Software/Library Specifications

**Fron-tend:**

**Backend :**
Python: 3.8.0
||
pandas : 1.5.3
||
scipy : 1.10.1
||
numpy : 1.24.0
||
scikit-learn  : 1.2.1
||
matplotlib : 3.5.3
||
tensorflow : 2.11.0


**DataBase:** MongoDB : 
## Deployment

First we need to prepare the data, for which we need to switch to BackEnd directory. Execute : 

```bash
cd BackEnd
```

To generate the clustering data, run the following command

```bash
cd main
python Main.py
```

To generate impressions of factors leading to dropout, execute:

```bash
cd RNNCode
python softmax.py
```

Now the data processing is complete, now we need to upload the data into our MongoDB database

```bash
cd ../../database
python uploadToDb.py
```
Now that we are done with running our ML models and uploading useful data to our database, we will run our next app locally.

```bash
cd frontend
```
Installing all dependencies:

```bash
npm i
```
Running the app in http://localhost:3000/

```bash
npm run dev
```

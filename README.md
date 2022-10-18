# ML-MINI-PROJECT-API

## Dataset 

``` https://www.kaggle.com/competitions/nlp-getting-started/data?select=train.csv ```

Accuracy achieved: 80.44%

collab Notebook link Training - `https://colab.research.google.com/drive/1NoBShinYljfw_sEKyF0TEDzGdlfaZRsT?usp=sharing`

collab Notebook link Inference - `https://colab.research.google.com/drive/1ThpOIpY33l3WXFGH9QAlX0BmE67pTZNK?usp=sharing`

# Setup [Docker]

## Build Docker Image

```docker-compose up```

## Rebuild Docker Image

```docker-compose up --build```

# Setup [Local]

## Model Used - BERT UNCASED 

Download and save the folder in backend/models/

Model link - ``` https://drive.google.com/file/d/1IJBNMt2pGmDxTq2e64rpzDjaz4aAauL7/view?usp=sharing ```

## Installation

- Twint installation

```
pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
```

-  Install requirements

```
pip install -r requirement.txt 
```

## Backend - FLASK

### If you want to start a new session od db

- Delete the db.sqlite file in backend folder
- Run the following commands

```
python init_db.py
```

```
cd backend
python app.py
```
# ML-MINI-PROJECT-API

## Dataset 

``` https://www.kaggle.com/competitions/nlp-getting-started/data?select=train.csv ```

Accuracy achieved: 80.44%

# Setup

## Model Used - BERT UNCASED 

Download and save the folder in backend/models/

Model link - ``` https://drive.google.com/file/d/1IJBNMt2pGmDxTq2e64rpzDjaz4aAauL7/view?usp=sharing ```

## Installation

```
pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
```

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
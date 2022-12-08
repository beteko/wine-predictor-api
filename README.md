# Wine Quality Predictor API :wine_glass:

API used to estimate the quality of wine using a machine learning model. Its main services are :

 - **Learning**: (Re)Train the wine quality model based on a predefined dataset 
 - **Prediction**: Estimate the quality of a wine based on several preselected features


## Pre-requisite 

- [Git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)
- [Python 3.7+](https://www.python.org/downloads/)
- [pip (package installer for Python)](https://pip.pypa.io/en/stable/installation/) 


## Project structure

```bash
.
├── dataset
│   └── winequality.csv : ................ description
├── src
│   ├── tests
│   │   ├── conftest.py   :  ............. description
│   │   └── test_healthcheck.py : ........ description
│   └── wine_predictor_api :  ............ description
│       ├── security
│       │   └── authentication.py : ...... description
│       ├── services
│       │   ├── healthcheck.py : ......... description
│       │   ├── learner.py :  ............ description
│       │   └── predictor.py :  .......... description
│       └── specs
│           └── openapi_spec.yaml : ...... description
│ 
├── config.template.json :  .............. description
├── dev-requirements.txt :  .............. description
├── launcher.sh :  ....................... description
├── logging.yaml :  ...................... description
├── MANIFEST.in :  ....................... description
├── README.md :  ......................... description
├── requirements.txt :  .................. description
├── setup.cfg :  ......................... description
├── setup.py :  .......................... description
└── VERSION :  ........................... description

```
## Get started  



First, clone this repository locally 

```shell
git clone https://github.com/beteko/wine-predictor-api.git
```

Then, browse into the `wine-predictor-api` directory 


```shell
cd  wine-predictor-api
```

We recommend you create a virtual environment  `venv` 


```shell
python -m venv venv
```

Activate your virtual environment 

```shell
source  venv/bin/activate
```


Update your PIP version and Install all required dependencies 
```shell
pip install -U pip
pip install -r dev-requirements.txt
```

Create your config.json file locally from the template `config.template.json` and fill it accordingly. 
```shell
cp config.template.json config.json
```

> :warning: The `config.json` file should not be committed to the repository as it contains sensitive details


Last, start the API by executing the  `launcher.sh` script
```shell
sh  launcher.sh
```

To access the swagger UI, kindly click on the following link from your preferred browser: [http://localhost:8001/ui](http://localhost:8001/ui)


> :information_source: On the first run, you may have **authenticate** (credentials in your config) then  **train** a model **before** attempting to **estimate** the quality of a wine.



## Tutorial


For further information on how to get started with building such API, we strongly recommend your go through the following tutorial  [How to design a prod-ready API](https://github.com/beteko/tutorials-design-prod-ready-apis/blob/main/README.md) 


## Essential links


- [Connexion Framework](https://github.com/spec-first/connexion)
- [OpenAPI Specification](https://swagger.io/specification/)
- [Logging in Python](https://realpython.com/python-logging/)
- [Flake8: Your Tool For Style Guide Enforcement](https://flake8.pycqa.org/en/latest/)
- [Mypy: Your Static type checker for Python](https://mypy.readthedocs.io/en/stable/)
- [Pytest: Full-featured Python testing tool](https://docs.pytest.org/en/7.2.x/)
- [How to Create a Wheel file for your Python package](https://www.realpythonproject.com/how-to-create-a-wheel-file-for-your-python-package-and-import-it-in-another-project/)
- [Kaggle: More on the 'Red Wine Quality Estimation' Challenge](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)
# Mongo app for variants

Simple flask application with mongo backend for variant searching 

## Installation 

### System requirements

At least Python3.6 and mongo db

1. Example Python installation for [Ubuntu](https://docs.python-guide.org/starting/install3/linux/)

    Example code at time of writing shown, please use link if this is not recent. 

    ```
    # Check python3 version
    python3 --version
    ```

    If Python version is less than 3.6

    ```
    # Add deadsnakes PPA
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    # Update apt
    sudo apt-get update
    # install python3.6
    sudo apt-get install python3.6 
    ```
2. Please see the [mongo db docuementation](https://docs.mongodb.com/manual/installation/) for installation

### Set up of project
1. Clone repository 

    ```
    git clone https://github.com/stefpiatek/mongo-variants.git
    ```

2. With **Python 3.6**, set up virtual environment
    
    ```
    cd mongo-variants
    # Create the virtual environment
    python3.6 -m venv .venv 
    # Enable the virtual environment
    source .venv/bin/activate
    ```

3. Install requirements

    ```
    pip install -r requirements.txt
    ```
    
4. Set up SQLite database
 
     ```
     # in the root of the mongo-variants directory
     python manage.py db upgrade

     ```
5. Run mongo database separately if not already running

     ```
     mongod

     ```
6. Save input data in `mongo-variants/input/all_vep_variants.json`

7. Import data
     ```
     python json_loader.py
     ```

8. Edit secret_info.py, replacing default `SECRET_KEY` and `SECURITY_PASSWORD_SALT` values

## Running the application

1. Run flask app
     ```
     python manage.py runserver

     ```
2. Log in to [http://localhost:5000](http://localhost:5000)

# Quizo

## About the project
This is a simple quiz web application, used to provide generic MCQ Tests. The project was developed as a requirement to pass [ReDi School Munich](https://www.redi-school.org/munich) Backend development course.

## Tech stack
- Backend : 
    - Python v3.10.x or higher
    - FastApi
    - MongoDB
- Frontend : 
    - HTML
    - CSS ( Bootstrap 5 )
    - JavaScript ( JQuery )

## Run the application

### Prerequisites
Python with version 3.10.x or higher installed in addition to pip

### Setting up environment variables 
To set up environment variables create a `.env` file within the source folder and set MongoDB host URL as the following:
```
mongo_db_host = "<YOUR_MONGO_DB_HOST_URL>"
```
### Setting up python virtual environment 
You need to create a new virtual environment within Python to install the required packages by executing the following commands in the root folder of the project within PowerShell :
```
py -m venv ./venv 
.\venv\Scripts\activate
pip install -r ./src/requirements.txt
```
### Running the application
To run the backend, execute the following command within the PowerShell : 
```
cd src | uvicorn main:app --reload 
``` 
To run the frontend, simply open the file `index.html` within   `src/ui` folder 

*Note: you need to be connected to the internet when opening index.html to download frontend libraries from CDN*

### Running the tests
To run the test execute the following commands within Powershell : 
```
pytest -s -q src/test/
```

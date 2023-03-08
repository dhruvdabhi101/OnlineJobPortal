# OnlineJobPortal

## Step to Run this Project 
1. Clone the Repo 
`git clone https://github.com/dhruvdabhi/OnlineJobPortal`

2. cd into the Repo 
`cd OnlineJobPortal`

3. Create Virtual Environment 
`python -m venv venv`

4. Run Virtual Environment
For Linux or Mac : `source venv/bin/activate` 
For Windows : `source venv\bin\activate`

5. Install needed dependencies
`pip install -r requirements.txt`

6. Migrate to the Database 
`python manage.py makemigrations`
`python manage.py migrate`

7. Run the server
`python manage.py runserver`


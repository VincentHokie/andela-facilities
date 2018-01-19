# Andela Facilities

This is an application developed for Andela to manage fellows under their accomodation and the processes around it.

Technologies
--------------------
Python - Django - Django Rest Framework backend
React - Redux front end


Documentation
--------------------

Coming Soon!


Deployment URL
--------------------

Coming Soon!


Python Dependancy
--------------------

Python v3.5.4 used


# Back-end Setup


After cloning, create a virtual environment and install the requirements. For Linux and Mac users:

    $ virtualenv --python=python3 venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt

If you are on Windows, then use the following commands instead:

    $ virtualenv venv
    $ venv\Scripts\activate
    (venv) $ pip install -r requirements.txt
    
## Database Setup
------------

Once installation is complete, we need to set up the postgres database.

**Postgres installation**

Use the OS link that applies to you, if it's not available please go to https://www.google.com

http://www.techrepublic.com/blog/diy-it-guy/diy-a-postgresql-database-server-setup-anyone-can-handle/ [any debian distribution]

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04 [ubuntu 16.04]

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04 [ubuntu 14.04]

https://labkey.org/Documentation/wiki-page.view?name=installPostgreSQLWindows [windows]

https://www.postgresql.org/download/windows/ [official docs windows]

https://www.postgresql.org/download/macosx/ [Mac osx]

If you're more comfortable with a desktop application give this a shot https://www.postgresapp.com

**Database Setup**

To set up the database, please follow this document https://www.codementor.io/devops/tutorial/getting-started-postgresql-server-mac-osx . 

Follow the following instructions to get your database up and running. (Begin from step 3 if postgres is already installed, MacOsX users can use it to both install and set up)

    1. Create role ‘Vince’ with password ‘vince’ (Step 3 A)
    2. Give this role a privilege of CREATEDB (Step 3 A)
    3. Create DB with name ‘andela-flask-api’ (Step 3 B)

The following must be done with **ALL** the above steps completed.
Execute these commands in the order they appear.

\#4 will ensure the application models are added to your database

    4. cd accomodations && python manage.py migrate


## Running
-------

To run the server use the following command:

    (venv) $ cd accomodations && python manage.py runserver

Then from a different terminal window you can send requests or an API test client like Postman.


# Front-end Installation

Ensure you have node installed.

From the project root, (and in a new terminal tab) enter the **react-client** directory and install npm dependacies:

    $ cd react-client
    $ npm install

and to run the application front-end, run

    $ npm run dev


## Running
-----------------

To run the server use the following command:

    $ npm run dev

Fire up a browser, go to http://localhost:8080/ and play!


## API Documentation
-----------------

The following routes are accessible publicly i.e. you don't need to log in.

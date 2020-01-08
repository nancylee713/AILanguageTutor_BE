# Language Learner
A RESTful JSON API that stores and delivers grammar and vocabulary content based on skill level. The frontend associated with this API can be found [here](https://github.com/nancylee713/AILanguageTutor_FE). 

[Live Demo](http://language-learner-be.herokuapp.com/swagger)

### Get Started
<details>
 <summary> Installation </summary>

 (this is  assuming you have home brew)
 1. Clone down the repo and then run:
  ```
  $ brew install python3
  ```

  This should add the pip package manager.

 2. Create a virtual environment.
  ```
  $ pip install virtualenv
  $ virtualenv venv -p python3 # this will create venv directory
  $ virtualenv -p python3 venv # this will create bin and include lib dir
  $ source ./venv/bin/activate
  ```

 3. Create a new database named language_learner_dev created.
 ```
 $ psql -c 'CREATE DATABASE language_learner_dev'
 ```

 4. Export environmental variables. Add a .env file with the following:
 ```
 $ export APP_SETTINGS="config.DevelopmentConfig"
 $ export DATABASE_URL="postresql://localhost/language_learner_dev"
 $ touch .env

 # .env
 export APP_SETTINGS="config.DevelopmentConfig"
 export DATABASE_URL="postresql://localhost/language_learner_dev"
 ```

 5. Install dependencies.
 ```
 $ run pip install -r
 ```

 6. Run migration. Initialize and update the tables:
 ```
 $ python3 manage.py db init
 $ python3 manage.py db upgrade
 ```

 7. Run the server.
 ```
 $ flask run
 ```

 You should see the following in your console:

 ```
  * Environment: development

    WARNING: This is a development server. Do not use it in a production deployment.

    Use a production WSGI server instead.

  * Debug mode: off

  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 a. It should be running on localhost:5000
 for installation instructions on other machines:
 https://realpython.com/installing-python
 ```


</details>



### Testing

<details>
  <summary>Unit test</summary>

  ```
  $ python3 manage.py test
  ```
  You should see the following:
  ```
  ----------------------------------------------------------------------
  Ran 2 tests in 0.080s

  OK
  ```

  To see coverage report:
  ```
  $ coverage run tests/test_endpoints.py
  $ coverage report
  ```

</details>



### Use of this API
This api is used to create and login users. Then it is able to return questions based on the specified proficiency level, and whether or not the user has answered them already. Endpoints can be tested with Swagger [here](http://language-learner-be.herokuapp.com/swagger).


 <details>
  <summary> <code>GET</code> all speech questions</summary>

  example request : `GET` `/https://language-learner-be.herokuapp.com/speech_questions`
  <br>
  example successful response:

  ```json
  [
    {
      created_date: "Mon, 06 Jan 2020 21:32:28 GMT",
      id: 1,
      image_url: "https://images.unsplash.com/photo-1487956382158-bb926046304a?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjk5NjI0fQ",
      level: "beginner",
      text: "walk",
      updated_date: "Mon, 06 Jan 2020 21:32:28 GMT",
      },
    {
      created_date: "Mon, 06 Jan 2020 21:32:28 GMT",
      id: 2,
      image_url: "https://images.unsplash.com/photo-1524678516592-b3fbf8938717?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjk5NjI0fQ",
      level: "beginner",
      text: "eat",
      updated_date: "Mon, 06 Jan 2020 21:32:28 GMT",
    },
    ...
  ]
  ```
</details>

---

<details>
  <summary> <code>GET</code> all grammar questions</summary>
  example request : `GET` `/https://language-learner-be.herokuapp.com/grammar_questions`
  <br>
  example successful response:

  ```json
  [
    {
      created_date: "Mon, 06 Jan 2020 14:52:54 GMT",
      id: 1,
      level: "beginner",
      text: "Have you make dinner yet?",
      updated_date: "Mon, 06 Jan 2020 14:52:54 GMT",
      },
    {
      created_date: "Mon, 06 Jan 2020 15:07:57 GMT",
      id: 2,
      level: "beginner",
      text: "How many biscuits is there in the tin?",
      updated_date: "Mon, 06 Jan 2020 15:07:57 GMT",
    },
    ...
  ]

  ```
</details>



### Schema
<details>
<summary>Data flow and database schema (PSQL)</summary>

![Schema](./docs/images/Schema.png)
</details>


### Technologies
This API was written entirely in Python using the following libraries:
- [Flask](http://flask.palletsprojects.com/en/1.1.x/)
- [SQLAlchemy](http://sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [Bcrypt](https://pypi.org/project/bcrypt/) (python)
- [Travis CI](https://travis-ci.com/)
- [Unsplash API](https://unsplash.com/documentation)
- [Heroku](https://www.heroku.com/) deployment and hosting


## Back End Collaborators
- [Nancy Lee](https://github.com/nancylee713)
- [Scott Schipke](https://github.com/sschipke)

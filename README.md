# quiz

## requirements

- python 3.9
- python-dotenv
- Flask
- Flask-Migrate
- flask-marshmallow
- marshmallow-sqlalchemy

## Database

### Tables

#### Accounts

##### User

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Primary Key |
| telegram_id | Integer | Telegram User ID |
| first_name | String | First Name |
| last_name | String | Last Name |
| username | String | Username |
| joined_at | DateTime | Joined At |
| last_seen | DateTime | Last Seen |
| is_admin | Boolean | Is Admin |
| is_banned | Boolean | Is Banned |
| is_active | Boolean | Is Active |

##### Account

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Primary Key |
| user_id | Integer | Foreign Key |
| balance | Float | Balance |
| created_at | DateTime | Created At |
| updated_at | DateTime | Updated At |

#### Quizzes

##### Technology

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Primary Key |
| name | String | Name |

##### Quiz

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Primary Key |
| technology_id | Integer | Foreign Key |
| title | String | Title |
| description | String | Description |

##### Question

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Primary Key |
| quiz_id | Integer | Foreign Key |
| question | String | Question |
| level | Integer | Level (1-5) |

##### Answer

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Primary Key |
| question_id | Integer | Foreign Key |
| answer | String | Answer |
| is_correct | Boolean | Is Correct |

##### UserQuiz

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Primary Key |
| user_id | Integer | Foreign Key |
| quiz_id | Integer | Foreign Key |
| correct_answers | Integer | Correct Answers |
| incorrect_answers | Integer | Incorrect Answers |
| missed_answers | Integer | Missed Answers |
| total_questions | Integer | Total Questions |
| score | Float | Score |
| time | Integer | Time in seconds |
| is_finished | Boolean | Is Finished |
| is_passed | Boolean | Is Passed |
| started_at | DateTime | Started At |
| finished_at | DateTime | Finished At |

### Relations

- User has one Account
- Account belongs to User
- Quiz has many Questions
- Question belongs to one Quiz
- Question has many Answers
- Answer belongs to one Question
- User has many UserQuizzes
- UserQuiz belongs to one User
- UserQuiz belongs to one Quiz

## API

### Endpoints

#### Accounts

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /accounts | Get all accounts |
| GET | /accounts/:id | Get account by id |
| POST | /accounts | Create account |
| PUT | /accounts/:id | Update account by id |
| DELETE | /accounts/:id | Delete account by id |

#### Quizzes

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /technologies | Get all technologies |
| GET | /technologies/:id/quizzes | Get quizzes by technology id |
| GET | /quizzes/:id/questions | Get questions by quiz id |
| GET | /questions/:id/answers | Get answers by question id |

#### UserQuizzes

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /user-quizzes | Get all user quizzes |
| GET | /user-quizzes/:id | Get user quiz by id |
| POST | /user-quizzes | Create user quiz |


Project Description
This project is a backend API built using FastAPI that performs User Management along with Text Analysis. The application stores all data in JSON files instead of using a database.

The system allows users to register by providing their name, email, and a text input. The text must contain between 1 and 200 words. Upon successful creation of a user, the system automatically generates a unique ID for that user.

After storing the user data, the application performs text analysis on the submitted text. The analysis includes:

Total word count

Number of uppercase characters

Number of special characters

Both the user data and analysis results are saved in separate JSON files to ensure data persistence.

The API provides the following functionalities:

Create User (POST /user)

Validates input data

Generates a unique ID

Performs text analysis

Stores user and analysis data

Returns structured JSON response

Get All Users (GET /users)

Returns a list of all registered users

Get Single User (GET /users/{user_id})

Returns a specific user by ID

Returns 404 if the user is not found

Get Analysis (GET /analysis/{analysis_id})

Returns text analysis data for a specific user

Delete User (DELETE /users/{user_id})

Deletes user data

Deletes corresponding analysis data

Updates JSON files

Returns confirmation message

The application properly handles validation errors and returns appropriate HTTP status codes such as 201 (Created), 400 (Bad Request), and 404 (Not Found).

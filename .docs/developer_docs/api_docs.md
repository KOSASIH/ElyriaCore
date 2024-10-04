# API Documentation

## Overview

Our API is a RESTful API that provides access to our platform's data and functionality. It is designed to be easy to use and understand, with clear and concise documentation.

## Endpoints

### GET /users

* Returns a list of all users in the system
* Parameters:
	+ `limit`: The maximum number of users to return (default: 100)
	+ `offset`: The offset from which to start returning users (default: 0)
* Response:
	+ `users`: A list of user objects
	+ `total`: The total number of users in the system

### POST /users

* Creates a new user in the system
* Parameters:
	+ `name`: The name of the user
	+ `email`: The email address of the user
	+ `password`: The password of the user
* Response:
	+ `user`: The newly created user object

### GET /users/{id}

* Returns a single user by ID
* Parameters:
	+ `id`: The ID of the user to retrieve
* Response:
	+ `user`: The user object

### PUT /users/{id}

* Updates a single user by ID
* Parameters:
	+ `id`: The ID of the user to update
	+ `name`: The new name of the user
	+ `email`: The new email address of the user
	+ `password`: The new password of the user
* Response:
	+ `user`: The updated user object

### DELETE /users/{id}

* Deletes a single user by ID
* Parameters:
	+ `id`: The ID of the user to delete
* Response:
	+ `success`: A boolean indicating whether the deletion was successful

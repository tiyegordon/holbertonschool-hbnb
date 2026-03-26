- namespace: 'user'
- model fields: first_name, last_name, email
- endpoints:
    GET /api/v1/user  #return all users
    POST /api/v1/user #create new user
    GET /api/v1/user/<id> #return one user
    PUT /api/v1/user/<id> #update one user

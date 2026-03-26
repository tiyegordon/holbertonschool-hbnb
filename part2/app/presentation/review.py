- namespace: 'review'
- model fields: text, rating, place+id, user_id
- endpoints:
    GET /api/v1/review/  #return all reviews
    POST /api/v1/review/ #create new review
    GET /api/v1/review/<id> #return one review
    PUT /api/v1/review/<id> #update one review
    DELETE /api/V1/review/<id> #delte review
    GET /api/v1/place/<id>/review #return all reviews for palce

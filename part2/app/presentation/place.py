- namespace: 'place'
- model fields: title, description, price, latitude, longitude, owner_id
- endpoints:
    GET /api/v1/place  #return all places
    POST /api/v1/place #create new place
    GET /api/v1/place/<id> #return one place (+owner name +amenities)
    PUT /api/v1/place/<id> #update one place

# 0x05. AirBnB clone - RESTful API

## The following concepts were demonstrated in this RESTful API Project

- What REST means
- What API means
- What CORS means
- What is an API
- What is a REST API
- What are other type of APIs
- Which is the HTTP method to retrieve resource(s)
- Which is the HTTP method to create a resource
- Which is the HTTP method to update resource
- Which is the HTTP method to delete resource
- How to request REST API

### Status of your APi
- The status of the API endpoints can be checked using the following command
`curl -X GET http://0.0.0.0:5000/api/v1/status` which will return a JSON body:
```
{
  "status": "OK"
}
```
- The returned content type for all API calls are is `application/json'
```
$ curl -X GET -s http://0.0.0.0:5000/api/v1/status -vvv 2>&1 | grep Content-Type
< Content-Type: application/json
```
- For this to work, we are using Blueprint class from Flask with `url_prefix='/api/v1'`
- The configuration of the API Host and Port can be controlled using the environment variables `HBNB_API_HOST` and  `HBNB_API_PORT` respectively. The default value for `host` is `0.0.0.0` and `port` is `5000`.

### Some Stats
- The total count of each object that hold information about a certain place such as `Amenity`, `Place`, '`City`', `State`, `Review`, and `User`.
- This is achieved using the `get` and `count` methods for each Object.
- Here is an example:
```
$ curl -X GET http://0.0.0.0:5000/api/v1/stats
{
  "amenities": 47, 
  "cities": 36, 
  "places": 154, 
  "reviews": 718, 
  "states": 27, 
  "users": 31
}
```
 
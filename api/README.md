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
### Not found
- Whenever an unknown url is used to query for the API, an error message is show as the following:
```
$ curl -X GET http://0.0.0.0:5000/api/v1/nop
{
  "error": "Not found"
}
```
- A handler is present in `api/v1/app.py` for `404` errors that returns a `JSON-formatted 404 status code` response.
```
$ curl -X GET http://0.0.0.0:5000/api/v1/nop -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/nop HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.51.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 404 NOT FOUND
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Fri, 14 Apr 2017 23:43:24 GMT
< 
{
  "error": "Not found"
}
```
### State
- View states can perform the following:
    - Retrieves the list of all State objects: `GET /api/v1/states`
    ```
    $ curl -X GET http://0.0.0.0:5000/api/v1/states/
    [
    {
        "__class__": "State", 
        "created_at": "2017-04-14T00:00:02", 
        "id": "8f165686-c98d-46d9-87d9-d6059ade2d99", 
        "name": "Louisiana", 
        "updated_at": "2017-04-14T00:00:02"
    }, 
    {
        "__class__": "State", 
        "created_at": "2017-04-14T16:21:42", 
        "id": "1a9c29c7-e39c-4840-b5f9-74310b34f269", 
        "name": "Arizona", 
        "updated_at": "2017-04-14T16:21:42"
    }, 
    ...
    ```
    - Retrieves a State object: `GET /api/v1/states/<state_id>`
    ```
    $ curl -X GET http://0.0.0.0:5000/api/v1/states/8f165686-c98d-46d9-87d9-d6059ade2d99
    {
    "__class__": "State", 
    "created_at": "2017-04-14T00:00:02", 
    "id": "8f165686-c98d-46d9-87d9-d6059ade2d99", 
    "name": "Louisiana", 
    "updated_at": "2017-04-14T00:00:02"
    }
    ```
    - Deletes a State object: `DELETE /api/v1/states/<state_id>`
    ```
    $ curl -X DELETE http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6
    {}
    ```
    - Creates a State: `POST /api/v1/states`
    ```
    $ curl -X POST http://0.0.0.0:5000/api/v1/states/ -H "Content-Type: application/json" -d '{"name": "California"}' -vvv
    *   Trying 0.0.0.0...
    * TCP_NODELAY set
    * Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
    > POST /api/v1/states/ HTTP/1.1
    > Host: 0.0.0.0:5000
    > User-Agent: curl/7.51.0
    > Accept: */*
    > Content-Type: application/json
    > Content-Length: 22
    > 
    * upload completely sent off: 22 out of 22 bytes
    * HTTP 1.0, assume close after body
    < HTTP/1.0 201 CREATED
    < Content-Type: application/json
    < Content-Length: 195
    < Server: Werkzeug/0.12.1 Python/3.4.3
    < Date: Sat, 15 Apr 2017 01:30:27 GMT
    < 
    {
    "__class__": "State", 
    "created_at": "2017-04-15T01:30:27.557877", 
    "id": "feadaa73-9e4b-4514-905b-8253f36b46f6", 
    "name": "California", 
    "updated_at": "2017-04-15T01:30:27.558081"
    }
    * Curl_http_done: called premature == 0
    * Closing connection 0
    ```
    - Updates a State object: `PUT /api/v1/states/<state_id>`
    ```
    $ curl -X GET http://0.0.0.0:5000/api/v1/states/8f165686-c98d-46d9-87d9-d6059ade2d99
    {
    "__class__": "State", 
    "created_at": "2017-04-14T00:00:02", 
    "id": "8f165686-c98d-46d9-87d9-d6059ade2d99", 
    "name": "Louisiana", 
    "updated_at": "2017-04-14T00:00:02"
    }
    $ curl -X PUT http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6 -H "Content-Type: application/json" -d '{"name": "California is so cool"}'
    {
    "__class__": "State", 
    "created_at": "2017-04-15T01:30:28", 
    "id": "feadaa73-9e4b-4514-905b-8253f36b46f6", 
    "name": "California is so cool", 
    "updated_at": "2017-04-15T01:51:08.044996"
    }
    $ curl -X GET http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6
    {
    "__class__": "State", 
    "created_at": "2017-04-15T01:30:28", 
    "id": "feadaa73-9e4b-4514-905b-8253f36b46f6", 
    "name": "California is so cool", 
    "updated_at": "2017-04-15T01:51:08"
    }

    ```
### City
- View cities creates a new view for City objects that handles all default RESTFul API actions:
    - Retrieves the list of all City objects of a State: `GET /api/v1/states/<state_id>/cities`
    ```
    $ curl -X GET http://0.0.0.0:5000/api/v1/states/not_an_id/cities/
    {
    "error": "Not found"
    }
    $ curl -X GET http://0.0.0.0:5000/api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities
    [
    {
        "__class__": "City", 
        "created_at": "2017-03-25T02:17:06", 
        "id": "1da255c0-f023-4779-8134-2b1b40f87683", 
        "name": "New Orleans", 
        "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
        "updated_at": "2017-03-25T02:17:06"
    }, 
    {
        "__class__": "City", 
        "created_at": "2017-03-25T02:17:06", 
        "id": "45903748-fa39-4cd0-8a0b-c62bfe471702", 
        "name": "Lafayette", 
        "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
        "updated_at": "2017-03-25T02:17:06"
    }, 
    {
        "__class__": "City", 
        "created_at": "2017-03-25T02:17:06", 
        "id": "e4e40a6e-59ff-4b4f-ab72-d6d100201588", 
        "name": "Baton rouge", 
        "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
        "updated_at": "2017-03-25T02:17:06"
    }
    ]
    ```
    - Retrieves a City object. : `GET /api/v1/cities/<city_id>`
    ```
    $ curl -X GET http://0.0.0.0:5000/api/v1/cities/1da255c0-f023-4779-8134-2b1b40f87683
    {
    "__class__": "City", 
    "created_at": "2017-03-25T02:17:06", 
    "id": "1da255c0-f023-4779-8134-2b1b40f87683", 
    "name": "New Orleans", 
    "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
    "updated_at": "2017-03-25T02:17:06"
    }
    ```
    - Creates a City: POST /api/v1/states/<state_id>/cities    
    ```
    $ curl -X POST http://0.0.0.0:5000/api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities -H "Content-Type: application/json" -d '{"name": "Alexandria"}' -vvv
    *   Trying 0.0.0.0...
    * TCP_NODELAY set
    * Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
    > POST /api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities/ HTTP/1.1
    > Host: 0.0.0.0:5000
    > User-Agent: curl/7.51.0
    > Accept: */*
    > Content-Type: application/json
    > Content-Length: 22
    > 
    * upload completely sent off: 22 out of 22 bytes
    * HTTP 1.0, assume close after body
    < HTTP/1.0 201 CREATED
    < Content-Type: application/json
    < Content-Length: 249
    < Server: Werkzeug/0.12.1 Python/3.4.3
    < Date: Sun, 16 Apr 2017 03:14:05 GMT
    < 
    {
    "__class__": "City", 
    "created_at": "2017-04-16T03:14:05.655490", 
    "id": "b75ae104-a8a3-475e-bf74-ab0a066ca2af", 
    "name": "Alexandria", 
    "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
    "updated_at": "2017-04-16T03:14:05.655748"
    }
    * Curl_http_done: called premature == 0
    * Closing connection 0
    ```
    - Updates a City object: PUT /api/v1/cities/<city_id>
    ```
    $ curl -X PUT http://0.0.0.0:5000/api/v1/cities/b75ae104-a8a3-475e-bf74-ab0a066ca2af -H "Content-Type: application/json" -d '{"name": "Bossier City"}'
    {
    "__class__": "City", 
    "created_at": "2017-04-16T03:14:06", 
    "id": "b75ae104-a8a3-475e-bf74-ab0a066ca2af", 
    "name": "Bossier City", 
    "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
    "updated_at": "2017-04-16T03:15:12.895894"
    }
    ```
    - Deletes a City object: DELETE /api/v1/cities/<city_id>
    ```
    $ curl -X GET http://0.0.0.0:5000/api/v1/cities/b75ae104-a8a3-475e-bf74-ab0a066ca2af
    {
    "__class__": "City", 
    "created_at": "2017-04-16T03:14:06", 
    "id": "b75ae104-a8a3-475e-bf74-ab0a066ca2af", 
    "name": "Bossier City", 
    "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
    "updated_at": "2017-04-16T03:15:13"
    }
    ```
### Amenity
- Creates a new view for Amenity objects that handles all default RESTFul API actions:
    - Retrieves a Amenity object: `GET /api/v1/amenities/<amenity_id>`
     
    - Deletes a Amenity object:: `DELETE /api/v1/amenities/<amenity_id>`
        
    - Creates a Amenity: `POST /api/v1/amenities`
        
    - Updates a Amenity object: `PUT /api/v1/amenities/<amenity_id>`

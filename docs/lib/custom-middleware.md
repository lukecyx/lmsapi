# Middleware

## Content-TypeMiddleware

Path: `/lib/middleware/content_type.py`

For all post requests:

Checks the `Content-Type` header for each request, if it is not `application/json` a 415 HTTP error is returned. (HTTP 415 == Unsupported Media Type).

*Note: Not sure if this is the correct HTTP status code to use but it conveys the message still.*

## JsonDataLoaderMiddleware

Path: `lib/middleware/json_data_loader.py`

Loads the body of a post request into Json, if all of the following conditions are not met, then it adds the request body as json into the view kwargs ready to be worked with.

`view_kwargs["data"] = json.loads(request.body)`

4 conditions that must be False for the request body to be sent as a kwarg:

- The request is not a POST request.
- The request can't be loaded into Json.
- That after loading the Json that it is not a falsey value.
- That the loaded request body is an instance of dict.

Access the loaded in any POST method by adding the data param.
For example:

```
def post(
    self, request: HttpRequest, data: Dict = None
) -> JsonResponse:
    """POST request with dummy response."""
                                                                                     
    return JsonResponse(status=200, data={"dummy": data})
```

## APIErrorMiddleware

Path: `lib/middleware/api_error.py`

In environemnts other than local and debug.

If an error occurs within a few, or code called from a view.
The response returned will be in the structure of:

```
{"error": "something bad happened"}
```
Rather than the full stack trace.
This is to avoid leaking the stack being used to power the API.

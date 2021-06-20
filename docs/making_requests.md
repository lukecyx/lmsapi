# Making Requests

## GET Requests

No deviance to how you would expect a GET request to behave.

## POST Requests

Even though it is acceptable for POST requests to allow an empty body, this is not the case for this API.

Any POST request that does not have a request body is rejected, we only want to be doing with POST requests when the requestor is sending data for us to work with.

Each POST request body is loaded into Json and used as a parameter (data) in a Views func/method.

For more details on how this is done see the docs:

[Middleware docs](lib/custom-middleware.md)

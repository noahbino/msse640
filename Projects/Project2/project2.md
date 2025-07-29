# Project 2: Integration Testing With Postman
## MSSE640 - Software Security Engineering

## Table of Contents
- [Part 1: Research on APIs](#part-1-research-on-apis)


### Part 1: Research on APIs

#### Common Terms
Client: Browser or App that sends HTTP requests (consumer)
Sever: Backend service that receives requests and sends responses 

Request: Sent by client with URL, headers (optional), body input (optional)
Response: Returned by server with status code body output

Headers: Meta data, can include content type, auth tokens, app info, etc
Body: Actual data, usually in JSON or XML format

GET: retrieve data 
POST: submit data
PUT: replace data
DELETE: remove data

200: ok
201: created
400: bad request
401: unauthorized
404: not found 
500: server error

HTTP is stateless becuase each request is independent, it doesn't need to remember previous requests in order to do its job. Sessions can be tracked with tokens or cookies if continuity is needed.

#### APIs
APIs allow different software systems to communicate, they enable moibile apps to talk to servers, services to interact, and frontends to fetch and post data.

#### Open APIs
Public APIs are accessible by independent developers without restrictions, they promote innovation, integrations, third party applications, and education.

Spotify has an open API where developers can access music metadata, control playback, fetch playlists, and much more. Apple has (somewhat) public APIs (if you're developing an iOS app) that give access to device functions like vibration, bluetooth/wifi networking, and much more.

	1.	OpenWeatherMap – Weather data by city or geolocation
		https://openweathermap.org/api
	2.	REST Countries – Info about countries and regions
		https://restcountries.com/
	3.	NASA API – Space images, Mars rover data, and more
		https://api.nasa.gov/
	4.	CoinGecko – Cryptocurrency prices and stats
		https://www.coingecko.com/en/api
	5.	The Dog API – Dog images by breed, size, and more
		https://thedogapi.com/


### Part 2: API Demo with Postman

For this portion of the project, I decided to use a public stock tracking API called [Marketstack](https://marketstack.com). 

1. Collection 
![Postman Collection](/Assets/postman-collection.png)

2. GET Request to fetch stock tickers
![GET Request](/Assets/Screenshot%202025-07-28%20at%207.01.19 PM.png)

3. Environment 
![Postman Environment](/Assets/postman-environment.png)

4. Refactor
![Environment Refactor](/Assets/refactored-get.png)

5. More Requests

Simple GET request to fetch end of day information for SoFi Technologies:
![GET Request](/Assets/Screenshot%202025-07-28%20at%206.51.22 PM.png)

This API does not contain any POST requests, but I created a mock POST Request to create a new Ticker
![Mock POST Request](/Assets/post-request.png)

![GET Request To Fetch Dividend Data](/Assets/Screenshot%202025-07-29%20at%205.37.04 PM.png)

![Exchanges Request](/Assets/Screenshot%202025-07-29%20at%205.38.13 PM.png)

![Currencies Request](/Assets/Screenshot%202025-07-29%20at%205.38.45 PM.png)

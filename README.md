## Uptime checker
Simple app that checks endpoints and records response time 

### components
  #### server
    - add a url to start checking
    - get all the urls that the cron is checking
    - get all of the results for a url

  #### checker cron
    - gets the list of endpoints
    - iterates list and async calls endpoints
    - records results to local sqllite db
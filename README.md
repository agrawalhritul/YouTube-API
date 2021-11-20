This API fetches the details of the vidoes from YouTube of a particular query (in this caes, football) and stores the detials such as:
1. Video Title
2. Video Description
3. Video Url
4. Date when it was published
5. Thumbnail URL

The details of videos of Football can be queried using the description and title

For this API, Flask is used and MySql is used as the database:
The libraries and frameworks that need to be installed are:
1. flask   
2. mysql.connector
3. google api python client     pip install --upgrade google-api-python-client


The project needs to be registered on google api console and youtube api credentials needs to be issued
The Youtube API credentials need to be saved in the file credentials.py
Also, the database and a table has to be made and the details have to be saved:
1. Host
2. Username
3. Password
4. Database Name

To run the server, run the app.py file and the API will start working

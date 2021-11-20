from googleapiclient.discovery import build
import credentials, mysql.connector, time, datetime

connection = mysql.connector.connect(user="root",
                                     host="localhost",
                                     password=credentials.dbPassword,
                                     database="josh"
                                     )
cur= connection.cursor()
link= "https://www.youtube.com/watch?v="

# Arguments that need to passed to the build function

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating Youtube Resource Object
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                       developerKey=credentials.DEVELOPER_KEY)


def youtube_search_keyword(query):
    # calling the search.list method to
    # retrieve youtube search results
    while (False):
        date= datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-4] + "Z"
        search_keyword = youtube_object.search().list(q=query,
                                                      part="id, snippet",
                                                      maxResults= 10,
                                                      order="date",
                                                      type= "video",
                                                      publishedBefore= "date"
                                                      ).execute()

        # extracting the results from search response


        results = search_keyword.get("items", [])
        for result in results:
            if (result["kind"]== "youtube#searchResult"):
                video_url= result["id"]["videoId"]
                video_title= result["snippet"]["title"]
                description= result["snippet"]["description"]
                publishedat= result["snippet"]["publishedAt"]
                thumbnail_url= result["snippet"]["thumbnails"]["default"]["url"]
                cur.execute("SELECT video_url FROM YOUTUBE WHERE video_url = %s", video_url)
                rec= cur.fetchall()
                if (rec.size()== 0):
                    sql= "INSERT INTO YOUTUBE (video_title, video_url, description, publishedat, thumbnail_url) VALUES (%s, %s, %s, %s, %s)"
                    values = (video_title, video_url, description, publishedat, thumbnail_url)
                    cur.execute(sql, values)
                    connection.commit()

        time.sleep(10)


def searchByTitle(query):
    try:
        cur.execute("SELECT * FROM YOUTUBE WHERE video_title LIKE %s", "%"+query)
        data= cur.fetchall()
        result= [{
            "Video_url": link + data[0],
            "Video_title": data[1],
            "Description": data[2],
            "PublishedAt": data[3],
            "ThumbnailURL": data[4]
        }]
    except:
        result= {"Error":"No data found"}
    return result


def searchByDescription(query):
    try:
        cur.execute("SELECT * FROM YOUTUBE WHERE description LIKE %s", "%"+query)
        data= cur.fetchall()
        result = [{
            "Video_url": link + data[0],
            "Video_title": data[1],
            "Description": data[2],
            "PublishedAt": data[3],
            "ThumbnailURL": data[4]
        }]
    except:
        result= {"Error":"No data found"}
    return result

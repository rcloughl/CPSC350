from flask import render_template, request, redirect, url_for
from cpsc350 import dbtour
from pymongo import MongoClient, ASCENDING, DESCENDING
import mariadb
import redis

@dbtour.route("/", methods=["GET","POST"])
def functionname():
    r = redis.Redis(password="rjcrjc", charset="utf-8",
    decode_responses=True)
    conn = mariadb.connect(user="joe", password="rjcrjc",
    host="localhost", port=5051, database="dbTour")
    cur = conn.cursor()
    if 'genre' in request.args:
        cur.execute("select name,genre,grammys,monthylisteners,topSong,album from artists left join albums on name=artist where genre=? order by RAND() limit 10", (request.args['genre'],)) 
    else:
        cur.execute("select name,genre,grammys,monthylisteners,topSong,album from artists left join albums on name=artist order by RAND() limit 10")
    artists=cur.fetchall() 
    if 'album' in request.args:
        r.rpush("queue",request.args['album'])
    queuelen=r.llen("queue")
    if (queuelen>0):
        tempq=[]
        num=1
        queuenames=r.lrange("queue","0",queuelen)
        for name in queuenames:
            cur.execute("select album, tracks from albums where album=?",(name,))
            temp=cur.fetchall()
            holder=(temp[0][0],temp[0][1],num)
            tempq.append(holder)
            num=num+1
        queue=tuple(tempq)
    else:
        queue=(('Album','Below','Choose'),)
    if 'rem' in request.args:
        r.lpop('queue')
    if 'rat' in request.args:
        r.zincrby('likes',1,request.args['rat'])
    scores=r.zrange('likes',0,10000, 'WITHSCORES')
    likes=[]
    for name in scores:
        score=r.zscore('likes',name)
        likes.append((name,score))
    likes=tuple(likes)
    cur.execute("select distinct genre from artists")
    genres=cur.fetchall()
    cur.execute("select album, tracks from albums")
    albums=cur.fetchall()
    conn.close()
    r.close()
    mongo_client = MongoClient("mongodb://localhost:27017")
    db = mongo_client.albums
    reviews=list(db.albums.find())
    print(reviews)
    if request.method== "POST":
        if 'key' in request.form:
            print('in')
            if request.form['value']=='':
                reviews=list(db.albums.find({ '$or':[ {request.form['key']:{'$exists':'true'}}, {request.form['value']:{'$exists':'true'}}]}))
            else:
                reviews=list(db.albums.find({request.form['key']:request.form['value']}))
    else:
        reviews=list(db.albums.find())
    return render_template("artists.html", artists=artists, genres=genres, albums=albums, queue=queue,likes=likes, reviews=reviews)


@dbtour.route("/addartists", methods=['GET','POST'])
def addartists():
    if request.method == "POST":
        conn = mariadb.connect(user="joe", password="rjcrjc", host="localhost", port=5051, database="dbTour")
        cur = conn.cursor() 
        cur.execute("insert into artists values (?,?,?,?,?)",(request.form['artist'],request.form['genre'],int(request.form['grammy']),int(request.form['monthly']),request.form['topsong']))        
        conn.commit()
        return redirect(url_for('functionname'))
    else:
        return render_template("addartists.html")

@dbtour.route("/editreviews/<sname>", methods=['GET','POST'])
def editreviews(sname):
    if request.method=="POST":
         mongo_client = MongoClient("mongodb://localhost:27017")
         db = mongo_client.albums
         if 'key' and 'value'  in request.form:
             db.albums.update_one({'name':sname},{'$set':{request.form['key']:request.form['value']}})
         if 'artist' in request.form:
             db.albums.update_many({"name":sname}, {'$set': {"artist":request.form['artist'],"orating":request.form['orating'],"sold":request.form['sold'],"features":request.form['features'],"rrating":request.form['rrating'],"erating":request.form['erating'],"underrated":request.form['underrated'],"overrated":request.form['overrated']}})
         return redirect(url_for('functionname'))
    else:
         mongo_client = MongoClient("mongodb://localhost:27017")
         db = mongo_client.albums
         review=db.albums.find({"name":sname}).next()
         print(review)
         return render_template("editreviews.html", review=review)


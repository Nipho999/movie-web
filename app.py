from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

def custom_enumerate(iterable, start=0):
    return enumerate(iterable, start=start)

app.jinja_env.filters['enumerate'] = custom_enumerate

# File to store all comments
COMMENTS_FILE = "comments.txt"

@app.route("/")
def home():
    # page 1
    movies = [
        {"id": 1, "title": " The&nbspWomen King ", "image_url":  "https://i.ibb.co/s36tGWT/oie-PPM8-J508-NNp-H.png"},
        {"id": 2, "title": "Project <br>Gemini", "image_url": "https://cdn.jwplayer.com/thumbs/RP1snTez-1280.jpg"},
        {"id": 3, "title": "Paradise <br> City", "image_url": "https://cdn.jwplayer.com/thumbs/KdJYs9Bw-1280.jpg"},
        {"id": 4, "title": "John wick Chapter 2", "image_url": "https://cdn.jwplayer.com/thumbs/euUesG53-640.jpg"},
        {"id": 5, "title": "Emancipation<br> &nbsp", "image_url": "https://cdn.jwplayer.com/thumbs/GTBpPBO0-1280.jpg"},
        {"id": 6, "title": "Black Adam <br> &nbsp", "image_url": "https://cdn.jwplayer.com/thumbs/NLkGeirN-1280.jpg" },
        {"id": 7, "title": "Doctor&nbspStrange<br> &nbsp", "image_url": "https://cdn.jwplayer.com/thumbs/wNxHPZWT-1280.jpg"},
        {"id": 8, "title": "The Ledge<br> &nbsp", "image_url": "https://cdn.jwplayer.com/thumbs/Xgwh6pNm-1280.jpg"},
        {"id": 9, "title": "Legend of The Ten Rings", "image_url": "https://cdn.jwplayer.com/thumbs/0B6F0HV0-1280.jpg"},
        {"id": 10, "title": "Top Gun Maverick", "image_url": "https://cdn.jwplayer.com/thumbs/Ik06LriI-1280.jpg"},
        {"id": 11, "title": "The North<br> Man", "image_url": "https://cdn.jwplayer.com/thumbs/oY89Ml5i-1280.jpg"},
        {"id": 12, "title": "John Wick chapter 1", "image_url": "https://cdn.jwplayer.com/thumbs/7Zhz6qQK-640.jpg"},
        {"id": 13, "title": "Movie 13", "image_url": ""},
        {"id": 14, "title": "Movie 14", "image_url": ""},
        {"id": 15, "title": "Movie 15", "image_url": ""},
        {"id": 16, "title": "Movie 16", "image_url": ""}
    ]
    return render_template("movies.html", movies=movies)

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    # page 2
    movie_details = {
        1: {"title": "The Women King ", "description": "After provoking the empire of Oyo by liberating enslaved women, General Nanisca prepares to face the wrath along with an all-women army of her own.",
            "rating": 8.5, "reviews": [], "poster_url": "https://i.ibb.co/s36tGWT/oie-PPM8-J508-NNp-H.png", "video_url": "https://cdn.jwplayer.com/manifests/m989R7Gr.m3u8"},
        2: {"title": "&nbsp &nbsp &nbsp PROJECT GEMINI", "description": "During a space mission sent to terraform a distant planet, the mission encounters something unknown that has its own plan for the planet.", "rating": 6.4, "reviews": [], "poster_url": "https://cdn.jwplayer.com/thumbs/RP1snTez-1280.jpg", "video_url": "https://cdn.jwplayer.com/manifests/RP1snTez.m3u8"},
        3: {"title": "&nbsp &nbsp &nbsp &nbspPARADISE CITY", "description": "Ryan Swan, along with his partners, embarks on a relentless quest for retribution against a criminal mastermind following the brutal assassination of his father.", "rating": 6.8, "reviews": [], "poster_url": "https://cdn.jwplayer.com/thumbs/KdJYs9Bw-1280.jpg", "video_url": "https://cdn.jwplayer.com/manifests/KdJYs9Bw.m3u8"},
        4: {"title": "JOHN WICK CHAPTER 2", "description": "John Wick, a retired hitman, visits Italy to pay off an inescapable blood debt. However, he soon finds himself cornered by every killer in the business due to an enormous bounty on his head.", "rating": 9.0, "reviews": [], "poster_url": "https://cdn.jwplayer.com/thumbs/euUesG53-640.jpg", "video_url": "https://cdn.jwplayer.com/manifests/euUesG53.m3u8"},
        5: {"title": "EMANCIPATION", "description": "Peter, a slave, flees a plantation in Louisiana after he was whipped within an inch of his life. He has to outwit cold-blooded hunters and the unforgiving swamps of Louisiana on a torturous journey north.", "rating": 8.7, "reviews": [], "poster_url": "https://cdn.jwplayer.com/thumbs/GTBpPBO0-1280.jpg", "video_url": "https://cdn.jwplayer.com/manifests/GTBpPBO0.m3u8"},
        6: {"title": "&nbsp &nbsp &nbsp &nbsp &nbsp &nbspBLACK ADAM&nbsp &nbsp ", "description": "After being granted with the divine power of the Egyptian Gods and spending almost 5000 years in a guardhouse, Black Adam is freed and he decides to unloose his own style of justice to the world.", "rating": 6.4, "reviews": [], "poster_url": "https://cdn.jwplayer.com/thumbs/NLkGeirN-1280.jpg", "video_url": "https://cdn.jwplayer.com/manifests/NLkGeirN.m3u8"},
        7: {"title": "&nbsp &nbsp &nbsp &nbspDr Strange&nbsp", "description": "In an accident, Stephen Strange, a famous neurosurgeon, loses the ability to use his hands. He goes to visit the mysterious Ancient One to heal himself and becomes a great sorcerer under her tutelage.", "rating": 8.7, "reviews": [], "poster_url": "https://cdn.jwplayer.com/thumbs/wNxHPZWT-1280.jpg", "video_url": "https://cdn.jwplayer.com/manifests/wNxHPZWT.m3u8"},
        8: {"title": "&nbsp The Ledge", "description": "A rock-climbing adventure turns into a living nightmare when a woman captures the murder of her best friend on camera. With nowhere to go, she begins a treacherous ascent up a mountain cliff as the killer and his friends follow close behind.", "rating": 9.1, "reviews": [], "poster_url": "https://cdn.jwplayer.com/thumbs/Xgwh6pNm-1280.jpg", "video_url": "https://cdn.jwplayer.com/manifests/Xgwh6pNm.m3u8"},
        9: {"title": " The Legend of The ten Rings", "description": "Shang-Chi, a martial artist, lives a quiet life after he leaves his father and the shadowy Ten Rings organisation behind. Years later, he is forced to confront his past when the Ten Rings attack him.", "rating": 8.7, "reviews": [], "poster_url": "https://cdn.jwplayer.com/thumbs/0B6F0HV0-1280.jpg", "video_url": "https://cdn.jwplayer.com/manifests/0B6F0HV0.m3u8"},
        10: {"title": " Top Gun Maverick", "description": "Thirty years of service leads Maverick to train a group of elite TOPGUN graduates to prepare for a high-profile mission while Maverick battles his past demons.", "rating": 8.7, "reviews": [], "poster_url": "https://cdn.jwplayer.com/thumbs/Ik06LriI-1280.jpg", "video_url": "https://cdn.jwplayer.com/manifests/Ik06LriI.m3u8"},
        11: {"title": "The North Man", "description": "Adventure awaits Prince Amleth, whose father was killed and mother was abducted by his ruthless uncle. However, the journey takes him through twists which unravel a dark truth about his family.", "rating": 8.7, "reviews": [], "poster_url": "https://cdn.jwplayer.com/thumbs/oY89Ml5i-1280.jpg", "video_url": "https://cdn.jwplayer.com/manifests/oY89Ml5i.m3u8"},
        12: {"title": "Jonh wick Chapter 1", "description": "John Wick, a retired hitman, is forced to return to his old ways after a group of Russian gangsters steal his car and kill a puppy gifted to him by his late wife.", "rating": 8.7, "reviews": [], "poster_url": "https://cdn.jwplayer.com/thumbs/7Zhz6qQK-640.jpg", "video_url": "https://cdn.jwplayer.com/manifests/7Zhz6qQK.m3u8"},
        13: {"title": "", "description": "", "rating": 8.7, "reviews": [], "poster_url": "", "video_url": ""},
        14: {"title": "", "description": "", "rating": 8.7, "reviews": [], "poster_url": "", "video_url": ""},
        15: {"title": "", "description": "", "rating": 8.7, "reviews": [], "poster_url": "", "video_url": ""},
        16: {"title": "", "description": "", "rating": 8.7, "reviews": [], "poster_url": "", "video_url": ""}
    }

    movie = movie_details.get(movie_id)
    if movie:
        movie["id"] = movie_id
        comments = []
        if os.path.exists(COMMENTS_FILE):
            with open(COMMENTS_FILE, "r") as f:
                for line in f:
                    parts = line.strip().split(":")
                    if len(parts) == 3 and int(parts[0]) == movie_id:
                        comments.append({"username": parts[1], "comment": parts[2]})
        return render_template("movie_details.html", movie=movie, comments=comments)
    else:
        return "Movie not found", 404



@app.route("/movie/<int:movie_id>/comment", methods=["POST"])
def add_comment(movie_id):
    username = request.form.get("username")
    comment = request.form.get("comment")
    if username and comment:
        with open(COMMENTS_FILE, "a") as f:
            f.write(f"{movie_id}:{username}:{comment}\n")
    return redirect(url_for("movie_details", movie_id=movie_id))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000')
    #app.run(host='0.0.0.0', ssl_context=('cert.pem', 'key.pem'))


from flask import *
import pymysql
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
app.permanent_session_lifetime=timedelta(minutes=10)
app = Flask(__name__,template_folder="templates",static_folder="static")
app.secret_key="manbigdat"
# Connect to PHPMyAdmin cloud database
db = pymysql.connect(
    host='sql9.freesqldatabase.com',
    user='sql9601859',
    password='4EmEWs8HSl',
    db='sql9601859'

)
@app.route("/first", methods=["GET", "POST"])
def first():
    if request.method == "POST":
        # Retrieve form data
        min_lat = request.form["min_lat"]
        max_lat = request.form["max_lat"]
        min_population = request.form["min_population"]
        max_population = request.form["max_population"]

        # Construct SQL query
        query = "SELECT city, State, Population, lat, lon FROM city WHERE lat BETWEEN %s AND %s AND Population BETWEEN %s AND %s"
        params = (min_lat, max_lat, min_population, max_population)

        # Execute SQL query
        cursor = db.cursor()
        cursor.execute(query, params)

        # Fetch results
        results = cursor.fetchall()
        print(results)

        # Render template with results
        return render_template("first.html", results=results)

    # Render the search form
    return render_template("allquestions.html")


@app.route("/bonus", methods=["GET", "POST"])
def bonus():
    if request.method == "POST":
        # Retrieve form data
        state_name = request.form.get("state_name")
        min_population = request.form["min_population2"]
        max_population = request.form["max_population2"]

        # Construct SQL query
        query = "SELECT city, state, population, lat, lon FROM city WHERE state = %s AND population BETWEEN %s AND %s"
        params = (state_name, min_population, max_population)

        # Execute SQL query
        cursor = db.cursor()
        cursor.execute(query, params)

        # Fetch results
        results = cursor.fetchall()

        # Render template with results
        return render_template("first.html", results=results)

    # Render the search form
    return render_template("allquestions.html")


@app.route("/third", methods=["GET", "POST"])
def third():
    if request.method == "POST":
        sentences = request.form.get("sentences")
        words = request.form.get("words")

        # Split sentences and words
        sentences_list = [s.strip() for s in sentences.split('.') if s.strip()]
        words_list = [w.strip() for w in words.split(',') if w.strip()]

        # Initialize word counts
        word_counts = {word: 0 for word in words_list}

        # Find word occurrences in sentences
        word_occurrences = {word: [] for word in words_list}
        for i, sentence in enumerate(sentences_list):
            for word in words_list:
                if word.lower() in sentence.lower():
                    word_occurrences[word].append((i + 1, sentence))
                    word_counts[word] += 1

        # Render template with results
        return render_template("third.html", word_occurrences=word_occurrences, word_counts=word_counts)

    # Render the search form
    return render_template("allquestions.html")


@app.route("/pie", methods=["GET", "POST"])
def pie():
    if request.method == "POST":
        sentences = request.form.get("sentences2")
        words = request.form.get("words2")

        # Split sentences and words
        sentences_list = [s.strip() for s in sentences.split('.') if s.strip()]
        words_list = [w.strip() for w in words.split(',') if w.strip()]

        # Initialize word counts
        word_counts = {word: 0 for word in words_list}

        # Find word occurrences in sentences
        word_occurrences = {word: [] for word in words_list}
        for i, sentence in enumerate(sentences_list):
            for word in words_list:
                if word.lower() in sentence.lower():
                    word_occurrences[word].append((i + 1, sentence))
                    word_counts[word] += 1

        # Generate pie chart
        labels = list(word_counts.keys())
        counts = list(word_counts.values())


        # Render template with results and chart
        return render_template("pie.html", labels=labels, counts=counts)

    # Render the search form
    return render_template("allquestions.html")





@app.route("/basic")
def index():
    return "<h1>Hello Azure!</h1>"

@app.route('/')
def home():
    return render_template("home.html")









if __name__ == "__main__":
    app.run(debug=True)
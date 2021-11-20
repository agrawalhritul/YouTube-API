from flask import Flask, jsonify
import database, multiprocessing

app = Flask(__name__)

#Search by Title
@app.route('/title/<query>')
def Title(query):
    result= database.searchByTitle(query)
    return jsonify(result)

#Search by Description
@app.route('/description/<query>')
def Description(query):
    result= database.searchByDescription(query)
    return jsonify(result)

def main():
    app.run(debug= True)

if __name__ == "__main__":
    p1= multiprocessing.Process(target= database.youtube_search_keyword("football")).start()
    p2= multiprocessing.Process(target= main()).start()
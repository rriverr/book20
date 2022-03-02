



from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:yunayuna@cluster0.5i0os.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta



@app.route('/')
def home():
    return render_template('index.html')

@app.route("/book", methods=["GET"])
def book_get():
    book_list = list(db.books.find({}, {'_id': False}))
    return jsonify({'books':book_list})

@app.route('/review', methods=['GET'])
def review():
    isbn = request.args.get('isbn')
    return render_template('review.html', isbn=isbn)

@app.route("/reviews", methods=["POST"])
def review_post():
    nickname_receive = request.form['nickname_give']
    content_receive = request.form['content_give']
    isbn_receive = request.form['isbn_give']
    isbn_int = int(isbn_receive)
    
    isbn = db.books.find_one({'isbn'['value']: isbn_int})
    print(isbn)
    # doc = {
    #     'nickname':nickname_receive,
    #     'content':content_receive,
    # }
    # db.books.find()

    return jsonify({'msg': '등록되었습니다.'})

@app.route("/reviews", methods=["GET"])
def review_get():
    book_list = list(db.books.find({}, {'_id': False}))
    return jsonify({'books':book_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
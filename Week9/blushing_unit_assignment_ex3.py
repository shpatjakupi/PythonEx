from flask import Flask, jsonify
import pymysql 

app = Flask(__name__)
cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='read9') 

@app.route('/api/worldpop/all')
def get_all():
    query = 'SELECT * FROM worldpop'
    with cnx.cursor() as cursor:
        cursor.execute(query)
        return jsonify(cursor.fetchall())

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
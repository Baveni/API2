from flask import Flask, jsonify
from connection import Conn

app = Flask(__name__)


@app.route("/something/", methods=["GET"])
def get_establishment():
    db = Conn()
    db.connect()

    data = db.session.execute("""SELECT array_to_json(array_agg(t)) AS data
    FROM
      (
    SELECT * FROM "somewhere" LIMIT 10
      ) t;""")
    data = data.fetchall()[0][0]
    print data
    db.close()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)

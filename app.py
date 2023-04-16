import pymysql
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/add/user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template("add_user.html")

    username = request.form.get("user")
    password = request.form.get("pwd")
    mobile = request.form.get("mobile")

    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password="123456",
        charset='utf8',
        db="unicom"
    )

    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "insert into admin(username,password,mobile) values(%s,%s,%s)"
    cursor.execute(sql, [username, password, mobile])
    conn.commit()

    cursor.close()
    conn.close()


@app.route("/show/user")
def show_user():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password="123456",
        charset='utf8',
        db="unicom"
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from admin"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    cursor.close()
    conn.close()

    print(data_list)

    return render_template('show_user.html', data_list=data_list)


if __name__ == '__main__':
    app.run()

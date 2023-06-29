from flask import Flask
from flask import render_template
import utils
from flask import jsonify
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/test1')
def test1():
    return render_template("test1.html")

@app.route('/get_left1',methods=['get','post'])
def get_left1():
    res = utils.get_left1()
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    for tup in res:
        day.append(tup[0].strftime("%m-%d"))
        confirm.append(tup[1])
        suspect.append(tup[2])
        heal.append(tup[3])
        dead.append(tup[4])
    return jsonify({"day":day,"confirm":confirm,"suspect":suspect,"heal":heal,"dead":dead})

# @app.route('/get_left2',methods=['get','post'])
# def get_left2():
#     res = utils.get_left2()
#     day,confirm,suspect = [],[],[]
#     for item in res:
#         day.append(item[0].strftime("%m-%d"))
#         confirm.append(item[1])
#         suspect.append(item[2])
#     return jsonify({"day":day,"confirm":confirm,"suspect":suspect})

@app.route('/get_left3',methods=['get','post'])
def get_left3():
    res = utils.get_left3()
    day,dead = [],[]
    for item in res:
        day.append(item[0].strftime("%m-%d"))
        dead.append(item[1])
        # heal.append(item[2])
    return jsonify({"day":day,"dead":dead})

@app.route('/get_right1',methods=['get','post'])
def get_right1():
    res = utils.get_right1()
    day,confirm,suspect,heal,dead,heal_add = [],[],[],[],[],[]
    for tup in res:
        day.append(tup[0].strftime("%m-%d"))
        confirm.append(tup[1])
        suspect.append(tup[2])
        heal.append(tup[3])
        dead.append(tup[4])
        dead.append(tup[5])
    return jsonify({"day":day,"confirm":confirm,"suspect":suspect,"heal":heal,"dead":dead,"heal_add":heal_add})

@app.route('/get_right2',methods=['get','post'])
def get_right2():
    res = utils.get_right2()
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    for tup in res:
        day.append(tup[0].strftime("%m-%d"))
        confirm.append(tup[1])
        suspect.append(tup[2])
        heal.append(tup[3])
        dead.append(tup[4])
    return jsonify({"day":day,"confirm":confirm,"suspect":suspect,"heal":heal,"dead":dead})

@app.route('/get_right3',methods=['get','post'])
def get_right3():
    res = utils.get_right3()
    #day,confirm = [],[]
    confirm=[]
    for tup in res:
        #day.append(tup[0].strftime("%m-%d"))
        confirm.append(tup[0])
    #return jsonify({"day":day,"confirm":confirm})
    return jsonify({"confirm":confirm})

# @app.route('/get_center',methods=['get','post'])
# def get_right3():
#     res = utils.get_center()
#     confirm=[]
#     for tup in res:
#         confirm.append(tup[0])
#     return jsonify({"confirm":confirm})


if __name__ == '__main__':
    app.run()

# importing Flask and other modules
from flask import Flask, request, render_template

from flask_pymongo import pymongo
import src.line_segmentation

CONNECTION_STRING = ""
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('my_database')

# Flask constructor
app = Flask(__name__)

def test(myname):
    print('request')
    db.mpr_database.insert_one(myname)
    return "Success"

def imageSegment(img):
    #retrieve image from mongo
    src.line_segmentation.image_read_and_resize(img)
    return render_template("result.html")

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def flask_mongodb_atlas():
    if request.method == "POST":
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        roll_num = request.form.get("roll-number")
        ans1 = request.form.get("file-upload")
        # image_bytes = io.BytesIO()
        # ans1.save(image_bytes, format='JPEG')

        test({"first_name":first_name,
              "last_name":last_name,
              "roll_num":roll_num,
              "Image":ans1})

        return imageSegment(ans1)
    return render_template("form.html")


if __name__=='__main__':
    app.run()

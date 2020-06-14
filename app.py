from flask import Flask,render_template,json,request



app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def function():
    print("Demo Print")
    return "HEllo"
@app.route("/abcd",methods=['GET','POST'])
def fun():
    print("ADithya")
    # print(request.json)
    print(request.json)
    return "Done succusss"

if __name__ == "__main__":
    app.run(debug=True)
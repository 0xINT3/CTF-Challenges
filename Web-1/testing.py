from flask import Flask, render_template
app = Flask(__name__, template_folder='template')

@app.route("/")
def hello():
  return  render_template("index.html")
@app.route("/notice.html")
def maintain():
    return render_template("notice.html")
@app.route("/admin-area/")
def admin():
    return "b4by0da{e4sy-p3asY}"
@app.route("/admin-area")
def admin2():
    return "b4by0da{e4sy-p3asY}"

if __name__ == "__main__":
  app.run(debug=True)


from flask import Flask,render_template
app=Flask(__name__)

posts=[
{
'author':'Kian Dousti',
'title':'Blog post',
'content':'First post content',
'date_posted':'today'
},
{
'author':'Kami Dousti',
'title':'cool post',
'content':'Third post content',
'date_posted':'yesterday'
}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if (__name__=='__main__'):
    app.run(debug=True)

from models import Person,Article
from flask import render_template,request,session,url_for,redirect
from blog import app,db
from forms import SigninForm,SignupForm

@app.route('/')
def index():
    articles = Article.all()
    return render_template('index.html',articles=articles)

@app.route('/signup',methods=['POST','GET'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if not form.validate():
            return render_template('signup.html',form=form)
        else:
            newperson = Person(form.firstname.data,form.lastname.data,form.email.data,form.password.data)
            db.session.add(newperson)
            db.session.commit()
            session['email']=newperson.email
            return redirect(url_for('profile'))
    elif request.method=='GET':
        return render_template('signup.html',form=form)
from models import Person,Article,Category
from flask import render_template,request,session,url_for,redirect
from blog import app,db
from forms import SigninForm,SignupForm,ArticleCreateForm,ArticleUpdateForm,CategoryCreateForm

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

@app.route('/profile',methods=['POST','GET'])
def profile():
    if 'email' not in session:
        return redirect(url_for('signin'))
    person = Person.query.filter_by(email=session['email']).first()
    if person:
        article = Article()
        form = ArticleCreateForm()
        if request.method=='POST' and form.validate_on_submit():
            form.populate_obj(article)
            db.session.add(article)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('create.html',form=form)
    return render_template('profile.html')

@app.route('/signin',methods=['POST','GET'])
def signin():
    if 'email' in session:
        return redirect(url_for('index'))
    form = SigninForm()
    if request.method=='POST':
        if form.validate():
            session['email']=form.email.data
            return redirect(url_for('profile'))
        else:
            return render_template('signin.html',form=form)
    elif request.method=='GET':
        return render_template('signin.html',form=form)

@app.route('/signout')
def signout():
    if 'email' not in session:
        return redirect(url_for('signin'))
    session.pop('email',None)
    return redirect(url_for('index'))

@app.route('/article/<int:id>/<slug>')
def show_article(id,slug):
    article = Article.find_by_id(id)
    return render_template('show_article.html',article=article)


@app.route('/article/<int:id>/<slug>/edit',methods=['POST','GET'])
def update_article(id,slug):
    article = Article.find_by_id(id)
    if article is None:
        return HTTPNotFound(404)
    form = ArticleUpdateForm(request.form,article)
    if form.validate_on_submit():
        form.populate_obj(article)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html',form=form)

@app.errorhandler(404)
def HTTPNotFound(e):
    return render_template('error.html'),404

@app.route('/category/create',methods=['GET','POST'])
def category_create():
    form = CategoryCreateForm()
    category = Category()
    if form.validate_on_submit():
        form.populate_obj(category)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('category.html',form=form)

from flask.ext.wtf import Form
from wtforms import SubmitField, TextField, validators, PasswordField, TextAreaField,HiddenField
from models import Person,Category
from wtforms.ext.sqlalchemy.fields import QuerySelectField

strip_filter = lambda x:x.strip() if x else None



def category_choice():
    return Category.query.all()

class ArticleCreateForm(Form):
    title = TextField('Title',[validators.Required("Please enter title.")],
        filters=[strip_filter])
    body = TextAreaField('Body',[validators.Required("Please enter body.")],
        filters=[strip_filter])
    category = QuerySelectField('Category',query_factory=category_choice)

class ArticleUpdateForm(ArticleCreateForm):
    id = HiddenField()

class SignupForm(Form):
    firstname = TextField("First name",[validators.Required("enter your first name.")])
    lastname = TextField("Last name",[validators.Required("enter your last name.")])
    email = TextField("Email",[validators.Required('Please enter your email address.'),validators.Email("Please enter your email address.")])
    password = PasswordField("Password",[validators.Required("Please enter your password.")])

    def __init__(self,*args,**kargs):
        Form.__init__(self,*args,**kargs)
    def validate(self):
        if not Form.validate(self):
            return False
        person = Person.query.filter_by(email=self.email.data.lower()).first()
        if person:
            self.email.errors.append("That email is already taken")
            return False
        else:
            return True
class SigninForm(Form):
    email = TextField("email",[validators.Required("Please enter your email address.")])
    password = PasswordField("Password",[validators.Required("Please enter your password")])
    submit = SubmitField("Sign In")

    def __init__(self,*args,**kargs):
        Form.__init__(self,*args,**kargs)
    def validate(self):
        if not Form.validate(self):
            return False
        person = Person.query.filter_by(email=self.email.data.lower()).first()
        if person and person.check_password(self.password.data):
            return True
        else:
            return False
class CategoryCreateForm(Form):
    name = TextField('Name',[validators.Required(),validators.Length(min=1,max=120)])
    description = TextAreaField('Discription',[validators.Required()])



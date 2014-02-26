from flas.ext.wtf import Form
from wtforms import TextField, validators, PasswordField, TextAreaField

strip_filter = lambda x:x.strip() if x else None

class ArticleCreateForm(Form):
    title = TextField('Title',[validators.Required("Please enter title.")],
        filters=[strip_filter])
    body = TextAreaField('Body',[validators.Required("Please enter body.")],
        filters=[strip_filter])

class SignupForm(Form):
    firstname = TextField("First name",[validators.Required("enter your first name.")])
    lastname = TextField("Last name",[validators.Required("enter your last name.")])
    email = TextField("Email",[validators.Required('Please enter your email address.'),validators.Email("Please enter your email address.")])


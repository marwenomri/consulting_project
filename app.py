from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,DateField,FloatField,IntegerField,SelectField, SubmitField
from wtforms.validators import DataRequired,InputRequired, NumberRange
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app =Flask(__name__)

#adding database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///factures.db"
#secret key
app.config['SECRET_KEY'] = "secret key"
#initialise database
db = SQLAlchemy(app)

#create model
class factures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mois = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    num_facture = db.Column(db.String(), nullable=False , unique=True)
    fournisseur = db.Column(db.String())
    type = db.Column(db.String())
    code_Frs = db.Column(db.String())
    nom_fournisseur = db.Column(db.String())
    achats = db.Column(db.Float)
    taux_TVA = db.Column(db.Integer)
    DT = db.Column(db.Integer)
    TVA = db.Column(db.Float)
    TTC = db.Column(db.Float)
    mode_reglement = db.Column(db.String())
    JRL = db.Column(db.String())
    cheque_num = db.Column(db.Integer)
    montant = db.Column(db.Float)
    date_reg = db.Column(db.DateTime)
    RS_state = db.Column(db.String())
    taux_RS = db.Column(db.Float)
    RS = db.Column(db.Float)
    NET = db.Column(db.Float)
    code_Frs_fin = db.Column(db.String())

    def __repr__(self):
        return '<facture  %r>' % self.num_facture

# Form class
class FactureForm(FlaskForm):
    date = DateField('Date', format='%'+'d-%m-%Y')
    num_facture = StringField('num de facture', validators=[DataRequired()])
    type = SelectField('type', choices=['a','b'], validators=[DataRequired()])
    achats = FloatField('achats', validators=[DataRequired(), NumberRange(min=0, message='Must enter a number greater than 0')])
    taux_TVA = FloatField('Taux TVA', validators=[DataRequired(), NumberRange(min=0,max=100, message='must be between 0 and 100')])
    DT = IntegerField('DT', validators=[DataRequired(), NumberRange(min=0, message=' must be higher than 0')])
    mode_reglement = SelectField('Mode reglement', choices=['biat','NH'], validators=[DataRequired()])
    JRL =  StringField('JRL', validators=[DataRequired()])
    cheque_num = IntegerField('cheque num', validators=[DataRequired(), NumberRange(min=0, message=' must behigher than 0')])
    RS = SelectField('RS', choices=['RS','sans RS'], validators=[DataRequired()])
    submit = SubmitField('Submit')
    


@app.route('/')
def index():
    first_name='jimbala'
    stuff=' <strong>test123</strong>  '
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff)

#localhost:5000/user/John
@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)


@app.route('/add', methods=['GET','POST'])
def add():
    facture= None
    form =FactureForm()

    if form.validate_on_submit():
        facture =form.facture.data
        form.facture.data = ''

    return render_template('AddFacture.html',
                           facture=facture,
                           form=form)



#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#internal server error message
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500



if __name__ == "__main__":
  app.run(debug=True)
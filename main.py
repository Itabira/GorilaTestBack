from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://odxxzjicrelrqz:f806cd00c1caa79c8b5860718ba813016b52ea64fda3629c575bb2e0ddd8123c@ec2-52-86-116-94.compute-1.amazonaws.com:5432/d4mhk4d2otbeun'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)

class Investments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def __init__(self, value, transaction_type, date):
        self.value = value
        self.transaction_type = transaction_type
        self.date = date

    def __repr__(self):
        return f"Investments(value = {value}, transaction_type = {transaction_type}, date = {date})"
    
db.create_all()

class InvestmentsSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Investments
        sqla_session = db.session
    id = fields.Integer(dump_only=True)
    value = fields.Float(required=True)
    transaction_type = fields.String(required=True)
    date = fields.DateTime(required=True)


@app.route('investments', methods=['GET'])
@cross_origin()
def index():
    get_investments = Investments.query.all()
    investment_schema = InvestmentsSchema(many=True)
    investments = investment_schema.dump(get_investments)
    return make_response(jsonify({"investments": investments}))


@app.route('investments', methods = ['POST'])
@cross_origin()
def create_investment():
    data = request.get_json()
    print(data)
    investment_schema = InvestmentsSchema()
    investments = investment_schema.load(data)
    result = investment_schema.dump(investments.create())
    return make_response(jsonify({"investments": result}),200)


@app.route('investments/<id>', methods = ['DELETE'])
@cross_origin()
def delete_investment_by_id(id):
    get_investment = Investments.query.get(id)
    db.session.delete(get_investment)
    db.session.commit()
    return make_response("",204)


if __name__ == "__main__":
    app.run(debug=True)
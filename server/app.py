from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from flask_migrate import Migrate 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# Define database models
class Hero(db.Model):
    __tablename__ = 'heroes'

    name = db.Column(db.String(255)) 
    super_name = db.Column(db.String(255))  
    id = db.Column(db.Integer, primary_key=True)

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)

    @validates('description')
    def validate_description(self, key, value):
        if not value:
            raise ValueError("Description cannot be empty")
        if len(value) < 10:
            raise ValueError("Description must be at least 10 characters long")
        return value

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)  
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    hero = db.relationship('Hero', backref='hero_powers')
    power = db.relationship('Power', backref='hero_powers')

# Routes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    hero_data = [{'id': hero.id, 'name': hero.name} for hero in heroes]
    return jsonify(hero_data)

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    
    if hero is None:
        return jsonify({'message': 'Hero not found'}), 404
    
    return jsonify({'id': hero.id, 'name': hero.name, 'super_name': hero.super_name})


@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    power_data = [{'id': power.id, 'description': power.description} for power in powers]
    return jsonify(power_data)

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'message': 'Power not found'}), 404
    return jsonify({'id': power.id, 'description': power.description})


@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'message': 'Power not found'}), 404

    new_description = request.json.get('description')
    if new_description:
        power.description = new_description
        db.session.commit()
        return jsonify({'message': 'Power updated successfully'})

    return jsonify({'message': 'No changes provided'}), 400

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')

    if not hero_id or not power_id:
        return jsonify({'message': 'Both hero_id and power_id are required'}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({'message': 'Hero or Power not found'}), 404

    hero_power = HeroPower(hero=hero, power=power)
    db.session.add(hero_power)
    db.session.commit()

    return jsonify({'message': 'HeroPower created successfully'}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555)
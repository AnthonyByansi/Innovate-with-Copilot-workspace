from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['JWT_SECRET_KEY'] = 'jwtsecretkey'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
oauth = OAuth(app)

google = oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    client_kwargs={'scope': 'openid profile email'}
)

facebook = oauth.register(
    name='facebook',
    client_id=os.getenv('FACEBOOK_CLIENT_ID'),
    client_secret=os.getenv('FACEBOOK_CLIENT_SECRET'),
    access_token_url='https://graph.facebook.com/oauth/access_token',
    access_token_params=None,
    authorize_url='https://www.facebook.com/dialog/oauth',
    authorize_params=None,
    client_kwargs={'scope': 'email'}
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/login/google', methods=['POST'])
def login_google():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    user = User.query.filter_by(username=user_info['email']).first()
    if not user:
        user = User(username=user_info['email'], password='')
        db.session.add(user)
        db.session.commit()
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

@app.route('/login/facebook', methods=['POST'])
def login_facebook():
    token = facebook.authorize_access_token()
    resp = facebook.get('me?fields=id,name,email')
    user_info = resp.json()
    user = User.query.filter_by(username=user_info['email']).first()
    if not user:
        user = User(username=user_info['email'], password='')
        db.session.add(user)
        db.session.commit()
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

@app.route('/ideas', methods=['POST'])
@jwt_required()
def create_idea():
    data = request.get_json()
    current_user = get_jwt_identity()
    new_idea = Idea(title=data['title'], description=data['description'], user_id=current_user)
    db.session.add(new_idea)
    db.session.commit()
    return jsonify({'message': 'Idea created successfully'}), 201

@app.route('/ideas', methods=['GET'])
@jwt_required()
def get_ideas():
    current_user = get_jwt_identity()
    ideas = Idea.query.filter_by(user_id=current_user).all()
    output = []
    for idea in ideas:
        idea_data = {'id': idea.id, 'title': idea.title, 'description': idea.description}
        output.append(idea_data)
    return jsonify({'ideas': output}), 200

@app.route('/ideas/<id>', methods=['PUT'])
@jwt_required()
def update_idea(id):
    data = request.get_json()
    current_user = get_jwt_identity()
    idea = Idea.query.filter_by(id=id, user_id=current_user).first()
    if not idea:
        return jsonify({'message': 'Idea not found'}), 404
    idea.title = data['title']
    idea.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Idea updated successfully'}), 200

@app.route('/ideas/<id>', methods=['DELETE'])
@jwt_required()
def delete_idea(id):
    current_user = get_jwt_identity()
    idea = Idea.query.filter_by(id=id, user_id=current_user).first()
    if not idea:
        return jsonify({'message': 'Idea not found'}), 404
    db.session.delete(idea)
    db.session.commit()
    return jsonify({'message': 'Idea deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, Blueprint, request
from booknet_app import app, db
from flask_restx import Api, Resource, fields, reqparse
from booknet_app.models import Store

store_api = Blueprint('store_api', __name__, url_prefix="/api")

api = Api(store_api, version='1.0', title='BookStore API',
        description='A simple BookStore API')

store_ns = api.namespace('stores', description='BookStore operations')

store_model = api.model('Store', {
    'id': fields.Integer(readOnly=True, required=True, description='Store ID'),
    'user_id': fields.Integer(required=True, description='User ID'),
    'storename': fields.String(required=True, description='Store name'),
    'category': fields.String(required=False, description='Store category'),
    'seats': fields.Integer(required=True, description='Store seats'),
    'adresse': fields.String(required=True, description='Store adress'),
    'city': fields.String(required=True, description='Store city'),
    'beschreibung': fields.String(required=False, description='Store description'),
})


@api.errorhandler
def std_handler(e):
    return {'message': 'An unexpected error has ocurred.'}, 500

@store_ns.route('/')
class StoreList(Resource):
    @store_ns.doc('list_stores')
    @store_ns.marshal_with(store_model, as_list=True)
    @store_ns.response(200, 'Success')
    @store_ns.response(400, 'Bad Request')
    @store_ns.response(404, 'Not Found')
    @store_ns.response(500, 'Internal Server Error')
    def get(self):
        """Returns a list of stores"""
        # parser = reqparse.RequestParser()
        # parser.add_argument('page', type=int, required=False, default=1, help='Page number')
        # parser.add_argument('page_size', type=int, required=False, default=10, help='Page size')
        # args = parser.parse_args()
        # page = args.get('page')
        # page_size = args.get('page_size')

        # Get all stores from database
        stores = Store.query.all()

        return stores, 200

    @store_ns.doc('post_store')
    @store_ns.marshal_with(store_model)
    def post(self):
        # Define request parser
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=str, required=True, help='User ID')
        parser.add_argument('storename', type=str, required=True, help='Storename')
        parser.add_argument('category', type=str, required=False, help='Store category')
        parser.add_argument('seats', type=str, required=True, help='Store seats')
        parser.add_argument('adresse', type=str, required=True, help='Store adress')
        parser.add_argument('city', type=str, required=True, help='Store city')
        parser.add_argument('beschreibung', type=str, required=True, help='Store description')
        
        args = parser.parse_args()

        user_id = args.get('user_id')
        storename = args.get('storename')
        category = args.get('category')
        seats = args.get('seats')
        adresse = args.get('adresse')
        city = args.get('city')
        beschreibung = args.get('beschreibung')
        
        store = Store(user_id=user_id, storename=storename, category=category, seats=seats, 
                      adresse=adresse, store_bild="book_store.jpg", city=city, beschreibung=beschreibung)
        db.session.add(store)
        db.session.commit()
        
        return {'message': 'Store created successfully!'}, 201
    
@api.route('/store/<int:id>')
class StoreItem(Resource):
    @api.doc('get_store')
    @api.marshal_with(store_model)
    def get(self, id):
        store = db.session.query(Store).filter(Store.id==id).first()
        if not store:
            api.abort(404, "Store not found")
        return store, 200

    @api.doc('edit_store')
    @api.marshal_with(store_model)
    def put(self,id):
        store = db.session.query(Store).filter(Store.id==id).first()
        if not store:
            api.abort(404, "Store not found")
        
        # Define request parser
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=str, required=True, help='User ID')
        parser.add_argument('storename', type=str, required=True, help='Storename')
        parser.add_argument('category', type=str, required=False, help='Store category')
        parser.add_argument('seats', type=str, required=True, help='Store seats')
        parser.add_argument('adresse', type=str, required=True, help='Store adress')
        parser.add_argument('city', type=str, required=True, help='Store city')
        parser.add_argument('beschreibung', type=str, required=True, help='Store description')
        
        args = parser.parse_args()

        store.user_id = args.get('user_id')
        store.name = args.get('storename')
        store.category = args.get('category')
        store.seats = args.get('seats')
        store.adresse = args.get('adresse')
        store.city = args.get('city')
        store.beschreibung = args.get('beschreibung')
  
        db.session.commit()
        return store, 200
    
    @api.doc('delete_store')
    @api.marshal_with(store_model)
    def delete(self, id):
        # Delete store from database
        store = db.session.query(Store).filter(Store.id==id).first()
        if store is None:
            api.abort(404, 'Store not found')

        db.session.delete(store)
        db.session.commit()
        return '', 204
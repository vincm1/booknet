from flask import request
from booknet_app import app, db
from flask_restx import Api, Resource, fields, reqparse
from flask import Flask, Blueprint
from booknet_app.models import Store

store_api = Blueprint('store_api', __name__, url_prefix="/api")

api = Api(store_api, version='1.0', title='BookStore API',
        description='A simple BookStore API')

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('page', type=int, required=False, default=1, help='Page number')
pagination_arguments.add_argument('per_page', type=int, required=False, choices=[2, 10, 20, 30, 40, 50],
                        default=10, help='Results per page')

store_ns = api.namespace('stores', description='BookStore operations')

store_model = api.model('Store', {
    'id': fields.Integer(readOnly=True),
    'user_id': fields.Integer(required=True),
    'storename': fields.String(required=True),
    'category': fields.String(required=False),
    'seats': fields.Integer(required=True),
    'adresse': fields.String(required=True),
    'city': fields.String(required=True),
    'beschreibung': fields.String(required=False),
})

@api.errorhandler
def std_handler(e):
    return {'message': 'An unexpected error has ocurred.'}, 500

@store_ns.route('/')
class Stores(Resource):
    @store_ns.doc('list_stores')
    @store_ns.marshal_with(store_model, envelope='resource')
    @store_ns.expect(pagination_arguments)
    @store_ns.response(200, 'Success')
    @store_ns.response(400, 'Bad Request')
    @store_ns.response(404, 'Not Found')
    @store_ns.response(500, 'Internal Server Error')
    def get(self):
        """Returns a list of stores"""
        args = pagination_arguments.parse_args()
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        stores = Store.query.paginate(page=page, per_page=per_page).items

        return stores

    @store_ns.doc('create_store')
    @store_ns.expect(store_model)
    @store_ns.response(201, 'Store created successfully')
    @store_ns.response(400, 'Bad Request')
    @store_ns.response(409, 'Conflict')
    @store_ns.response(500, 'Internal Server Error')
    def post(self):
        '''Create a new store'''
        store = Store(**api.payload)
        db.session.add(store)
        db.session.commit()

        return {'message': 'Store created successfully'}, 201
    
@store_ns.route('/store/<int:id>')
class StoreItem(Resource):
    @store_ns.doc('get_store')
    @store_ns.marshal_with(store_model)
    def get(self, id):
        store = db.session.query(Store).filter(Store.id==id).first()
        if not store:
            api.abort(404, "Store not found")
        return store
    
    def put(self,id):
        pass
    
    def delete(self, id):
        pass
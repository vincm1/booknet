from flask_restx import Api, Resource, fields, reqparse
### Pagination
pagination_parser = reqparse.RequestParser()
pagination_parser.add_argument('page', type=int, required=False, default=1, help='Page number')
pagination_parser.add_argument('stores_per_page', type=int, required=False, choices=[2, 10, 20, 30, 40, 50],
                        default=10, help='Stores per page')
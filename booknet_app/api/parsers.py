from flask_restx import reqparse

pagination_parser = reqparse.RequestParser()
pagination_parser.add_argument('page', type=int, required=False, default=1, help='Page number')
pagination_parser.add_argument('per_page', type=int, required=False, choices=[2, 10, 20, 30, 40, 50],
                        default=10, help='Results per page')
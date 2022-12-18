from booknet_app import app, db


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        #if not User.query.filter_by(name="MaxMuster").first():
        #     User.create_user(name="MaxMuser")
    app.run(debug=True)
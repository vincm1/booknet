from booknet_app import app, db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # if not User.query.filter_by(username="MaxMuster").first():
        #     user1 = User(username="Maxmuster", email="max@web.de", passwort="helloworld")
        #     db.session.add(user1)
        #     db.session.commit()
    app.run(debug=True, threaded=True)
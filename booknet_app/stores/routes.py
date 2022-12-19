from flask import Flask, Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required
from booknet_app import db
from booknet_app.models import Store
from booknet_app.stores.forms import AddStoreForm

stores = Blueprint('stores', __name__)

@login_required
@stores.route('/stores', methods=['GET', 'POST'])
def all_stores():
    form = AddStoreForm()
    stores = db.session.query(Store).all()
    return render_template('stores/all_stores.html', stores=stores, form=form)

@login_required
@stores.route('/add_store', methods=['GET', 'POST'])
def add_store():

    form = AddStoreForm()

    if form.validate_on_submit() and request.method == "POST":
        store = Store(storename=form.storename.data, adresse=form.adresse.data, 
        beschreibung=form.beschreibung.data, user_id = current_user.id)
        db.session.add(store)
        db.session.commit()
        flash('Store hinzugefügt!')
        return render_template('stores/all_stores.html', form=form)
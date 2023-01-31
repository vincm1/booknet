from datetime import datetime
from flask import Flask, Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required
from booknet_app import db
from booknet_app.models import Store
from booknet_app.stores.forms import StoreForm
from booknet_app.picture_handler import save_store_picture

stores = Blueprint('stores', __name__)

@login_required
@stores.route('/stores', methods=['GET', 'POST'])
def all_stores():
    '''df'''
    form = StoreForm()   
    
    page = request.args.get('page', 1, type=int)
    stores = Store.query.order_by(Store.creation_date.desc()).paginate(page=page, per_page=12)
    time_now = datetime.now()
    cities = db.session.query(Store.city).distinct()
    
    return render_template('stores/all_stores.html', stores=stores, form=form, time_now=time_now, cities=cities) 

@login_required
@stores.route('/store/<int:store_id>', methods=['GET','POST'])
def store(store_id):
    '''df'''
    store = Store.query.get_or_404(store_id)
    form = StoreForm()
    return(render_template('stores/store.html', store=store, store_id=store_id, form=form))

@login_required
@stores.route('/add_store', methods=['GET', 'POST'])
def add_store():
    '''df'''
    form = StoreForm()

    if form.validate_on_submit() and request.method == "POST":
        if form.storebild.data:
            picture_file = save_store_picture(form.storebild.data)
            store = Store(storename=form.storename.data, store_bild=picture_file, city=form.city.data, 
                          seats=form.seats.data, category=form.category.data, adresse=form.adresse.data,
                          beschreibung=form.beschreibung.data, user_id=current_user.id)
            db.session.add(store)
            db.session.commit()
            return redirect(url_for('stores.all_stores'))
        else:
            store = Store(storename=form.storename.data, store_bild="book_store.jpg", adresse=form.adresse.data, 
                        seats=form.seats.data, category=form.category.data, beschreibung=form.beschreibung.data, 
                        city=form.city.data, user_id=current_user.id)
            db.session.add(store)
            db.session.commit()
            return redirect(url_for('stores.all_stores'))
    
    time_now = datetime.now() 
    
    return render_template('stores/all_stores.html', form=form, stores=stores, time_now=time_now)

@login_required
@stores.route('/store/<int:store_id>/edit', methods=['GET', 'POST'])
def edit_store(store_id):
    '''df'''
    store = Store.query.get_or_404(store_id)

    if store.user_id != current_user.id:
        abort(403)

    form = StoreForm()

    if form.validate_on_submit() and request.method == "POST":
        if form.storebild.data:
            picture_file = save_store_picture(form.storebild.data)
            store.store_bild = picture_file
        store.storename = form.storename.data
        store.adresse = form.adresse.data
        store.beschreibung = form.beschreibung.data
        db.session.commit()
        flash('Store erfolgreich geupdatet!')
        return redirect(url_for('stores.store', store_id=store.id))

    elif request.method == "GET":
        form.storename.data = store.storename
        form.adresse.data = store.adresse
        form.beschreibung.data = store.beschreibung
        form.storebild.data = store.store_bild

    store_bild = url_for('static', filename='store_pics/' + store.store_bild)
    return render_template('stores/all_stores.html', form=form, store_bild=store_bild)

@login_required
@stores.route('/store/<int:store_id>/delete', methods=['POST'])
def delete_store(store_id):
    '''df'''
    store = Store.query.get_or_404(store_id)

    if store.user_id != current_user.id:
        abort(403)
    
    db.session.delete(store)
    db.session.commit()

    flash("Store deleted!")
    
    return redirect(url_for('stores.all_stores'))

@login_required
@stores.route('/stores/<city>', methods=['GET','POST'])
def store_city(city):
    '''df'''
    form = StoreForm()
    
    page = request.args.get('page', 1, type=int)
    stores = Store.query.filter_by(city=city).order_by(Store.creation_date.desc()).paginate(page=page, per_page=12)
    time_now = datetime.now()
    
    if stores:
        return render_template('stores/city_store.html', stores=stores, form=form, time_now=time_now)
    
    else:
        return redirect(url_for('stores.all_stores'))

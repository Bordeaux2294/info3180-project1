"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from app.form import CreateProperty
from app.models import PropertyProfile


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['POST','GET'])
def properties():
    """Render the website's properties creation form."""
    form = CreateProperty()

    if request.method == 'POST':
        if form.validate_on_submit:

            title = form.title.data
            description = form.description.data
            bedrooms = form.bedrooms.data
            bathrooms = form.bathrooms.data
            price = form.price.data
            type = form.type.data
            location = form.location.data
            image = form.image.data
            
            image_name = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
            
            property = PropertyProfile(title, description, bedrooms, bathrooms, price, type, location, image_name)
            
            #added the property profile to the database
            db.session.add(property)
            db.session.commit()
            
            flash("Property Successfully Added", "Success")
            
            return redirect(url_for('viewproperties'))

    return render_template('property.html', form=form)

@app.route('/properties')
def viewproperties():
    """Render the website's list of properties."""
    return render_template('properties.html', properties= list_properties())



def list_properties():
    results = PropertyProfile.query.all()
    properties = []
    for property in results:
        properties.append([property.id, property.image_name, property.title, property.location, property.price])
    return properties

@app.route("/properties/<filename>")
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)



@app.route("/properties/<propertyid>/")
def specific_property(propertyid):
    return render_template("individual.html", propid= get_property(propertyid))


def get_property(propertyid):
    property = db.session.execute(db.select(PropertyProfile).filter_by(id=propertyid)).scalar()
    return property




###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from flask_babel import _
from app import db
from app.rover import bp

@bp.route('/rover', methods=['GET','POST'])	
def rover():
	return render_template('rover/rover.html', title=_('Rover'))
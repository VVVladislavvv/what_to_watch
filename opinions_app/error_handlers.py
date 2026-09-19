from . import app, db
from flask import render_template


@app.errorhandler(500)
def internal_error(error):
    # чтобы в базу не записалось ничего лишнего.
    db.session.rollback()
    # вернётся страница, сгенерированная на основе шаблона 500.html.
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(error):
    # При ошибке 404 в качестве ответа вернётся страница, созданная
    # на основе шаблона 404.html и код HTTP-ответа 404.
    return render_template('404.html'), 404

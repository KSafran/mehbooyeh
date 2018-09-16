"""routes"""
from flask import Blueprint, current_app, render_template, request
from .model import mehbooyeh, db
from .forms import MBYForm

BLUEPRINT = Blueprint("BLUEPRINT", __name__)


@BLUEPRINT.route("/", methods=['GET', 'POST'])
def add_boop():
    form = MBYForm(request.form)
    import pdb; pdb.set_trace()

    if request.method == 'POST' and form.validate():
        import pdb; pdb.set_trace()

        reg = mehbooyeh(form.name.data, form.mby.data)
        db.session.add(reg)
        db.session.commit()
        return render_template('success.html')
    return render_template('index.html', form = form)


@BLUEPRINT.route('/reg', methods=['POST'])
def reg():
    form = MBYForm(request.form)
    if request.method == 'POST':
        name = request.form['name']
        item = request.form['item']
        reg = mehbooyeh(name, item)
        db.session.add(reg)
        db.session.commit()
        return render_template('success.html')
    return render_template('index.html')

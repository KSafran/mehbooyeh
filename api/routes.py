"""routes"""
from flask import Blueprint, current_app, render_template, request, redirect
from .model import mehbooyeh, db
from .forms import MBYForm

BLUEPRINT = Blueprint("BLUEPRINT", __name__)


@BLUEPRINT.route("/", methods=['GET', 'POST'])
def add_boop():
    form = MBYForm(request.form)
    if request.method == 'POST' and form.validate():
        reg = mehbooyeh(form.name.data, form.mby.data)
        db.session.add(reg)
        db.session.commit()
        meh_id = reg.id
        return redirect('/meh/' + str(meh_id))
    return render_template('index.html', form = form)

@BLUEPRINT.route('/meh/<meh_id>', methods=['GET','POST'])
def meh_id(meh_id):

    meh = db.session.query(mehbooyeh).filter(mehbooyeh.id == meh_id).first()
    return render_template('mehbooyeh.html',
                           name=meh.name, item=meh.item,
                           mehs=meh.mehs, boos=meh.boos, yehs=meh.yehs)

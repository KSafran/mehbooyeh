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
        vote_id = reg.id
        return redirect('/vote/' + str(vote_id))
    return render_template('index.html', form = form)

@BLUEPRINT.route('/vote/<vote_id>', methods=['GET','POST'])
def vote_id(vote_id):

    vote = db.session.query(mehbooyeh).filter(mehbooyeh.id == vote_id).first()
    return render_template('mehbooyeh.html',
                           name=vote.name, item=vote.item, vote_id=vote_id,
                           mehs=vote.mehs, boos=vote.boos, yehs=vote.yehs)

@BLUEPRINT.route('/meh/<vote_id>', methods=['GET','POST'])
def meh(vote_id):
    vote = db.session.query(mehbooyeh).filter(mehbooyeh.id == vote_id).first()
    vote.mehs += 1
    db.session.commit()
    return redirect('/vote/' + str(vote_id))

@BLUEPRINT.route('/boo/<vote_id>', methods=['GET','POST'])
def boo(vote_id):
    vote = db.session.query(mehbooyeh).filter(mehbooyeh.id == vote_id).first()
    vote.boos += 1
    db.session.commit()
    return redirect('/vote/' + str(vote_id))

@BLUEPRINT.route('/yeh/<vote_id>', methods=['GET','POST'])
def yeh(vote_id):
    vote = db.session.query(mehbooyeh).filter(mehbooyeh.id == vote_id).first()
    vote.yehs += 1
    db.session.commit()
    return redirect('/vote/' + str(vote_id))

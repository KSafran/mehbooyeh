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

@BLUEPRINT.route('/<vote_type>/<vote_id>', methods=['GET','POST'])
def tally_vote(vote_id):
    vote = db.session.query(mehbooyeh).filter(mehbooyeh.id == vote_id).first()
    getattr(vote, vote_type) += 1
    db.session.commit()
    return redirect('/vote/' + str(vote_id))

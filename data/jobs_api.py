import flask
from flask import jsonify, request, Blueprint

from . import db_session
from .jobs import Jobs


blueprint = Blueprint('jobs_api', __name__,template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {'jobs': [item.to_dict(
            only=('id', 'job', 'team_leader', 'work_size', 'collaborators',
              'start_date', 'end_date', 'is_finished'))
            for item in jobs]})
    # return jsonify(
    #     {'jobs': [item.to_dict(
    #         only=('id', 'job', 'team_leader', 'work_size', 'collaborators',
    #           'start_date', 'end_date', 'is_finished'))
    #     for item in jobs]})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_news(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': jobs.to_dict(rules=('-user', '-user.jobs'))
        }
    )
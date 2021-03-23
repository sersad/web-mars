from flask import jsonify
from flask_restful import abort, reqparse, Resource

from . import db_session
from .jobs import Jobs

parser = reqparse.RequestParser()
parser.add_argument('team_leader', required=True, type=int)
parser.add_argument('job', required=True)
parser.add_argument('work_size', required=False, type=int)
parser.add_argument('collaborators', required=True)
parser.add_argument('start_date', required=False)
parser.add_argument('end_date', required=False)
parser.add_argument('is_finished', required=False, type=bool)


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs':
                            [item.to_dict(rules=('-user', '-user.jobs')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=args['start_date'],
            end_date=args['end_date'],
            is_finished=args['is_finished'],
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        user = session.query(Jobs).get(job_id)
        return jsonify(
            {'jobs': user.to_dict(rules=('-user', '-user.jobs'))})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")

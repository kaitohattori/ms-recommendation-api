from flasgger import swag_from
from flask import Blueprint
from flask import jsonify
from flask import request

from app.models.video import Video


app = Blueprint('video', __name__)

@app.route('/videos/recommended/', methods=['GET'])
def get_recommended_videos():
    """ Find recommended videos
    ---
    tags:
      - Videos
    parameters:
      - name: user_id
        in: query
        type: string
        required: false
      - name: limit
        in: query
        type: integer
        required: false
    produces:
      - application/json
    definitions:
      Video:
        type: object
        properties:
          id:
            example: 1
            type: integer
          userId:
            example: test-user
            type: string
          title:
            example: Spider-Man 1
            type: string
          createdAt:
            format: date-time
            type: string
          updatedAt:
            format: date-time
            type: string
    responses:
      200:
        description: Recommended Videos
        schema:
          $ref: '#/definitions/Video'
    """
    user_id = request.args.get('user_id')
    limit_str = request.args.get('limit')
    limit = int(limit_str) if limit_str is not None else None
    videos = Video.find_all_recommended(user_id=user_id, limit=limit)
    return jsonify(list(map(lambda x: x.json, videos)))

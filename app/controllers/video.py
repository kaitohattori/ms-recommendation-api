import logging

from flask import Blueprint, jsonify, request

from app.models.video import Video

app = Blueprint("video", __name__)
logger = logging.getLogger(__name__)


@app.route("/videos/recommended/", methods=["GET"])
def get_recommended_videos():
    """Find recommended videos
    ---
    tags:
      - Videos
    parameters:
      - name: user_id
        in: query
        type: string
        required: true
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
          items:
            $ref: '#/definitions/Video'
    """
    user_id = request.args.get("user_id")
    if user_id is None or user_id == "":
        return jsonify({"message": "user_id is required"}), 400
    limit_str = request.args.get("limit")
    limit = int(limit_str) if limit_str is not None else None

    videos = Video.find_all_recommended(user_id=user_id, limit=limit)

    json_videos = []
    for video in videos:
        json_videos.append(video.json)

    return jsonify(json_videos)

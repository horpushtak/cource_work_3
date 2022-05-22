import logging

from flask import Blueprint, jsonify
from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO

api_blueprint = Blueprint('api_blueprint', __name__)

posts_dao = PostsDAO('data/data.json')
comments_dao = CommentsDAO('data/comments.json')
logger = logging.getLogger('basic')


@api_blueprint.route('/api/posts/')
def posts_all():
    logger.debug("Запрошены все посты через API")  # Что значит "запрошены через API" я-таки до конца и не въехал
    posts = posts_dao.get_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_pk>/')
def post_one(post_pk):
    logger.debug(f"Запрошены пост с pk {post_pk} через API")
    post = posts_dao.get_post_by_pk(post_pk)
    return jsonify(post)

"""Ого, если я подготовил правильно объекты, которые манипулируют данными, то создание новых вьюшек"""
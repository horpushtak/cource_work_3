import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request
from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
posts_dao = PostsDAO('data/data.json')
comments_dao = CommentsDAO('data/comments.json')
logger = logging.getLogger('basic')


@posts_blueprint.route('/')
def posts_all():
    logger.debug("Запрошены все посты")
    try:
        posts = posts_dao.get_all()
        return render_template('index.html', posts=posts)
    except:
        return "Что-то не так"


@posts_blueprint.route('/posts/<int:post_pk>/')
def post_one(post_pk):
    logger.debug(f"Запрошен пост {post_pk}")

    try:
        post = posts_dao.get_post_by_pk(post_pk)
        comments = comments_dao.get_by_post_pk(post_pk)
    except (JSONDecodeError, FileNotFoundError) as error:
        return render_template("error.html", error=error)
    except BaseException:  # Что такое BaseException?
        return render_template("error.html", error="Неизвестная ошибка")
    number_of_comments = len(comments)
    return render_template('post.html', post=post, comments=comments, number_of_comments=number_of_comments)


@posts_blueprint.route('/search/')
def posts_search():
    query = request.args.get("s", "")  # Либо получить что-то, либо пустую строку,
    # чтобы None в шаблоне не светилась и не пачкала
    # Поискать про переменную "s", это - то, что в шаблоне устанавливается как name="s" в инпуте, например
    # if "s" in request.args:
    #     query = request.args["s"]
    # else:
    #     query = ""
    # Всё, что flask принял от пользователя, он кидает в request
    # args - это одна из "коробочек", где лежит то, что он туда скинул
    # сегменты маршрута /.../, аргументы - это уточнения сегмента; аргументы, они же - параметры
    if query != "":  # Зачем тут условие, если цикл есть в шаблоне?
        posts = posts_dao.search(query)
        number_of_posts = len(posts)
    else:
        posts = []
        number_of_posts = 0  # Затем, что нужно ещё передать переменные в шаблон, чтобы там они заработали
    return render_template("search.html", query=query, posts=posts, number_of_posts=number_of_posts)


@posts_blueprint.route('/users/<user_name>')
def posts_by_user(user_name):
    posts = posts_dao.get_posts_by_user(user_name)
    return render_template("user-feed.html", posts=posts)


@posts_blueprint.errorhandler  # errorhandler - это ...?
# Способ поймать ошибку и красиво с ней совладать (handle it)
# написать функцию, которая выведет мне красивое сообщение об ошибке
# по шаблону, к примеру
def post_error(e):  # Зачем нужна (e)?
    return "Такой пост не найден", 404  # Куда статус-код передаётся?

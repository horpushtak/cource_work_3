import json


class PostsDAO:
    """ Класс, ответственный за работу с постами """

    def __init__(self, path):
        self.path = path

    def _load(self):
        with open(f'{self.path}', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def get_all(self):
        """ Возвращает все посты """
        return self._load()

    def get_post_by_pk(self, pk):
        """ Возвращает пост по идентификатору """
        posts = self.get_all()

        for post in posts:
            if post["pk"] == pk:
                return post

    def get_posts_by_user(self, user_name):
        """ Возвращает список постов по имени пользователя """
        posts = self.get_all()
        posts_by_user = []

        try:
            for post in posts:
                if post["poster_name"] == user_name:
                    posts_by_user.append(post)
        except ValueError:
            return "Такого пользователя нет"
        else:
            return posts_by_user

    def search_for_posts(self, query):
        """ Возвращает список словарей по вхождению query """
        posts = self.get_all()
        matching_posts = []
        query_lower = query.lower()

        for post in posts:
            if query_lower in post["content"].lower():
                matching_posts.append(post)
        return matching_posts

import pytest

from app.posts.dao.posts_dao import PostsDAO


class TestsPostsDAO:

    @pytest.fixture  # Фикстура - это
    # Фикстура помогает очень быстро поменять путь файла и структуру, чтобы тест работал с внимание
    # Не нужно будет переписывать всю логику тестов, они снова будут работать
    def posts_dao(self):
        return PostsDAO('data/data.json')  # Важно понять, откуда запускается тест
        # print(os.getcwd()) нам в помощь

    @pytest.fixture
    def keys_expected(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    def test_get_all_check_types(self, posts_dao):  # Проверить тип важно, чтобы ...
        posts = posts_dao.get_all()
        assert type(posts) == list
        assert type(posts[0]) == dict

    # Как определять, что за тесты нам нужны?
    # Предполагать все возможные ситуации, для начала проверять все возможные варианты ввода данных
    # Мало ли кто чего нажмакает

    def test_get_all_has_keys(self, posts_dao, keys_expected):  # Передавать фикстуры можно в любом порядке
        # Проверить структуру важно, чтобы вся логика работы с данными не поломалась,
        # так мне кажется во всяком случае
        posts = posts_dao.get_all()
        first_post = posts[0]
        first_post_keys = set(first_post.keys())  # Уникализирует и позволяет не обращать внимание на порядок
        assert first_post_keys == keys_expected, "Полученные ключи неверны"

    def test_get_one_check_type_check(self, posts_dao):  # Проверить один пост
        post = posts_dao.get_post_by_pk(1)
        assert type(post) == dict

    def test_get_one_has_keys(self, posts_dao, keys_expected):
        post = posts_dao.get_post_by_pk(1)
        post_keys = set(post.keys())  # set() здесь полезна, чтобы не зависеть от порядка, в который собраны данные
        assert post_keys == keys_expected, "Полученные ключи неверны"

    parametrs_to_get_by_pk = [1, 2, 3, 4, 5, 6, 7, 8]

    # здесь включается параметризация
    # 1. называем переменную, с которой дальше будем работать
    # 2. скармливаем то, откуда надо брать значения (в теории было написано, что тут обычно список кортежей)
    # потому что это неизменяемые данные
    @pytest.mark.parametrize("post_pk", parametrs_to_get_by_pk)
    def test_get_one_has_correct_pk(self, posts_dao, post_pk):
        post = posts_dao.get_post_by_pk(post_pk)
        assert post["pk"] == post_pk, "Номер поста не тот, что в запрошенном"


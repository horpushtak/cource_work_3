import pytest

from app.posts.dao.comments_dao import CommentsDAO


class TestCommentsDAO:

    @pytest.fixture
    def comments_dao(self):
        return CommentsDAO('tests/mock/comments.json')  # Это что ещё за зверь?
        # Это, во-первых, чтобы не поломать основной сайт
        # Во-вторых, чтобы не привязываться к тому, что может поменяться

    @pytest.fixture
    def keys_expected(self):
        return "post_pk", "commenter_name", "comment", "pk"

    def test_get_by_post_pk(self, comments_dao):
        comments = comments_dao.get_by_post_pk(1)
        assert type(comments) == list, "Результат должен быть списком"
        assert type(comments[0]) == dict, "Результат должен быть словарем"

    def test_get_by_post_pk_check_keys(self, comments_dao, keys_expected):
        comments = comments_dao.get_by_post_pk(1)[0]
        comment_keys = set(comments.keys())
        assert comment_keys == keys_expected

    parameters_for_posts_and_comments = [
        (1, {1, 2}),
        (2, {7}),
        (0, set())
    ]

    @pytest.mark.parametrize("post_pk, correct_comments_pk", parameters_for_posts_and_comments)
    def test_get_by_post_pk_check_match(self, comments_dao, post_pk, correct_comments_pk,):
        comments = comments_dao.get_by_post_pk(post_pk)
        comments_pks = set(comment['pk'] for comment in comments)
        assert comments_pks == correct_comments_pk, f'Не совпадают pks комментов поста {post_pk}'




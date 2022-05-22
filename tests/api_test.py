from main import app
from app.posts.tests.comments_dao_test import TestCommentsDAO
test_comments = TestCommentsDAO


class TestApi:

    def test_app_all_posts_staus_code(self):
        """������� �� ���������� ������"""
        responce = app.test_client().get("/api/posts", follow_redirects=True)

        assert responce.status_code == 200, "������-��� ������� ���� ������ ��������"
        assert responce.mimetype == "application/json", "������� �� JSON"

    def test_app_one_post_status_code(self):
        """������� �� ���������� ������ (��� ������ �����)"""
        responce = app.test_client().get("/api/posts/1", follow_redirects=True)
        keys_expected = test_comments.keys_expected
        assert responce.keys == keys_expected, "�������� �����"
        assert responce.status_code == 200, "������-��� ������� ���� ������ ��������"
        assert responce.mimetype == "application/json", "������� �� JSON"

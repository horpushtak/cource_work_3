import json


class CommentsDAO:

    def __init__(self, path):
        self.path = path

    def _load_comments(self):
        """��������� ��� �����������"""
        with open(self.path, 'r', encoding='utf8') as f:
            data = json.load(f)
        return data

    def get_by_post_pk(self, post_pk):
        """�������� ����������� � ����� �� ��������������"""
        comments = self._load_comments()
        comments_by_pk = []
        try:
            for comment in comments:
                if comment["post_pk"] == post_pk:
                    comments_by_pk.append(comment)
        except ValueError:
            return "������ ����� ���"
        else:
            return comments_by_pk

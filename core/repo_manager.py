# 仓库管理模块，订阅/取消订阅功能
class RepoManager:
    def __init__(self):
        self.repositories = []

    def add_repository(self, user, repo):
        self.repositories.append({'user': user, 'repo': repo})

    def remove_repository(self, user, repo):
        self.repositories = [r for r in self.repositories if not (r['user'] == user and r['repo'] == repo)]

    def list_subscribed_repositories(self, user):
        return [r for r in self.repositories if r['user'] == user]

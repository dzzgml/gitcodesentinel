import unittest
from core.repo_manager import RepoManager

class TestRepoManager(unittest.TestCase):
    def test_add_repository(self):
        repo_manager = RepoManager()
        repo_manager.add_repository('user1', 'repo1')
        self.assertEqual(len(repo_manager.repositories), 1)

    def test_remove_repository(self):
        repo_manager = RepoManager()
        repo_manager.add_repository('user1', 'repo1')
        repo_manager.remove_repository('user1', 'repo1')
        self.assertEqual(len(repo_manager.repositories), 0)

    def test_list_subscribed_repositories(self):
        repo_manager = RepoManager()
        repo_manager.add_repository('user1', 'repo1')
        repos = repo_manager.list_subscribed_repositories('user1')
        self.assertEqual(len(repos), 1)

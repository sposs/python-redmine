from unittest import mock, TestCase

from redminelib import Redmine


class BaseRedmineTestCase(TestCase):
    url = 'https://foo.bar'
    patch_prefix = 'patch'
    patch_targets = {'requests': 'redminelib.engines.sync.requests.Session.request'}

    def setUp(self):
        self.redmine = Redmine(self.url)
        self.response = mock.Mock(**{'status_code': 200, 'history': [], 'request.url': self.url})

        for target, path in self.patch_targets.items():
            setattr(self, f'{self.patch_prefix}_{target}', mock.patch(path, return_value=self.response).start())

        self.addCleanup(mock.patch.stopall)

    def set_patch_side_effect(self, side_effect):
        for target in self.patch_targets:
            getattr(self, f'{self.patch_prefix}_{target}').side_effect = side_effect

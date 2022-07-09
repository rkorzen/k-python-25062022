import pytest


def count_status(statuses: dict, status) -> int:
    return list(statuses.values()).count(status)


class TestOnlineStatuses:
    @pytest.fixture
    def statuses(self):
        s = {
            "Alice": "online",
            "Bob": "offline",
            "Eve": "online",
        }
        return s

    def test_correct_statuses(self, statuses):
        assert count_status(statuses, "online") == 2
        assert count_status(statuses, "offline") == 1
        assert count_status(statuses, "xxx") == 0

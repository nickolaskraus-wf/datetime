from datetime import date, datetime
from unittest import TestCase
from unittest.mock import patch
from zoneinfo import ZoneInfo

import to_ct


class TestToCt(TestCase):
    def setUp(self):
        super(TestToCt, self).setUp()

    def test(self):
        # 1970-01-01
        #
        # See: https://docs.python.org/3/library/datetime.html#datetime.date
        d = date(1970, 1, 1)
        actual = to_ct.to_ct(d)
        # 1970-12-31 18:00:00-06:00
        #
        # See: https://docs.python.org/3/library/datetime.html#datetime.datetime
        expected = datetime(1969, 12, 31, 18, 0, 0, tzinfo=ZoneInfo("US/Central"))
        self.assertEqual(expected, actual)

    def test_raise(self):
        self.mock_logging = patch.object(to_ct, "logging").start()
        d = datetime(1970, 1, 1)
        with self.assertRaises(TypeError):
            _ = to_ct.to_ct(d)
            self.mock_logging.assert_called_with(
                "ERROR: Argument must be of type datetime.datetime"
            )

import unittest


def age_check(age):
    if not isinstance(age, (float, int)):
        raise ValueError

    if 0 <= age <= 8:
        return('Пиздюк')
    elif 9 <= age <= 18:
        return('Пиздюк+')
    elif 19 <= age <= 25:
        return('ПиздюкSSS+')
    elif 26 <= age <= 60:
        return('Старость')
    elif 61 <= age <= 101:
        return('Сигма')
    else:
        raise ValueError


class TestAge(unittest.TestCase):

    def test_pizduk(self):
        age = 9
        expected_result = 'Пиздюк+'
        function_result = age_check(age)
        self.assertEqual(expected_result, function_result)

    def test_zvizduk(self):
        age = 'oh, u live on twitch?..'
        with self.assertRaises(ValueError):
            age_check(age)

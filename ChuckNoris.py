import unittest
import requests

URL = 'https://api.chucknorris.io/jokes/random'
icon_url = "https://assets.chucknorris.host/img/avatar/chuck-norris.png"


class ChuckNorrisTestCase(unittest.TestCase):

    response = None
    data = None

    @classmethod
    def setUpClass(cls):
        cls.response = requests.get(URL)

    """Check response URL"""
    def test_is_request_ok(self):
        response = requests.get(URL)
        print('Response Status: {}'.format(response.status_code))
        self.assertEqual = (response.status_code, 200)

    """Check get random joke"""
    def test_get_joke(self):
        response = requests.get(URL)
        data = response.json()
        joke_text = data["value"]
        print(joke_text)
        self.assertTrue(joke_text)

    """ Check id is in a joke"""
    def test_check_id(self):
        response = requests.get(URL)
        data = response.json()
        print(data['id'])
        self.assertTrue(id)

    """ Check created_at is in a joke"""
    def test_check_created_at(self):
        response = requests.get(URL)
        data = response.json()
        print(data['created_at'])
        self.assertTrue('created_at')

    """ Check icon url"""
    def test_check_icon_url(self):
        response = requests.get(URL)
        data = response.json()
        print(data["icon_url"])
        self.assertTrue("icon_url")

    """Update time is in joke"""
    def test_check_updated_time(self):
        response = requests.get(URL)
        data = response.json()
        print(data["updated_at"])
        self.assertTrue("updated_at")

    """Find name in joke"""
    def test_find_name(self):
        response = requests.get(URL)
        data = response.json()
        joke_text = data["value"]
        name = "Chuck" in joke_text
        self.assertTrue(all(name for joke_text in data))
        print(name)

    """Find last name in joke"""
    def test_find_last_name(self):
        response = requests.get(URL)
        data = response.json()
        joke_text = data["value"]
        last_name = "Norris" in joke_text
        self.assertTrue(all(last_name for joke_text in data))
        print(last_name)

    """No to find word "gun" in joke"""
    def test_find_word_gun(self):
        response = requests.get(URL)
        data = response.json()
        joke_text = data["value"]
        word = "gan" in joke_text
        self.assertFalse(all(word for joke_text in data))
        print(word)

    """No to Find word "minsk" in joke"""
    def test_find_word_minsk(self):
        response = requests.get(URL)
        data = response.json()
        joke_text = data["value"]
        word = "minsk" in joke_text
        self.assertFalse(all(word for joke_text in data))
        print(word)


if __name__ == '__main__':
    unittest.main()
    
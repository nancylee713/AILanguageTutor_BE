from copy import deepcopy
import unittest
import json

import app


BASE_URL = 'http://127.0.0.1:5000'
USERS_URL = '{}/users'.format(BASE_URL)
USER_PROFILE_URL = '{}/users_profile'.format(BASE_URL)
CREATE_USER_PROFILE_URL = '{}/create_user_profile'.format(BASE_URL)
SIGNUP_URL = '{}/signup'.format(BASE_URL)
LOGIN_URL = '{}/login'.format(BASE_URL)
SPEECH_QUESTIONS_URL = '{}/speech_questions'.format(BASE_URL)
GRAMMAR_QUESTIONS_URL = '{}/grammar_questions'.format(BASE_URL)
USERS_SPEECH_URL = '{}/users_speech'.format(BASE_URL)
USERS_GRAMMAR_URL = '{}/users_grammar'.format(BASE_URL)


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        # self.backup_items = deepcopy(app.users)
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_all_users(self):
        response = self.app.get(USERS_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 6)


    def test_get_one_user(self):
        response = self.app.get(USERS_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data[0]['email'], 'test@email.com')

    def test_get_all_users_profile(self):
        response = self.app.get(USER_PROFILE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 3)

    def test_get_one_user_profile(self):
        response = self.app.get(USER_PROFILE_URL)
        data = json.loads(response.get_data())
        keys = ['age', 'created_date', 'id', 'name', 'proficiency', 'updated_date', 'user_id']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(data[0]), keys)

    def test_post_user_already_exists(self):
        # duplicate attribute = bad
        user = {"email": "test@email.com", "password": "password"}
        response = self.app.post(SIGNUP_URL,
                                 data=json.dumps(user),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 409)

    def test_post_new_user(self):
        user = {"email": "test100@email.com", "password": "password"}
        response = self.app.post(SIGNUP_URL,
                                 data=json.dumps(user),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 222)

    # need to include test for missing value field

    # def test_get_new_user_profile(self):
    #     user = {"email": "test35@email.com", "password": "password"}
    #     response = self.app.get(SIGNUP_URL,
    #                              data=json.dumps(user),
    #                              content_type='application/json')
    #     self.assertEqual(response.status_code, 222)

    def test_get_all_speech_questions(self):
        response = self.app.get(SPEECH_QUESTIONS_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 15)

    def test_get_all_grammar_questions(self):
        response = self.app.get(GRAMMAR_QUESTIONS_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 15)

if __name__ == "__main__":
    unittest.main()

from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient
import json

from api.models import SimpleReadWrite

class  SimpleReadWriteTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient(enforce_csrf_checks=True)

    def testSimpleReadWriteViewSet(self):
        # 登録
        obj = {'name': 'aaa'}
        response1 = self.client.post('/api/simplereadwrite/', obj)
        self.assertEqual(response1.status_code, 201)

        created_user = json.loads(str(response1.content.decode('ascii')))
        self.assertEqual(obj['name'], created_user['name'])

        # 取得
        response2 = self.client.get('/api/simplereadwrite/%d/' % created_user['id'])
        self.assertEqual(response2.status_code, 200)

        stored_user = json.loads(str(response2.content.decode('ascii')))
        self.assertEqual(stored_user['name'], created_user['name'])

        # 更新
        update = {'name': 'zzz'}
        response3 = self.client.put('/api/simplereadwrite/%d/' % created_user['id'], update)
        self.assertEqual(response3.status_code, 200)

        updated_user = json.loads(str(response3.content.decode('ascii')))
        self.assertEqual(update['name'], updated_user['name'])

        # 取得
        response4 = self.client.get('/api/simplereadwrite/%d/' % updated_user['id'])
        self.assertEqual(response4.status_code, 200)

        stored_user = json.loads(str(response4.content.decode('ascii')))
        self.assertEqual(stored_user['name'], updated_user['name'])

        # 削除
        response5 = self.client.delete('/api/simplereadwrite/%d/' % created_user['id'])
        self.assertEqual(response5.status_code, 204)

        # 取得
        response6 = self.client.get('/api/simplereadwrite/%d/' % created_user['id'])
        self.assertEqual(response6.status_code, 404)




# basic authentication

@pytest.skip
def test_basic_auth():
    access_token = 'dkldfjgjfhg'
    headers = {'Authorization': f'Bearer {access_token}'}
    'Content-type': 'application/json'}
    response = 'requests.get('https://api.example.com/protected',
                            headers = headers)
    assert response.status_code == 200

   # 1. обрати сайт для тестів
  #  2. написати 10 тестів
   # 3.Зробити пакунок хелпер з методами і функціями
# як то все працює. короткі, лаконічні тести
# покриває потребу щоб зрозуміло було що і де
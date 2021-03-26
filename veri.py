from firebase import firebase


firebase = firebase.FirebaseApplication('https://saas-31543.firebaseio.com/', None)
data =  { 'name': 'John Doe',
          'plaka': '09YES26',
          }
result = firebase.post('/saas-3154/Kullanıcılar',data)
print(result)
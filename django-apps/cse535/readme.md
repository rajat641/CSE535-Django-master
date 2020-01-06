endpoints:

/preferences/pref_save/ : To save the preference of each user in preferences table
curl -X POST \
  http://127.0.0.1:8000/preferences/pref_save/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F userid=2 \
  -F topic1=8 \
  -F 'topic2=3 ' \
  -F topic3=5 \
  -F topic4=6 \
  -F topic5=7



/authen/login/ : To authenticate the given use and send his details
curl -X POST \
  http://127.0.0.1:8000/authen/login/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F username=user3@gmail.com \
  -F password=user3password

/authen/signup/ : To store the user details in appuser table
  curl -X POST \
    http://127.0.0.1:8000/authen/signup/ \
    -H ': ' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -H 'cache-control: no-cache' \
    -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
    -F email=user4@gmail.com \
    -F password=user4password \
    -F first_name=user4 \
    -F mobile=3838383749


/authen/group_save/ : To create and save the groups in the database (with dummy data for now)
    curl -X GET \
      http://127.0.0.1:8000/authen/group_save/ \
      -H 'cache-control: no-cache' \
      -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
      -F username=user3@gmail.com \
      -F password=user3password

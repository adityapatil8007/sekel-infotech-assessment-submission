responce = requests.get("https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC")
 assert response.status_code == 200
 response_json = response.json()
expected_keys = ["username", "role", "status"]
for user in response_json['data']:
    for key in expected_keys:
        assert key in user,
expected_user_details = {
    "username": "Aditya",
    "role": "Admin",
    "status": "Active"
},
for user in response_json['data']:
    if user['username'] == expected_user_details['username']:
        assert user['role'] == expected_user_details['role'], 
        assert user['status'] == expected_user_details['status'],
print("API response validated successfully.")

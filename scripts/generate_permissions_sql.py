template = (
    "INSERT INTO user_company_privileges (user_id,company_id) VALUES ('{}','{}');"
)
for i in range(67):

    print(template.format(1, i))

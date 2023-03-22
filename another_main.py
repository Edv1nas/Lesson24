from dotenv import dotenv_values

# config = {'DOMAIN': 'example.org', 'ADMIN_EMAIL': 'admin@example.org', 'ROOT_URL': 'example.org/app'}
config = dotenv_values(".env")

print(type(config))

print(config["DOMAIN"])
print(config["ADMIN_EMAIL"])

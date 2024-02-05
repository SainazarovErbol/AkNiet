
def upload_avatar_for_user(instance, filename):
    return f'/avatar/{instance.username}/{filename}'


def upload_products(instance, filename):
    return f'/products/{instance.product}/{filename}'

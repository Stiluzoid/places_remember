def get_avatar(backend, response, user=None, *args, **kwargs):
    url = None
    if backend.name == 'vk-oauth2':
        url = response.get('photo', '')

        print(url)

    if url:
        user.profile.avatar = url
        user.profile.save()
        print(user.profile.avatar)

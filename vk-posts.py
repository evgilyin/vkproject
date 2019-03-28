import vk_api
import passwords


def get_id():
	login, password = passwords.login, passwords.password
	vk_session = vk_api.VkApi(login, password)
	try:
		vk_session.auth(token_only=True)
	except vk_api.AuthError as error_msg:
		print(error_msg)
		return

	group_link = str(input('Введите ссылку на сообщество в формате https://vk.com/...: '))
	vk = vk_session.get_api()

	while True:
		if 'https://vk.com/' in group_link:
			if 'public' in group_link:
				group_data = -int(group_link[21:])
			elif 'club' in group_link:
				group_data = -int(group_link[19:])
			else:
				group_data = vk.groups.getById(group_id=group_link[15:])
				for elements in group_data:
					group_data = -int(elements.get("id"))
			return group_data
			continue
		else:
			group_link = str(input('Некорректный ввод. Пожалуйста, введите ссылку на сообщество в следующем формате: https://vk.com/...: '))


def main():
	login, password = passwords.login, passwords.password
	vk_session = vk_api.VkApi(login, password)
	try:
		vk_session.auth(token_only=True)
	except vk_api.AuthError as error_msg:
		print(error_msg)
		return

	tools = vk_api.VkTools(vk_session)
	
	all_posts=[]
	
	posts = tools.get_all('wall.get', 100, {'owner_id': get_id(), 'filter': 'owner'})
	for elements in posts["items"]:
		all_posts.append(elements.get("text"))
	print('\n\n'.join(all_posts))


if __name__ == "__main__":
	main()


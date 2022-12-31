import file_dumps


def get_followers_info(cl, users_names):
	for user in users_names:
		user_id = cl.user_id_from_username(user)
		print(user_id)
		users_following = cl.user_followers_v1(user_id)
		# users_following = cl.user_followers(user_id).keys()
		file_dumps.write_info_to_file(list(users_following))

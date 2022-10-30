import malclient

client = malclient.Client.generate_new_token('48563b906310d3fdb4cefa1c1877bfc3', '7d1c1c9dff161b5bf61dbbb1cc8ceed03d7988db888fc702ef8b9a6ebff7de7e')
print(client.get_anime_ranking())
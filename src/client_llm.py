from langserve import RemoteRunnable

chain_remote = RemoteRunnable("http://localhost:8000/tradutor")
text = chain_remote.invoke({"idiom": "espanhol", "text": "ja deu like no video???"})
print(text)
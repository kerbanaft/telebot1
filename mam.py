import ctypes
import requests
import getpass

p = getpass.getuser()

req = requests.get("https://preview.redd.it/xj93s759hqx41.jpg?auto=webp&s=efad21047027a8cdf44d5e671755bb6d8e6e80bb",allow_redirects=True)
open(f'C:/Users/{p}/lol.jpg','wb').write(req.content)
ctypes.windll.user32.SystemParametersInfoW(20, 0, f"C:/Users/{p}/lol.jpg", 0)

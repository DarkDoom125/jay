import pandas as pd

data = {"Name": ["Jay", "Arya", "Nick", "Daniel", "Guru", "Reeshan", "Anirudh"],
"fav_color": ["Blue", "green", "Black", "brown", "red", "blue ", "orange"],
"Age": [13, 12, 13, 12, 10, 9, 9,]}
df = pd.DataFrame(data)
print(df)

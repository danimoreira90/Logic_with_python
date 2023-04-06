import pandas as pd

df = {'email': ['p@gmail.com;m@gmail.com;i@gmail.com',
                'a@gmail.com,b@gmail.com',
                'c@gmail.com',
                '']}

df = pd.DataFrame(df)

print(df)
print()

df = (df['email'].str.split('[,;]', expand=True)
      .fillna('')
      .rename(columns={i: col for i,col in enumerate(['email_1', 'email_2', 'email_3'])}))

print(df)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

sns.set()

buku = {
    "Diameter": [50, 26.5, 30, 20, 40],
    "Jumlah_Buku": [36, 24, 28, 18, 34],
    "Harga": [18.000, 6.360, 8.400, 3.600, 13.600],
}

df = pd.DataFrame(buku).sort_values(by=["Diameter", "Jumlah_Buku", "Harga"])

x_train = np.array(df[["Diameter", "Jumlah_Buku"]])
y_train = np.array(df["Harga"])

model = LinearRegression()
model.fit(x_train, y_train)

# lebar = int(input("tentukan lebar: "))
# tinggi = int(input("tentukan tinggi: "))
# ukuran = lebar * tinggi
# lembaran = int(input("mau berapa lembar: "))

# X_test = np.array([[ukuran, lembaran]])
# y_pred = model.predict(X_test)

# for test, pred in zip(X_test, y_pred):
#     if y_pred >= float(1.0):
#         print(
#             f"Prediksi Harga NoteBook dengan ukuran {test[0]} Cm dan Dengan isi lembar {test[1]} Lembar dengan harga {int(pred)} Ribu Rupiah"
#         )
#     else:
#         print(
#             f"Prediksi Harga NoteBook dengan ukuran {test[0]} Cm dan Dengan isi lembar {test[1]} Lembar dengan harga {pred} Rupiah"
#         )

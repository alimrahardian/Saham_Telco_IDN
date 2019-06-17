import pandas as pd
import matplotlib.pyplot as plt

xl = pd.read_csv('EXCL.JK.csv', parse_dates=['Date'])
fren = pd.read_csv('FREN.JK.csv', parse_dates=['Date'])
indosat = pd.read_csv('ISAT.JK.csv', parse_dates=['Date'])
telkom = pd.read_csv('TLKM.JK.csv', parse_dates=['Date'])

date = xl['Date']
close_xl = xl['Close']
close_fren = fren['Close']
close_indosat = indosat['Close']
close_telkom = telkom['Close']

date_april = xl.loc[(xl['Date'].dt.month==4)]['Date']
close_april_xl = xl.loc[(xl['Date'].dt.month==4)]['Close']
close_april_fren = fren.loc[(fren['Date'].dt.month==4)]['Close']
close_april_indosat = indosat.loc[(indosat['Date'].dt.month==4)]['Close']
close_april_telkom = telkom.loc[(telkom['Date'].dt.month==4)]['Close']

plt.subplot(2, 1, 1)
plt.plot(date, close_xl, color='green', label='PT XL Axiata Tbk')
plt.plot(date, close_fren, color='cyan', label='PT Smartfren Telecom Tbk')
plt.plot(date, close_indosat, color='blue', label='PT Indosat Tbk')
plt.plot(date, close_telkom, color='red', label='PT Telekomunikasi Indonesia Tbk')

plt.title('Harga Saham Historis Provider Telco Indonesia')
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.xticks(rotation=45)
plt.legend(loc='center')

plt.subplot(2, 1, 2)
plt.plot(date_april, close_april_xl, color='green', label='PT XL Axiata Tbk')
plt.plot(date_april, close_april_fren, color='cyan', label='PT Smartfren Telecom Tbk')
plt.plot(date_april, close_april_indosat, color='blue', label='PT Indosat Tbk')
plt.plot(date_april, close_april_telkom, color='red', label='PT Telekomunikasi Indonesia Tbk')

plt.title('Harga Saham Historis Provider Telco Indonesia (April 2019)')
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.xticks(rotation=15)
plt.legend(loc='center')

plt.show()
# print(xl.dtypes)
# print(date_april.shape)
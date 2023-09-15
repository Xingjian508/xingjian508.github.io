import requests
import json


APP_ID = '65296dcc4e414151832e3b66ea08b2d4'


def simulated_data():
  """Returns the simulated sample data."""
  data =\
      '{"disclaimer": "Usage subject to terms: https://openexchangerates.org/terms", "license": "https://openexchangerates.org/license", "timestamp": 1694685600, "base": "USD", "rates": {"AED": 3.673025, "AFN": 78.860389, "ALL": 99.065196, "AMD": 385.173937, "ANG": 1.801778, "AOA": 828.5, "ARS": 349.9685, "AUD": 1.555418, "AWG": 1.8, "AZN": 1.7, "BAM": 1.820975, "BBD": 2, "BDT": 109.714537, "BGN": 1.8231, "BHD": 0.377015, "BIF": 2831.73774, "BMD": 1, "BND": 1.361402, "BOB": 6.908495, "BRL": 4.9164, "BSD": 1, "BTC": 3.8049962e-05, "BTN": 82.930677, "BWP": 13.629846, "BYN": 2.523463, "BZD": 2.015176, "CAD": 1.353147, "CDF": 2481.238425, "CHF": 0.893238, "CLF": 0.032153, "CLP": 887.19, "CNH": 7.283049, "CNY": 7.277, "COP": 3991.046347, "CRC": 534.798313, "CUC": 1, "CUP": 25.75, "CVE": 102.661839, "CZK": 22.790878, "DJF": 177.997511, "DKK": 6.95339, "DOP": 56.757134, "DZD": 137.256821, "EGP": 30.8998, "ERN": 15, "ETB": 55.13486, "EUR": 0.932111, "FJD": 2.2661, "FKP": 0.801667, "GBP": 0.801667, "GEL": 2.62, "GGP": 0.801667, "GHS": 11.446501, "GIP": 0.801667, "GMD": 60.5, "GNF": 8582.605911, "GTQ": 7.869207, "GYD": 209.321775, "HKD": 7.8269, "HNL": 24.629206, "HRK": 7.023445, "HTG": 135.459227, "HUF": 358.298468, "IDR": 15356.393571, "ILS": 3.825585, "IMP": 0.801667, "INR": 83.014495, "IQD": 1309.238574, "IRR": 42252.5, "ISK": 135.62, "JEP": 0.801667, "JMD": 154.424839, "JOD": 0.7082, "JPY": 147.38, "KES": 146.6, "KGS": 88.39, "KHR": 4111.581612, "KMF": 458.949862, "KPW": 900, "KRW": 1326.493743, "KWD": 0.308772, "KYD": 0.833101, "KZT": 465.979446, "LAK": 19848.594947, "LBP": 15025.618002, "LKR": 323.41773, "LRD": 186.450039, "LSL": 18.926482, "LYD": 4.848891, "MAD": 10.160795, "MDL": 17.959854, "MGA": 4512.838499, "MKD": 57.348852, "MMK": 2099.449609, "MNT": 3450, "MOP": 8.05644, "MRU": 37.95, "MUR": 44.797614, "MVR": 15.38, "MWK": 1098.749687, "MXN": 17.14791, "MYR": 4.682, "MZN": 63.875002, "NAD": 18.91, "NGN": 770.5, "NIO": 36.581506, "NOK": 10.716325, "NPR": 132.689373, "NZD": 1.689517, "OMR": 0.384993, "PAB": 1, "PEN": 3.698956, "PGK": 3.673014, "PHP": 56.711506, "PKR": 295.170388, "PLN": 4.310404, "PYG": 7275.270501, "QAR": 3.641, "RON": 4.6323, "RSD": 109.31963, "RUB": 96.095, "RWF": 1204.695365, "SAR": 3.750915, "SBD": 8.418851, "SCR": 12.926619, "SDG": 601.5, "SEK": 11.130112, "SGD": 1.361065, "SHP": 0.801667, "SLL": 20969.5, "SOS": 571.296485, "SRD": 38.198, "SSP": 130.26, "STD": 22281.8, "STN": 22.810856, "SVC": 8.747184, "SYP": 2512.53, "SZL": 18.932256, "THB": 35.793, "TJS": 10.981942, "TMT": 3.51, "TND": 3.13125, "TOP": 2.39283, "TRY": 26.948068, "TTD": 6.786399, "TWD": 31.921499, "TZS": 2505, "UAH": 36.921529, "UGX": 3721.466932, "USD": 1, "UYU": 38.26202, "UZS": 12158.340173, "VES": 33.295446, "VND": 24233.615222, "VUV": 118.722, "WST": 2.7185, "XAF": 611.424664, "XAG": 0.04432919, "XAU": 0.00052455, "XCD": 2.70255, "XDR": 0.756583, "XOF": 611.424664, "XPD": 0.00079632, "XPF": 111.230417, "XPT": 0.00110823, "YER": 250.324945, "ZAR": 18.903414, "ZMW": 21.028817, "ZWL": 322}}'
  return data


def get_forex_data(app_id, base):
  """Returns the API-obtained forex data."""
  url = f"https://openexchangerates.org/api/latest.json?app_id={app_id}&base={base}"
  response = requests.get(url)
  data = response.json()
  return data


def convert_to_rates(data):
  """Converts raw data to a rates dictionary."""
  return data['rates']


def get_base_rates(base):
  """Function to get real time rates."""
  forex_data = get_forex_data(APP_ID, base)
  return convert_to_rates(forex_data)


def get_rates_single(currencies):
  """Get real time rates from USD."""
  rates = dict()
  rates['USD'] = get_base_rates('USD')
  
  selected_rates = dict()
  for from_currency in currencies:
    selected_rates[from_currency] = dict()
    for to_currency in currencies:
      if from_currency != to_currency:
        if from_currency == 'USD':
          selected_rates[from_currency][to_currency] = rates[from_currency][to_currency]
        elif to_currency == 'USD':
          selected_rates[from_currency][to_currency] = 1/rates[to_currency][from_currency]
        else:
          selected_rates[from_currency][to_currency] = rates['USD'][to_currency] / rates['USD'][from_currency]
  return selected_rates



def get_rates_simul(currencies):
  """Get simulated rates."""
  data = json.loads(simulated_data())['rates']
  rates = dict()
  for base in currencies:
    if base != 'USD':
      if 'USD' not in rates:
        rates['USD'] = dict()
      rates['USD'][base] = data[base]
  
  selected_rates = dict()
  for from_currency in currencies:
    selected_rates[from_currency] = dict()
    for to_currency in currencies:
      if from_currency != to_currency:
        if from_currency == 'USD':
          selected_rates[from_currency][to_currency] = rates[from_currency][to_currency]
        elif to_currency == 'USD':
          selected_rates[from_currency][to_currency] = 1/rates[to_currency][from_currency]
        else:
          selected_rates[from_currency][to_currency] = rates['USD'][to_currency] / rates['USD'][from_currency]
  return selected_rates


def get_rates(currencies):
  """Returns a nested dictionary of exchange rates for specific currencies."""
  rates = dict()
  for base in currencies:
    rates[base] = get_base_rates(base)

  selected_rates = dict()
  for from_currency in currencies:
    selected_rates[from_currency] = dict()
    for to_currency in currencies:
      if from_currency != to_currency:
        selected_rates[from_currency][to_currency] = rates[from_currency][to_currency]
  return selected_rates


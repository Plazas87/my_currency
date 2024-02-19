from datetime import datetime
import time

import pandas as pd

# Define start and end dates
start_date = "2024-02-10"
end_date = "2024-02-17"

# Create a date range using pandas
date_range = pd.date_range(start=start_date, end=end_date, freq="D")

date_strings = [date.strftime("%Y-%m-%d") for date in date_range]

# Print the list of date strings
print(date_strings)

print(datetime.strptime(start_date, "%Y-%m-%d"))


{"source_currency": "EUR", "date_from": "2024-02-15", "date_to": "2024-02-15"}
{"source_currency": "EUR", "date_from": "2024-02-14", "date_to": "2024-02-14"}


{
    "success": True,
    "timestamp": 1707609599,
    "historical": True,
    "base": "EUR",
    "date": "2024-02-10",
    "rates": {
        "AED": 3.96107,
        "AFN": 79.472647,
        "ALL": 104.079659,
        "AMD": 437.424649,
        "ANG": 1.941853,
        "AOA": 896.198428,
        "ARS": 895.059457,
        "AUD": 1.65279,
        "AWG": 1.943919,
        "AZN": 1.837659,
        "BAM": 1.956357,
        "BBD": 2.17552,
        "BDT": 118.253698,
        "BGN": 1.956357,
        "BHD": 0.406116,
        "BIF": 3075.576421,
        "BMD": 1.078457,
        "BND": 1.450313,
        "BOB": 7.445122,
        "BRL": 5.378833,
        "BSD": 1.077407,
        "BTC": 2.2608837e-05,
        "BTN": 89.443888,
        "BWP": 14.790215,
        "BYN": 3.525505,
        "BYR": 21137.763448,
        "BZD": 2.171819,
        "CAD": 1.454678,
        "CDF": 2958.208816,
        "CHF": 0.943618,
        "CLF": 0.037896,
        "CLP": 1045.667975,
        "CNY": 7.74375,
        "COP": 4247.910491,
        "CRC": 556.758655,
        "CUC": 1.078457,
        "CUP": 28.579119,
        "CVE": 110.29643,
        "CZK": 25.241837,
        "DJF": 191.844668,
        "DKK": 7.454949,
        "DOP": 63.218015,
        "DZD": 144.877843,
        "EGP": 33.293387,
        "ERN": 16.17686,
        "ETB": 61.031992,
        "EUR": 1,
        "FJD": 2.418711,
        "FKP": 0.85414,
        "GBP": 0.853953,
        "GEL": 2.858333,
        "GGP": 0.85414,
        "GHS": 13.36881,
        "GIP": 0.85414,
        "GMD": 73.015716,
        "GNF": 9264.640065,
        "GTQ": 8.415398,
        "GYD": 225.594286,
        "HKD": 8.433698,
        "HNL": 26.586576,
        "HRK": 7.420132,
        "HTG": 141.870428,
        "HUF": 386.972473,
        "IDR": 16836.282509,
        "ILS": 3.95906,
        "IMP": 0.85414,
        "INR": 89.527865,
        "IQD": 1411.502224,
        "IRR": 45327.561488,
        "ISK": 148.342221,
        "JEP": 0.85414,
        "JMD": 168.61805,
        "JOD": 0.764738,
        "JPY": 161.040682,
        "KES": 175.089894,
        "KGS": 96.446853,
        "KHR": 4395.252478,
        "KMF": 492.31986,
        "KPW": 970.625892,
        "KRW": 1436.003708,
        "KWD": 0.332079,
        "KYD": 0.897856,
        "KZT": 481.297151,
        "LAK": 22442.395218,
        "LBP": 16194.214727,
        "LKR": 337.256105,
        "LRD": 205.342344,
        "LSL": 20.523454,
        "LTL": 3.184405,
        "LVL": 0.652348,
        "LYD": 5.210485,
        "MAD": 10.803579,
        "MDL": 19.211475,
        "MGA": 4888.393004,
        "MKD": 61.637564,
        "MMK": 2262.644767,
        "MNT": 3692.746441,
        "MOP": 8.677873,
        "MRU": 42.685749,
        "MUR": 49.069683,
        "MVR": 16.612277,
        "MWK": 1813.716839,
        "MXN": 18.427642,
        "MYR": 5.138891,
        "MZN": 68.486064,
        "NAD": 20.52345,
        "NGN": 1590.315138,
        "NIO": 39.651299,
        "NOK": 11.456765,
        "NPR": 143.109781,
        "NZD": 1.742398,
        "OMR": 0.415163,
        "PAB": 1.077607,
        "PEN": 4.151983,
        "PGK": 4.097168,
        "PHP": 60.280413,
        "PKR": 298.186372,
        "PLN": 4.32566,
        "PYG": 7851.2373,
        "QAR": 3.926394,
        "RON": 4.976222,
        "RSD": 117.204399,
        "RUB": 98.554863,
        "RWF": 1369.790337,
        "SAR": 4.044334,
        "SBD": 9.117758,
        "SCR": 14.217251,
        "SDG": 648.153215,
        "SEK": 11.353988,
        "SGD": 1.451658,
        "SHP": 1.362133,
        "SLE": 24.316266,
        "SLL": 21299.532411,
        "SOS": 616.34231,
        "SRD": 39.363157,
        "STD": 22321.889102,
        "SYP": 14021.933506,
        "SZL": 20.482837,
        "THB": 38.727801,
        "TJS": 11.79276,
        "TMT": 3.785385,
        "TND": 3.372879,
        "TOP": 2.557566,
        "TRY": 33.080712,
        "TTD": 7.312084,
        "TWD": 33.845015,
        "TZS": 2720.575259,
        "UAH": 40.570261,
        "UGX": 4156.184352,
        "USD": 1.078457,
        "UYU": 42.122003,
        "UZS": 13301.790498,
        "VEF": 3903171.91348,
        "VES": 39.031776,
        "VND": 26341.320011,
        "VUV": 130.371435,
        "WST": 2.975033,
        "XAF": 656.143976,
        "XAG": 0.047688,
        "XAU": 0.000533,
        "XCD": 2.914585,
        "XDR": 0.80843,
        "XOF": 656.143976,
        "XPF": 119.331742,
        "YER": 270.018791,
        "ZAR": 20.470932,
        "ZMK": 9707.41389,
        "ZMW": 29.010267,
        "ZWL": 347.262817,
    },
}



{
    "status_code": 200,
    "headers": {},
    "body": {
        "rates": [
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "AED",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 3.96107
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "AFN",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 79.472647
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ALL",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 104.079659
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "AMD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 437.424649
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ANG",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.941853
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "AOA",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 896.198428
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ARS",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 895.059457
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "AUD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.65279
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "AWG",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.943919
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "AZN",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.837659
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BAM",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.956357
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BBD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 2.17552
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BDT",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 118.253698
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BGN",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.956357
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BHD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.406116
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BIF",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 3075.576421
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BMD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.078457
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BND",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.450313
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BOB",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 7.445122
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BRL",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 5.378833
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BSD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.077407
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BTC",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 2.2608837e-05
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BTN",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 89.443888
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BWP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 14.790215
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BYN",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 3.525505
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BYR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 21137.763448
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BZD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 2.171819
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CAD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.454678
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CDF",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 2958.208816
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CHF",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.943618
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CLF",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.037896
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CLP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1045.667975
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CNY",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 7.74375
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "COP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 4247.910491
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CRC",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 556.758655
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CUC",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.078457
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CUP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 28.579119
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CVE",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 110.29643
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CZK",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 25.241837
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "DJF",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 191.844668
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "DKK",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 7.454949
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "DOP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 63.218015
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "DZD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 144.877843
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "EGP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 33.293387
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ERN",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 16.17686
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ETB",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 61.031992
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "EUR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "FJD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 2.418711
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "FKP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.85414
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GBP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.853953
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GEL",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 2.858333
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GGP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.85414
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GHS",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 13.36881
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GIP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.85414
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GMD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 73.015716
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GNF",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 9264.640065
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GTQ",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 8.415398
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GYD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 225.594286
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "HKD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 8.433698
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "HNL",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 26.586576
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "HRK",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 7.420132
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "HTG",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 141.870428
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "HUF",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 386.972473
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "IDR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 16836.282509
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ILS",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 3.95906
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "IMP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.85414
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "INR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 89.527865
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "IQD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1411.502224
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "IRR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 45327.561488
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ISK",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 148.342221
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "JEP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.85414
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "JMD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 168.61805
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "JOD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.764738
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "JPY",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 161.040682
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KES",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 175.089894
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KGS",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 96.446853
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KHR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 4395.252478
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KMF",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 492.31986
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KPW",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 970.625892
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KRW",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1436.003708
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KWD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.332079
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KYD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.897856
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KZT",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 481.297151
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LAK",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 22442.395218
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LBP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 16194.214727
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LKR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 337.256105
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LRD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 205.342344
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LSL",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 20.523454
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LTL",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 3.184405
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LVL",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.652348
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LYD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 5.210485
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MAD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 10.803579
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MDL",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 19.211475
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MGA",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 4888.393004
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MKD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 61.637564
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MMK",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 2262.644767
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MNT",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 3692.746441
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MOP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 8.677873
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MRU",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 42.685749
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MUR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 49.069683
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MVR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 16.612277
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MWK",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1813.716839
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MXN",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 18.427642
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MYR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 5.138891
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MZN",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 68.486064
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "NAD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 20.52345
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "NGN",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1590.315138
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "NIO",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 39.651299
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "NOK",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 11.456765
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "NPR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 143.109781
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "NZD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.742398
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "OMR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.415163
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "PAB",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.077607
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "PEN",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 4.151983
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "PGK",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 4.097168
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "PHP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 60.280413
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "PKR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 298.186372
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "PLN",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 4.32566
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "PYG",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 7851.2373
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "QAR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 3.926394
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "RON",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 4.976222
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "RSD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 117.204399
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "RUB",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 98.554863
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "RWF",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1369.790337
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SAR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 4.044334
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SBD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 9.117758
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SCR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 14.217251
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SDG",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 648.153215
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SEK",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 11.353988
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SGD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.451658
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SHP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.362133
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SLE",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 24.316266
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SLL",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 21299.532411
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SOS",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 616.34231
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SRD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 39.363157
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "STD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 22321.889102
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SYP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 14021.933506
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SZL",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 20.482837
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "THB",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 38.727801
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TJS",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 11.79276
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TMT",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 3.785385
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TND",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 3.372879
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TOP",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 2.557566
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TRY",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 33.080712
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TTD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 7.312084
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TWD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 33.845015
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TZS",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 2720.575259
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "UAH",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 40.570261
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "UGX",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 4156.184352
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "USD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 1.078457
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "UYU",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 42.122003
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "UZS",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 13301.790498
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "VEF",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 3903171.91348
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "VES",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 39.031776
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "VND",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 26341.320011
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "VUV",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 130.371435
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "WST",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 2.975033
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "XAF",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 656.143976
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "XAG",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.047688
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "XAU",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.000533
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "XCD",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 2.914585
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "XDR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 0.80843
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "XOF",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 656.143976
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "XPF",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 119.331742
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "YER",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 270.018791
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ZAR",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 20.470932
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ZMK",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 9707.41389
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ZMW",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 29.010267
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ZWL",
                "valuation_date": "2024-02-10T00:00:00",
                "rate_value": 347.262817
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "AED",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 3.965527
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "AFN",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 79.632713
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ALL",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 104.208386
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "AMD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 437.965661
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ANG",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.944255
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "AOA",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 897.306164
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ARS",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 894.768079
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "AUD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.654953
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "AWG",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.946324
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "AZN",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.860485
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BAM",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.958777
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BBD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 2.178211
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BDT",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 118.399955
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BGN",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.95981
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BHD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.406618
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BIF",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 3079.380332
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BMD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.079791
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BND",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.452107
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BOB",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 7.45433
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BRL",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 5.349931
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BSD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.07874
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BTC",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 2.2405573e-05
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BTN",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 89.554513
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BWP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 14.808507
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BYN",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 3.529865
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BYR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 21163.9069
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "BZD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 2.174505
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CAD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.453221
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CDF",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 2961.867456
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CHF",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.943975
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CLF",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.037943
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CLP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1046.96127
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CNY",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 7.752777
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "COP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 4253.16436
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CRC",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 557.447261
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CUC",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.079791
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CUP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 28.614466
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CVE",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 110.432846
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "CZK",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 25.237904
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "DJF",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 192.081944
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "DKK",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 7.455223
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "DOP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 63.296204
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "DZD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 145.057013
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "EGP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 33.282549
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ERN",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 16.196868
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ETB",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 61.107477
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "EUR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "FJD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 2.421702
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "FKP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.855094
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GBP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.854498
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GEL",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 2.861072
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GGP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.855094
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GHS",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 13.385344
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GIP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.855094
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GMD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 73.106793
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GNF",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 9276.098689
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GTQ",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 8.425806
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "GYD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 225.873304
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "HKD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 8.444091
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "HNL",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 26.619459
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "HRK",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 7.429309
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "HTG",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 142.045895
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "HUF",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 387.483599
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "IDR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 16857.105836
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ILS",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 3.961431
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "IMP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.855094
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "INR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 89.638594
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "IQD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1413.247987
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "IRR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 45383.622754
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ISK",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 148.525215
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "JEP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.855094
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "JMD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 168.826599
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "JOD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.765681
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "JPY",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 161.075692
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KES",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 175.306447
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KGS",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 96.565641
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KHR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 4400.688581
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KMF",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 492.923025
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KPW",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 971.762832
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KRW",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1437.779748
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KWD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.332489
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KYD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.898966
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "KZT",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 481.892426
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LAK",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 22470.152255
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LBP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 16214.243936
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LKR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 337.673228
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LRD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 205.583654
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LSL",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 20.548064
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LTL",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 3.188342
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LVL",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.653155
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "LYD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 5.216929
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MAD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 10.816941
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MDL",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 19.235236
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MGA",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 4894.43903
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MKD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 61.713798
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MMK",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 2265.443234
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MNT",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 3670.584653
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MOP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 8.688606
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MRU",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 42.737742
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MUR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 49.130373
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MVR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 16.623366
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MWK",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1815.960067
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MXN",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 18.441645
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MYR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 5.145214
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "MZN",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 68.564247
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "NAD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 20.548122
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "NGN",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1592.281898
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "NIO",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 39.70034
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "NOK",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 11.382035
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "NPR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 143.286781
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "NZD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.756566
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "OMR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.415676
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "PAB",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.07894
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "PEN",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 4.157118
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "PGK",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 4.102235
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "PHP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 60.354938
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "PKR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 298.555172
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "PLN",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 4.32639
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "PYG",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 7860.947809
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "QAR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 3.93125
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "RON",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 4.982432
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "RSD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 117.349359
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "RUB",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 98.676715
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "RWF",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1371.484511
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SAR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 4.04948
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SBD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 9.129035
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SCR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 14.234835
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SDG",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 648.954693
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SEK",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 11.281518
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SGD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.452605
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SHP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.363781
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SLE",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 24.613079
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SLL",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 21325.875329
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SOS",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 617.099192
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SRD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 39.411841
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "STD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 22349.497096
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SYP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 14038.707808
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "SZL",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 20.50817
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "THB",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 38.753165
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TJS",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 11.807346
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TMT",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 3.790067
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TND",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 3.377044
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TOP",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 2.560727
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TRY",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 33.132841
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TTD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 7.321127
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TWD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 33.886867
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "TZS",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 2723.940101
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "UAH",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 40.620439
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "UGX",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 4161.324774
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "USD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 1.079791
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "UYU",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 42.1741
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "UZS",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 13318.24232
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "VEF",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 3903801.497722
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "VES",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 39.080051
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "VND",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 26373.899288
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "VUV",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 129.514726
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "WST",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 2.968014
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "XAF",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 656.955503
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "XAG",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.047651
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "XAU",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.000533
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "XCD",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 2.91819
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "XDR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 0.80943
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "XOF",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 656.955503
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "XPF",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 119.331742
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "YER",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 270.352689
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ZAR",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 20.52278
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ZMK",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 9719.422191
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ZMW",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 29.046147
            },
            {
                "success": true,
                "error_message": null,
                "provider_name": null,
                "source_currency": "EUR",
                "exchange_currency": "ZWL",
                "valuation_date": "2024-02-11T00:00:00",
                "rate_value": 347.692316
            }
        ]
    }
}

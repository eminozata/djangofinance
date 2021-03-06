from binance.client import Client
import time


api_key = "SHVyAf6sIQMYOSnBXiuD0jfHfNBmfQv2epL8HlT5uu78cevYokrtPIKoYKL85y44"
api_secret = "7NqFrVDlmzo6R4TuuKEfI14NuiotWaqR9OGUqXuOpKXBPAlivYhh0ptTAk0q0gSf"
client = Client(api_key, api_secret)

ana_para = 4450
odenecek_tutar = 5561.86



def kredi_cuzdan():

    krediden_alinan_btc = 0.00283
    krediden_alinan_eth = 0.0082 + 0.0267
    krediden_alinan_tl = 8 


    btc_try_price = float(client.get_symbol_ticker(symbol=f"BTCTRY")['price'])
    btc_usd_price = float(client.get_symbol_ticker(symbol=f"BTCUSDT")['price'])
    eth_try_price = float(client.get_symbol_ticker(symbol=f"ETHTRY")['price'])
    eth_usd_price = float(client.get_symbol_ticker(symbol=f"ETHUSDT")['price'])
    try_usd_price = float(client.get_symbol_ticker(symbol=f"USDTTRY")['price']) 
    krediden_alinan_btc_try = krediden_alinan_btc * btc_try_price
    krediden_alinan_btc_usd = krediden_alinan_btc * btc_usd_price

    krediden_alinan_eth_try = krediden_alinan_eth * eth_try_price
    krediden_alinan_eth_usd = krediden_alinan_eth * eth_usd_price

    krediden_alinan_usd = krediden_alinan_tl / try_usd_price
    toplam_tl = krediden_alinan_btc_try + krediden_alinan_eth_try + krediden_alinan_tl
    toplam_usd = krediden_alinan_btc_usd + krediden_alinan_eth_usd + krediden_alinan_usd


    ana_para_usd = ana_para / 16.35  
    kredi_giris_parasiyla_fark_tl = -(ana_para - toplam_tl)
    kredi_giris_parasiyla_fark_usd = -(ana_para_usd - toplam_usd)

    if kredi_giris_parasiyla_fark_tl < 0 :
        kredi_erime_yuzdesi = kredi_giris_parasiyla_fark_tl / ana_para * 100
    

    x = {"toplam_tl":round(toplam_tl,2),
        "toplam_usd":round(toplam_usd,2),
        "kredi_giris_parasiyla_fark_tl":round(kredi_giris_parasiyla_fark_tl,2),
        "kredi_giris_parasiyla_fark_usd":round(kredi_giris_parasiyla_fark_usd,2),
        "kredi_erime_yuzdesi":-round(kredi_erime_yuzdesi,2)}
    return x




def crypto_rates(asset):
    if asset == 'USDT':
        asset_usd_price = 1
        asset_try_price = float(client.get_symbol_ticker(symbol=f"{asset}TRY")['price'])
    else:
        asset_try_price = float(client.get_symbol_ticker(symbol=f"{asset}TRY")['price'])
        asset_usd_price = float(client.get_symbol_ticker(symbol=f"{asset}USDT")['price'])
    return {"asset":asset,
            "asset_try_price":asset_try_price,
            "asset_usd_price":asset_usd_price}



def ne_durumday??m():
    #Varl??k Analizi
    info = client.get_account()
    varl??klar??m = []

    for i in info["balances"]:
        if float(i["free"]) > 0:
            varl??klar??m.append({"asset": i["asset"], "free":i["free"]})
            
            
    #C??zdan Analizi
    wallet = []
    for varl??k in varl??klar??m:
        varl??k_asset = varl??k["asset"]
        my_varl??k = "{:.8f}".format(float(varl??k["free"]))
        varl??k_asset_degerler = crypto_rates(varl??k_asset)
        varl??k_tl_deger = float(varl??k_asset_degerler["asset_try_price"])
        varl??k_usd_deger = float(varl??k_asset_degerler["asset_usd_price"])

        my_varl??k_tl = float(my_varl??k) * varl??k_tl_deger
        my_varl??k_usd = float(my_varl??k) * varl??k_usd_deger
        varl??k_to_wallet = {"asset": varl??k_asset,
                            "my_varl??k": my_varl??k,
                            "varl??k_tl_deger":varl??k_tl_deger,
                            "varl??k_usd_deger":varl??k_usd_deger,
                            "my_varl??k_tl":round(my_varl??k_tl,2),
                            "my_varl??k_usd":round(my_varl??k_usd,2)}
        wallet.append(varl??k_to_wallet)
    
    
    #Toplam C??zdan Kripto De??erleri
    
    #Toplam Para C??zdan De??erlerim
    my_usd = sum([x["my_varl??k_usd"] for x in wallet])
    my_tl = sum([x["my_varl??k_tl"] for x in wallet])
    my_wallet = {"toplam_usd":my_usd,
        "toplam_tl":my_tl}
    
    
    #Bor?? Analizi
    profit = my_tl - 4646.57
    profit_perc = profit / my_tl
    kalan_para = odenecek_tutar - my_tl
    kalan_para_perc = my_tl / odenecek_tutar * 100
    progress = profit / kalan_para * 100
    
    
    x = {"my_tl":str(f"???{round(my_tl,2)}"),
        "my_usd":str(f"${round(my_usd,2)}"),
        "profit":round(profit,2),
        "profit_perc":round(profit_perc,2),
        "kalan_para":kalan_para,
        "kalan_para_perc":round(kalan_para_perc,2),
        "progress":round(progress,2),
        "wallet":wallet}
    return x





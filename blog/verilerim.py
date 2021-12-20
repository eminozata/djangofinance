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


    x = {"toplam_tl":round(toplam_tl,2),
        "toplam_usd":round(toplam_usd,2),
        "kredi_giris_parasiyla_fark_tl":round(kredi_giris_parasiyla_fark_tl,2),
        "kredi_giris_parasiyla_fark_usd":round(kredi_giris_parasiyla_fark_usd,2)}
    return x




def crypto_rates(asset):
    asset_try_price = float(client.get_symbol_ticker(symbol=f"{asset}TRY")['price'])
    asset_usd_price = float(client.get_symbol_ticker(symbol=f"{asset}USDT")['price'])
    return {"asset":asset,
            "asset_try_price":asset_try_price,
            "asset_usd_price":asset_usd_price}



def ne_durumdayım():
    #Varlık Analizi
    info = client.get_account()
    varlıklarım = []

    for i in info["balances"]:
        if float(i["free"]) > 0:
            varlıklarım.append({"asset": i["asset"], "free":i["free"]})
            
            
    #Cüzdan Analizi
    wallet = []
    for varlık in varlıklarım:
        varlık_asset = varlık["asset"]
        my_varlık = "{:.8f}".format(float(varlık["free"]))
        varlık_asset_degerler = crypto_rates(varlık_asset)
        varlık_tl_deger = float(varlık_asset_degerler["asset_try_price"])
        varlık_usd_deger = float(varlık_asset_degerler["asset_usd_price"])

        my_varlık_tl = float(my_varlık) * varlık_tl_deger
        my_varlık_usd = float(my_varlık) * varlık_usd_deger
        varlık_to_wallet = {"asset": varlık_asset,
                            "my_varlık": my_varlık,
                            "varlık_tl_deger":varlık_tl_deger,
                            "varlık_usd_deger":varlık_usd_deger,
                            "my_varlık_tl":round(my_varlık_tl,2),
                            "my_varlık_usd":round(my_varlık_usd,2)}
        wallet.append(varlık_to_wallet)
    
    
    #Toplam Cüzdan Kripto Değerleri
    
    #Toplam Para Cüzdan Değerlerim
    my_usd = sum([x["my_varlık_usd"] for x in wallet])
    my_tl = sum([x["my_varlık_tl"] for x in wallet])
    my_wallet = {"toplam_usd":my_usd,
        "toplam_tl":my_tl}
    
    
    #Borç Analizi
    profit = my_tl - ana_para
    profit_perc = profit / my_tl * 100
    kalan_para = odenecek_tutar - my_tl
    kalan_para_perc = my_tl / odenecek_tutar * 100
    progress = profit / kalan_para * 100
    
    x = {"my_tl":str(f"₺{round(my_tl,2)}"),
        "my_usd":str(f"${round(my_usd,2)}"),
        "profit":profit,
        "profit_perc":round(profit_perc,2),
        "kalan_para":kalan_para,
        "kalan_para_perc":round(kalan_para_perc,2),
        "progress":round(progress,2),
        "wallet":wallet}
    return x





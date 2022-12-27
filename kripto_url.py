#comments are in Turkish and they are for me, so don't mind them

def url_mech(): #iki ayrı senaryo için tanımlanmış fonksiyon
    import webbrowser #gerekli modül
    url = ("https://www.binance.com/tr/trade/"+currency+"_BUSD?_from=markets&theme=dark&type=spot") #url birleştirme,boşluklara dikkat
    webbrowser.open(url, new=1, autoraise= True) #gerekli kod
    
    exit = input("For exit 0: ")  
    if exit == 0: #bu eklenmeyince programı bitirmediği için sekmeyi direkt kapatıyor
        exit()


        decision = int(input("Press 0 to choose manually, 1 to see top 5 currencies:"))
if decision == 1:
    popular_currencies = {1: "BTC", 2: "DOGE", 3: "AVAX", 4: "ETH", 5: "BNB"} #dictionary
    print("Top 5 currencies: ", popular_currencies)
    
    currency_index = int(input("Enter the index of the currency: ")) 
    currency = popular_currencies[currency_index] #keyin sırasını girerek value bulma
    url_mech()

    elif decision == 0:
    currency = str(input("Enter the code of currency:"))
    url_mech()



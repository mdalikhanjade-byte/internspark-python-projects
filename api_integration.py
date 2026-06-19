import requests

def fetch_crypto_data():
    print("\n--- Live Crypto Price Tracker ---")
    print("Connecting to live API market network...\n")
    
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 5,
        'page': 1
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        crypto_list = response.json()
        
        # This draws a clean, error-free text layout
        print("Rank | Coin Name    | Symbol   | Price (USD)")
        print("-" * 45)
        for coin in crypto_list:
            rank = coin['market_cap_rank']
            name = coin['name']
            symbol = coin['symbol'].upper()
            price = coin['current_price']
            print(f"#{rank:<3} | {name:<12} | {symbol:<8} | ${price}")
            
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_crypto_data()
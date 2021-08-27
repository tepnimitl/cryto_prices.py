echo "> Binance.US"
echo "> ----------"
for i in BTC DOGE ETH ADA COMP BNB IOTA XTZ XLM KNC ATOM UNI ALGO EOS ZIL BAND LTC MKR OMG ETC
do
  curl -X GET https://api.binance.us/api/v3/ticker/price?symbol=$i'USD' | awk -F'"' '{print $4, $8}'
done

echo
echo "> Binance.Com"
echo "> -----------"
for i in BTC DOGE ADA BNB ATOM ZIL LTC XLM SUSHI BAND DOT REEF UNI ETH BCH FIL IOST CAKE ALPHA DODO MATIC MKR ADA BAND ZIL DOGE LTC NEAR CAKE ETH
do
  curl -X GET https://api.binance.com/api/v3/ticker/price?symbol=$i'USDT' | awk -F'"' '{print $4, $8}'
done

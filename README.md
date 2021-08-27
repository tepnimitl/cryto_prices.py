# cryto_prices.py
# Run
./cryto_prices.py 2>/dev/null | grep USD | awk -F' ' '{print $2}'

# customer_idが"CS018205000001"の条件を満たすデータを抽出
df_receipt.query('customer_id == "CS018205000001"')

# customer_idが"CS018205000001", かつ, amountが1000以上, の条件を満たすデータを抽出
df_receipt.query('customer_id == "CS018205000001" & amount >= 1000')

# customer_idが"CS018205000001", かつ, (amountが1000以上, または, quantityが5以上), の条件を満たすデータを抽出
df_receipt.query('customer_id == "CS018205000001" & (amount >= 1000 | quantity >= 5)')

# df_storeからstore_cdが"S14"で始まるものだけ抽出
df_store.query("store_cd.str.startswith('S14')", engine='python').head(10)

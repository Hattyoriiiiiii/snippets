import requests, zipfile
import io

# zip?
zip_file_url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/'
r = requests.get(zip_file_url, stream = True)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

# 
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/'
res = requests.get(url).content
df = pd.read_csv(io.StringIO(res.decode('utf-8')), header=None)
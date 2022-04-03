import requests, sys
url='https://justinjackson.ca/words.html'
response = requests.get(url)
num_word=0
if response.status_code != 200:
    print(f"cannot connect to url{url}")
    sys.exit(1)
res=response.text.split('\n')
for line in res:
    line = line.strip()
    if not line.startswith('<'):
        for word in line:
            word=word.strip()
            if not word.startswith('<'):
                  num_word=num_word+1
        print(line)
print(f"{num_word} is number of words in the page not including the headers")
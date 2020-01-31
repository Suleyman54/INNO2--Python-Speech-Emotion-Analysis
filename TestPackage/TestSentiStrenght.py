from SentiStrenght.senti_client import sentistrength

file1 = open("C:/Users/suley/Pycharm/Ziggoo/Ziggo/Ziggo/ben2.txt","r")
lijst = str(file1.readlines())


senti = sentistrength('NL')
res = senti.get_sentiment(lijst)
print(res)

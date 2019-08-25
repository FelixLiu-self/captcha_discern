import requests
from lxml import etree
url="http://www.yundama.com/user/history/2019-08-25/20/%s"
headers={
    "User-Agent":"User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Cookie":"IESESSION=alive; pgv_pvi=4940731392; pgv_si=s7399095296; tencentSig=7328908288; _qddaz=QD.dk2zvj.o9ni6i.jzqxo1zi; _qdda=3-1.1; _qddab=3-li9x8b.jzqxo1zj; _qddamta_4008588180=3-0; session=RBnhp6O7f1lmq6WHbLIwSn3PBt0Z8dynAd4V3QUEE7POSBzyAaeubSTRIUqFhpfYvDtoi%2FL4ptNO50n%2BemmNfABCb%2FljgApLxW7WVfEVNmKoaLV2eCdLvLiY%2B%2BJG173CEB0KcKUyGYOF1rpcyZ6XMnVzizX0sSTPns7nC1IhJ61DYSfL99rKSWZxCj2oONy%2F%2BpvQUhKv8%2BLkvwGsifyiG%2FoItTnMBprdhp45KqK9YmHjJcbeVU56bYOcAN4ykWAc6J3z4DRZ1rQMY0Ec2xHtt%2F0yB4RT63YCXOGBHxMhXlFNVYhD1elkMjkIwnNUbh7G92ZJyw%2BslwtWh5hSzVSYssKiQ%2FMnesT2YvMIsfWysirrKlH73oN%2Fzvtliw9w00yoHY%2FqKvxAFLxtxpNvD3bu%2FE1wH0UhTW7BFvOQAVIcR%2BSx3wxeHby1abQFacu2O5lnAolzpFpjYrMe2OuQaXoB8Tr7gr9ndoNG%2BElsCWdd4kFPaA0XwDKPWiSWayQkylCTchuvOe8H6K2E7%2B%2FSIqvfEt6OyEPprVpytCN5jcODyNkUlw9Zz8mE8tnRTl3HbYLeGXedH9TbuKBSOqbgikqftNAccJQNZtHcXmN0hCQW6XjxbETzlq8j%2FGfGmh6qG2qEJIB2o9yoxMfP5%2Bq0yS3T%2BorSwE%2FlltcX4GKEBrEdrYs%3D"
}
for i in range(0,19):
    i=i*10
    response=requests.get(url%str(i),headers=headers)
    html=etree.HTML(response.content.decode('gbk'))
    parse=html.xpath('//table/tr')
    for node in parse:
        try:
            imge_link=node.xpath('td[1]/img/@src')[0]
            string=node.xpath('td[2]/text()')[0].replace('\r','').replace('\n','').replace('\t','')
            imge_response=requests.get(imge_link).content
            with open('Images\\'+string+'.png','wb') as f:
                f.write(imge_response)
                print(i)
        except Exception as e:
            print(str(e))


fruits2 = ("mango","apple","banana","pear","strawberry");
print(sorted(fruits2));
fruits3 = {"mango","apple","banana","pear","strawberry"};
print(sorted(fruits3));
guitars = [
    {'model' : 'yahama f310','price':8400},
    {'model' : 'faith  neptune','price':50000},
    {'model' : 'faith apollo venus','price':35000},
    {'model' : 'taylor 814ce','price':450000}  
]
print(sorted(guitars,key = lambda item :item.get('price'),reverse=True));
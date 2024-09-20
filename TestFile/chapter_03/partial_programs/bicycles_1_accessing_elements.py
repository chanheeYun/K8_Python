bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[1] = 'samcheonri' #바꿔치기
#추가 -> insert, append
bicycles.append('swork')
bicycles.insert(1, 'cannondale')
print(bicycles)
print(bicycles[-3].title())
del bicycles[0]
print(bicycles)

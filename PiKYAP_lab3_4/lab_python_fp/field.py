
def field(items, *args):
    assert len(args) > 0
    for i in items:
        yield i[args[0]] if len(args) == 1 else {j: i[j] for j in args}


if __name__ == '__main__':
    goods = [
       {'title': 'Ковер', 'price': 2000, 'color': 'green'},
       {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    a = field(goods, 'title')
    print(next(a)) # Ковер
    print(next(a)) # Диван для отдыха
    print(next(a))  # Диван для отдыха
    for i in field(goods, 'color'):
        print(i) # green и потом black
    a = field(goods, 'title', 'price')
    print(next(a)) # {'title': 'Ковер', 'price': 2000}
    print(next(a)) # {'title': 'Диван для отдыха', 'price': 5300}

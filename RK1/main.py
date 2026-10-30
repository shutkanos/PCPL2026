from operator import itemgetter

class Detail:
    def __init__(self, id, name, price, manufacturer_id):
        self.id = id
        self.name = name
        self.price = price
        self.manufacturer_id = manufacturer_id

class Manufacturer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class DetailManufacturer:
    def __init__(self, detail_id, manufacturer_id):
        self.detail_id = detail_id
        self.manufacturer_id = manufacturer_id

manufacturers = [
    Manufacturer(1, "Автоваз"),
    Manufacturer(2, "АртАлмаз"),
    Manufacturer(3, "ООО 'Тмыв денег'"),
]
details = [
    Detail(1, "Свеча зажигания", 600, 1),
    Detail(2, "Коленчатый вал", 18500, 1),
    Detail(3, "Алмазная коронка", 9200, 2),
    Detail(4, "Шлифовальный диск", 3400, 2),
    Detail(5, "Позолоченный болт", 45000, 3),
    Detail(6, "Титановая заглушка", 120000, 3),
]
details_manufacturers = [
    DetailManufacturer(1, 1),
    DetailManufacturer(1, 2),
    DetailManufacturer(2, 1),
    DetailManufacturer(2, 3),
    DetailManufacturer(2, 4),
    DetailManufacturer(3, 3),
    DetailManufacturer(3, 5),
    DetailManufacturer(3, 6),
]

def main():
    one_to_many = [
        (d.name, d.price, m.name)
        for m in manufacturers
        for d in details
        if d.manufacturer_id == m.id
    ]

    many_to_many_temp = [
        (m.name, dm.manufacturer_id, dm.detail_id)
        for m in manufacturers
        for dm in details_manufacturers
        if m.id == dm.manufacturer_id
    ]

    many_to_many = [
        (d.name, d.price, manufacturer_name)
        for manufacturer_name, manufacturer_id, detail_id in many_to_many_temp
        for d in details
        if d.id == detail_id
    ]

    print("Задание Г1")
    res_g1 = {}
    for m in manufacturers:
        if m.name.startswith("А"):
            m_details = list(filter(lambda i: i[2] == m.name, one_to_many))
            res_g1[m.name] = [name for name, _, _ in m_details]

    print(res_g1)
    print()

    print("Задание Г2")
    res_g2_unsorted = []
    for m in manufacturers:
        m_details = list(filter(lambda i: i[2] == m.name, one_to_many))
        if len(m_details) > 0:
            res_g2_unsorted.append((m.name, max([price for _, price, _ in m_details])))

    res_g2 = sorted(res_g2_unsorted, key=itemgetter(1), reverse=True)
    print(res_g2)
    print()

    print("Задание Г3")
    res_g3 = sorted(many_to_many, key=itemgetter(2))
    print(res_g3)


if __name__ == '__main__':
    main()
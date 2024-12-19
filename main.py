from djikstra import *

def main():
    ## uji
    data_a = Graph(1, "kode 1")
    data_b = Graph(2, "kode 2")
    data_c = Graph(3, "kode 3")
    data_d = Graph(4, "kode 4")
    data_e = Graph(5, "kode 5")
    data_b.connect_graph(data_d, 50.2)
    data_b.connect_graph(data_a, 50.2)
    data_b.connect_graph(data_e, 50.2)
    data_d.connect_graph(data_e, 50.2)
    data_d.connect_graph(data_a, 20.2)
    data_c.connect_graph(data_e, 40.2)
    for i in data_a.connection:
        print(f'nilai: {i.label}')
    result = DjikstraRunner()
    hasil = list(reversed(result.run(data_a, data_c)))
    for i in hasil:
        print(f'Hasil: {i.label}')


if __name__ == '__main__':
    main()

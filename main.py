import djikstra

def main():
    data_a = djikstra.Graph(1, "kode 1")
    data_b = djikstra.Graph(2, "kode 2")
    data_a.connect_graph(data_b, 50.2)
    data_a.debugging()




if __name__ == '__main__':
    main()

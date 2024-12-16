class Graph:
    def __init__(self, unit:int, label:str):
        self.unit = unit
        self.connection = []
        self.jarak = [] # jarak dalam Meter
        self.label = label
    
    def connect_graph(self, graph, jarak:float):
        self.connection.append(graph)
        self.jarak.append(jarak)

    def debugging(self):
        for i in range(len(self.connection)):
            print(f"terhubung ke graph: {self.connection[i].unit} dengan label: {self.connection[i].label}, dengan jarak: {self.jarak[i]}")



def main():
    pass


    
if __name__ == '__main__':
    main()

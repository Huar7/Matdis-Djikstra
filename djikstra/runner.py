class DjikstraRunner:
    def __init__(self):
        self.performance_nodes = []

        pass
    
    def run(self, first_position, target, already_visited=[], finale_data=[]):
        for i in range(len(first_position.connection)): ## menerima parameter dari Graph

            if i == 0:
                currently_path = []
                for j in range(len(first_position.connection)): ## ini untuk menentukan jarak terpendek
                    currently_path.append(first_position.connection[j])
                    currently_path = self.buble_sorting(currently_path)                    
                for h in currently_path:
                    print(f'hasil sorting: {h.label}') ## hasil kini terbuka

            print(currently_path[i].label)
            if currently_path[i] == target: ## untuk pengecekan target terhadapa posisi utama
                print("-------------Found target-------------")
                finale_data.append(currently_path[i])
                break

            elif target in finale_data:
                finale_data.append(currently_path[i])
                break
            
            if currently_path[i] in already_visited:
                print("Already visited")
                continue
            already_visited.append(currently_path[i])

            self.run(currently_path[i], target, already_visited=already_visited, finale_data=finale_data)
            

        return finale_data
    


    def buble_sorting(self, current_data: list) -> list:
        ## ini untuk melaukukan sorting berdasarkan algoritmanya
        for i in range(len(current_data)):
            if i < len(current_data) - 1: ## menghindari over Listing
                if current_data[i].jarak > current_data[i + 1].jarak:
                    not_long = current_data[i] ## Temporary Variable
                    current_data[i] = current_data[i+1]
                    current_data[i+1] = not_long

            if i > 0:
                if current_data[i].jarak < current_data[i - 1].jarak:
                    not_long = current_data[i] ## Temporary Variables
                    current_data[i] = current_data[i-1]
                    current_data[i-1] = not_long
        return current_data
        
    def debugging():
        pass
        
        
        




def main():
    pass



if __name__ == "__main__":
    main()

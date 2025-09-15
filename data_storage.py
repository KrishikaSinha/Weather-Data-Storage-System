class WeatherDataStorage:
    def __init__(self, date: str, city: str, temperature: float):
        self.date = date
        self.city = city
        self.temperature = temperature


class WeatherDataStorage:
    def __init__(self, years: list, cities: list):
        self.years = years
        self.cities = cities
        self.data = [[None for _ in range(len(cities))] for _ in range(len(years))]
        self.year_index = {year: idx for idx, year in enumerate(years)}
        self.city_index = {city: idx for idx, city in enumerate(cities)}

    def populate_array(self, record: WeatherDataStorage):
        year = record.date.split('/')[-1]  # extract year from date string (e.g. "12/05/2024" -> "2024")
        if year in self.year_index and record.city in self.city_index:
            row = self.year_index[year]
            col = self.city_index[record.city]
            self.data[row][col] = record.temperature
        else:
            print("Year or city not recognized.")

    def row_major_access(self):
        print("Row-major order traversal:")
        for row in self.data:
            for temp in row:
                print(temp, end=' ')
            print()

    def column_major_access(self):
        print("Column-major order traversal:")
        for col_idx in range(len(self.cities)):
            for row_idx in range(len(self.years)):
                print(self.data[row_idx][col_idx], end=' ')
            print()

    def handle_sparse_data(self):
        print("Sparse Data Handling (using sentinel -1):")
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] is None:
                    self.data[i][j] = -1  

    def retrieve(self, city: str, year: str):
        if year in self.year_index and city in self.city_index:
            row = self.year_index[year]
            col = self.city_index[city]
            return self.data[row][col]
        return None

    def analyze_complexity(self):
        print("Time Complexity:")
        print("- Insertion: O(1)")
        print("- Retrieval: O(1)")
        print("- Sparse Handling: O(n * m)")
        print("\nSpace Complexity: O(n * m), where n = years, m = cities")

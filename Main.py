from weather_record import WeatherRecord
from data_storage import WeatherDataStorage

def main():
    years = ['2023', '2024']
    cities = ['Delhi', 'Mumbai', 'Chennai']

    storage = WeatherDataStorage(years, cities)

    # Insert sample records
    records = [
        WeatherRecord('01/01/2023', 'Delhi', 25.5),
        WeatherRecord('01/01/2024', 'Mumbai', 30.2)
    ]

    for rec in records:
        storage.populate_array(rec)

    storage.handle_sparse_data()

    storage.row_major_access()
    storage.column_major_access()

    print("\nRetrieving temperature for Delhi in 2023:", storage.retrieve('Delhi', '2023'))
    storage.analyze_complexity()

if __name__ == '__main__':  
    main()

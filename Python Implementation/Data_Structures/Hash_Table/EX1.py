'''
Source: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/4_hash_table_exercise.md

nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
    What was the average temperature in first week of Jan
    What was the maximum temperature in first 10 days of Jan
'''
import hash_table

class HashTable(hash_table.HashTable):
    def week_avg(self):
        temperature = 0
        
        for i in range(7):
            temperature += self.__getitem__(f"Jan {i+1}")

        return temperature/7

if __name__ == "__main__":
    table = HashTable()
    table['Jan 2'] = 31
    table['Jan 1'] = 27
    table['Jan 3'] = 23
    table['Jan 4'] = 34
    table['Jan 5'] = 37
    table['Jan 6'] = 38
    table['Jan 7'] = 29
    table['Jan 8'] = 30
    table['Jan 9'] = 35
    table['Jan 10'] = 30
    print(table.week_avg())
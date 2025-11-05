import requests


def send_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return False

def main():
    url_name = 'https://swapi.dev/api/people/1/'
    data_name = send_request(url_name)
    return data_name

def main_planet():
    data = main()
    planet = data['homeworld']
    data_planet = send_request(planet)
    return data_planet

def pilots():
    end_pilot_list = []
    url_pilots = 'https://swapi.dev/api/starships/?search-Millennium Falcon'
    data = send_request(url_pilots)
    index = 0
    for _ in range(0, 36):
        if data['results'][_]['name'] == 'Millennium Falcon':
            index = _
            break
    pilots_list = data['results'][index]['pilots']
    for _ in pilots_list:
        pilot = send_request(_)
        end_pilot_list.append(pilot['name'])
    return end_pilot_list

if __name__ == '__main__':
    data = main()
    data_planet = main_planet()
    pilots_list = pilots()
    name = data['name']
    height = data['height']
    mass = data['mass']
    hair_color = data['hair_color']
    homeworld = data_planet['name']
    print(f'Имя: {name}')
    print(f'Рост: {height}')
    print(f'Масса: {mass}')
    print(f'Цвет волос: {hair_color}')
    print(f'Планета: {homeworld}')
    print('Список пилотов Millenium Falcon:')
    for _ in pilots_list:
        print(f' - {_}')
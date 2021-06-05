#ejecricio 1
print('----------------------------------------------- Ejercicio 1 -------------------------------------------------------------')
def closePrimeNumber(num: int) -> int:
    num += 1
    if num < 2:
        return 1
    elif num == 2:
        return 2
    else:
        for i in range(2, int(num**0.5 + 1)):
            if num % i == 0:
                return closePrimeNumber(num)
        return num
print(closePrimeNumber(20))
print('\n')
print('----------------------------------------------- Ejercicio 2 -------------------------------------------------------------')
#ejercicio 2
import requests
def getPokemonType(name: str) -> dict:
    url = f"http://pokeapi.co/api/v2/type/{name}"
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        return {'Error': response.status_code}
print(getPokemonType('ground'))
print('\n')
print('----------------------------------------------- Ejercicio 3 -------------------------------------------------------------')

#ejercicio 3
import requests
def getPokemonTypeArray(name: str) -> any:
    url = f"http://pokeapi.co/api/v2/type/{name}"
    response = requests.get(url)
    if response.ok:
        try:
            return response.json()['pokemon']
        except:
            return []
    else:
        return []
print(getPokemonTypeArray('ground'))
print('\n')
print('----------------------------------------------- Ejercicio 4 -------------------------------------------------------------')
#ejercicio 4
import requests
def getPokemonTypeArrayStartWithS(name: str) -> any:
    url = f"http://pokeapi.co/api/v2/type/{name}"
    response = requests.get(url)
    if response.ok:
        try:
            pokemons = response.json()['pokemon']
            return [value for value in pokemons if (str(value['pokemon']['name'][0]).lower() == 's')]
        except:
            return []
    else:
        return []
print(getPokemonTypeArrayStartWithS('ground'))

#ejercicio 5 have a app


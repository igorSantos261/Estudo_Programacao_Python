#Informações Pais

from countryinfo import CountryInfo

country = CountryInfo(input("Digite o nome do Pais:  "))

print(f'Pais: {country.name()}')
print(f'Capital: {country.capital()}')
print(f'Moeda: {country.currencies()}')
print(f'Idioma: {country.languages()}')
print(f'Faz Fronteira: {country.borders()}')
print(f'Código de Area: {country.calling_codes()}')
print(f'Papulação: {country.population()}')


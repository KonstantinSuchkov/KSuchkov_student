import utils

print(utils.currency_rates('USD'))
print(utils.currency_rates('EUR'))
print(utils.currency_rates('USD') + utils.currency_rates('EUR'))
print(utils.currency_rates('USD') * 1500)
def plant_recommendation(care):
    if care == 'low':
        print('aloe')
    elif care == 'medium':
        print('pothos')
    else:
        print('orchid')


plant_recommendation('low')
plant_recommendation('medium')
plant_recommendation('high')

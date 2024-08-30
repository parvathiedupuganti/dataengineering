
#1)Demand-Supply Mismatch Analysis

zone_regional_zone_weights = {}
with open('FMCG_data.csv', mode='r') as file:
    headers = file.readline().strip().split(',')
    zone_index = headers.index('zone')
    regional_zone_index = headers.index('WH_regional_zone')
    product_weight_index = headers.index('product_wg_ton')

    for line in file:
        values = line.strip().split(',')
        zone = values[zone_index]
        regional_zone = values[regional_zone_index]

        try:
            product_weight = float(values[product_weight_index])
        except ValueError:
            continue        
        key = (zone, regional_zone)
        if key in zone_regional_zone_weights:
            zone_regional_zone_weights[key] += product_weight
        else:
            zone_regional_zone_weights[key] = product_weight
for key, total_weight in zone_regional_zone_weights.items():
    print(f'Zone: {key[0]}, Regional Zone: {key[1]}, Total Supply Weight: {total_weight}')

#2)Warehouse Refill Frequency Correlation

def convert_capacity_to_numeric(capacity_size):
    size_map = {
        'Small': 1,
        'Mid': 2,
        'Large': 3
    }
    return size_map.get(capacity_size, 0)

capacities = []
refill_requests = []
#3)Transport Issue Impact Analysis

issue_weights = {}
with open('FMCG_data.csv', mode='r') as file:
    headers = file.readline().strip().split(',')
    issue_index = headers.index('transport_issue_l1y')
    product_weight_index = headers.index('product_wg_ton')

    for line in file:
        values = line.strip().split(',')
        issue = values[issue_index]
        try:
            product_weight = float(values[product_weight_index])
        except ValueError:
            continue 
        if issue in issue_weights:
            issue_weights[issue] += product_weight
        else:
            issue_weights[issue] = product_weight
for issue, total_weight in issue_weights.items():
    print(f'Transport Issue: {issue}, Total Supply Weight: {total_weight}')

#4)Storage Issue Analysis

storage_issue_weights = {}
with open('FMCG_data.csv', mode='r') as file:

    headers = file.readline().strip().split(',')
    issue_index = headers.index('storage_issue_reported_l3m')
    product_weight_index = headers.index('product_wg_ton')

    for line in file:
        values = line.strip().split(',')
        issue = values[issue_index]
        try:
            product_weight = float(values[product_weight_index])
        except ValueError:
            continue 
        if issue in storage_issue_weights:
            storage_issue_weights[issue] += product_weight
        else:
            storage_issue_weights[issue] = product_weight

for issue, total_weight in storage_issue_weights.items():
    print(f'Storage Issue: {issue}, Total Supply Weight: {total_weight}')
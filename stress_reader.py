import yaml


#open yaml file using pyyaml
with open() as f:
    config = yaml.safe_load(f)

#printing all scenarios
print("vvvvvv Stress Scenarios vvvvvv")
for scenario in config['scenario']:
    print(f" - {scenario['name']} ({scenario['type']})")

# Print all assets
print("\nvvvvvv All Assets vvvvvv")
for asset in config['assets']:
    print(f"  - {asset['name']} ({asset['class']}, Liquidity: {asset['liquidity_bucket']})")

# Print scenario-to-asset mappings
print("\nvvvvvv Scenario-to-Asset Mapping: vvvvvv")
for mapping in config["scenario_asset_mapping"]:
    print(f"  - {mapping['scenario']} ➡ {', '.join(mapping['affected_assets'])}")

import yaml

with open('./training-code/py-training/Spreadsheet/test-pars.yaml') as yaml_file:
    print(yaml.load(yaml_file, Loader=yaml.FullLoader))
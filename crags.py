import json
import os

# Load JSON data
with open('olog.json') as f:
    data = json.load(f)

# Create vault directory  
vault_dir = 'rainforest_vault'
if not os.path.exists(vault_dir):
    os.mkdir(vault_dir)

types_dir = os.path.join(vault_dir, 'types')
os.mkdir(types_dir)

aspects_dir = os.path.join(vault_dir, 'aspects') 
os.mkdir(aspects_dir)

instances_dir = os.path.join(vault_dir, 'instances')
os.mkdir(instances_dir)

# Create files
for type in data['Olog']['Types']:
    filename = f"{type['Name'].lower().replace(' ', '_')}.md"
    filepath = os.path.join(types_dir, filename)
    
    with open(filepath, 'w') as f:
        f.write(f"# {type['Name']}\n\n{type['Description']}")
        
for aspect in data['Olog']['Aspects']:
    filename = f"{aspect['Label'].lower().replace(' ', '_')}.md"
    filepath = os.path.join(aspects_dir, filename)
    
    with open(filepath, 'w') as f: 
        f.write(f"[[{aspect['Source'].lower().replace(' ', '_')}]] | [[{aspect['Label']}]] -> [[{aspect['Target'].lower().replace(' ', '_')}]]")
        
for type in data['Olog']['Types']:
    if type['Instances']:
        filename = f"{type['Name'].lower().replace(' ', '_')}.md"
        filepath = os.path.join(instances_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(f"Instances of [[{type['Name'].lower().replace(' ', '_')}]]:\n")
            for instance in type['Instances']:
                f.write(f"- [[{instance['Name']}]]\n")

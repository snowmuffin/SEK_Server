import os


current_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_directory, "Torch.cfg")

with open(config_file_path, 'r') as file:
    config_content = file.read()
new_instance_path = os.path.join(current_directory, "Instance")
config_content = config_content.replace('<InstancePath></InstancePath>', f'<InstancePath>{new_instance_path}</InstancePath>')
with open(config_file_path, 'w') as file:
    file.write(config_content)

print(f"Updated Torch.cfg with new InstancePath: {new_instance_path}")
input("Press Enter to close the window...")

import os
import xml.etree.ElementTree as ET

def process_xml_file(file_path_list):
    # Open and parse the XML file
    gate_list = []
    for filepath in file_path_list:
        print(filepath)
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()

            # Loop through each <Gate> element in the XML
            for gate in root.findall('.//Gate'):  # Adjust the path if needed
                name = gate.find('Name')
                if name is not None:
                    gate_list.append(name.text)
                    print(name.text)
            for destinations in root.findall('.//Destinations'):
                destinations.clear()

        except ET.ParseError as e:
            print(f"Error parsing {filepath}: {e}")
        tree.write(filepath)

    for filepath in file_path_list:
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            # Loop through each <Gate> element in the XML
            for gate in root.findall('.//Gate'):  # Adjust the path if needed
                name = gate.find('Name')
                name_last2 = name.text[-2:]
                filtered_gate = [s for s in gate_list if s.endswith(name_last2) and s != name.text]

                destinations = gate.find('Destinations')
                if destinations is None:
                    # <Destinations> 요소가 없다면 생성합니다.
                    destinations = ET.SubElement(gate, 'Destinations')
                for dest_name in filtered_gate:
                    destination = ET.SubElement(destinations, 'Destination')
                    ET.SubElement(destination, 'DisplayName').text = str(dest_name)
                    ET.SubElement(destination, 'Name').text = str(dest_name)
                    # 기타 필요한 속성을 추가할 수 있습니다.
                    ET.SubElement(destination, 'Id').text = "ID" + str(dest_name)
            
        except ET.ParseError as e:
            print(f"Error parsing {filepath}: {e}")
        tree.write(filepath)
    
def find_files(directory, filename):
    # Walk through all directories and files in 'directory'
    file_path_list=[]
    for root, dirs, files in os.walk(directory):
        # Check if 'filename' is in the list of files
        if filename in files:
            full_path = os.path.join(root, filename)
            file_path_list.append(full_path)
            # Process each found XML file
    process_xml_file(file_path_list)
    print(file_path_list)


# Directory to start from, adjust this to the root of your library
root_directory = 'C:\SEK_Server'

# Filename to look for
target_filename = 'Wormhole.cfg'

# Call the function with the root directory and the filename to find
find_files(root_directory, target_filename)
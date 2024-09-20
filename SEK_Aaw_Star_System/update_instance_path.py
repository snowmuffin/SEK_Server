import os

# 현재 스크립트가 실행되는 경로를 가져옴
current_directory = os.path.dirname(os.path.abspath(__file__))

# Torch.cfg 파일 경로
config_file_path = os.path.join(current_directory, "Torch.cfg")

# 설정 파일 내용 읽기
with open(config_file_path, 'r') as file:
    config_content = file.read()

# 현재 디렉토리 경로로 설정 파일의 InstancePath 값을 수정
new_instance_path = os.path.join(current_directory, "Instance")
config_content = config_content.replace('<InstancePath></InstancePath>', f'<InstancePath>{new_instance_path}</InstancePath>')

# 수정된 설정 파일 내용을 다시 저장
with open(config_file_path, 'w') as file:
    file.write(config_content)

print(f"Updated Torch.cfg with new InstancePath: {new_instance_path}")
input("Press Enter to close the window...")

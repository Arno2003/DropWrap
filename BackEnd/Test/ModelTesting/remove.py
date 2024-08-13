import os
import shutil

path = "BackEnd\Test\ModelTesting\outputData\Andhra Pradesh\Merged"
dir = "..\\..\\BackEnd\\Test\ModelTesting\\outputData"

for subDir in os.listdir(dir):
    directory = os.path.join(dir, f"{subDir}\\Merged")  
    if os.path.exists(directory):
        # Delete the directory and all its contents
        shutil.rmtree(directory)
        print(f'Deleted: {directory}')
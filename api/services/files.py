import os
from fastapi import UploadFile
import shutil
from datetime import datetime

def save_file(file: UploadFile):
  date = datetime.now()
  folder_path = f"uploads/{str(date.year)}/{str(date.month)}/{str(date.day)}/"
  image_path = f"{folder_path}({date.hour}h{date.minute}m{date.second}s)-{file.filename}"

  if not os.path.exists(folder_path):
    os.makedirs(folder_path)

  with open(image_path, 'wb') as buffer:
    shutil.copyfileobj(file.file, buffer)

  return image_path

def delete_file(path: str):
  os.remove(path)

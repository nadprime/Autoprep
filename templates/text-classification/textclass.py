import sys
import pandas as pd

filename = str(sys.argv[1])
project_name = str(sys.argv[2])
task_name = str(sys.argv[3])
textual_coloum = str(sys.argv[4])

from clearml import Task, StorageManager
task = Task.init(project_name=project_name, task_name=task_name)


data = pd.read_csv(filename)

NO_OF_ENTRIES = len(data)//8
imdb = data.review.iloc[:NO_OF_ENTRIES]


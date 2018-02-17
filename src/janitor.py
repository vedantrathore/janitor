import os
from pprint import pprint

class Janitor():

	file_list = []

	def __init__(self,search_directory):
		self.directory = search_directory

	def analyse(self):
		for root, dirs, files in os.walk(self.directory):
			for file in files:
				path_to_file = os.path.join(root, file)
				try:
					size = os.path.getsize(path_to_file)
					extension = file.split('.')[-1]
					file_metadata = {
						'name' : file,
						'path' : path_to_file,
						'size' : size,
						'extension' : extension
	 				}
	 				self.file_list.append(file_metadata)
	 			except Exception:
	 				pass # todo: find an elegant way to handle exceptions
 		return self.file_list

 	def clean(self,output_directory, file_list=None):
 		if file_list is None:
	 		input_directory = self.directory
	 		file_list = [f for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f))]
	 		for file in file_list:
	 			file = os.path.basename(file)
	 			extension = file.split('.')[-1]
	 			new_path = os.path.join(output_directory, extension.upper())
	 			if not os.path.exists(new_path):
	 				os.makedirs(new_path)
	 			os.rename(os.path.join(input_directory , file), os.path.join(new_path , file))
	 		return


if __name__ == '__main__':
	search_directory = '/Users/vedantrathore/Desktop/Important Stuff'
	cleaner = Janitor(search_directory)
	cleaner.clean('/Users/vedantrathore/Documents/Janitor')
import pandas as pd

class ExcelObject():

	def __init__(self, file_directory):
		self.__file_directory = file_directory
		try:
			self.__dataframe = pd.read_excel(file_directory)
		except FileNotFoundError:
			self.__dataframe = None

	def __repr__(self):
		return f"file located at {self.__file_directory}"

	def __str__(self):
		return str(self.__file_directory)

	def __del__(self):
		#just to be safe I delete the dataframe specifically 
		del self.__dataframe

	def getColumns(self):
		return self.__dataframe.columns

	def getEachForColumn(self, column_name):
		return self.__dataframe[column_name].tolist()

	def dataframeIsValid(self):
		if self.__dataframe is not None:
			return True
		return False


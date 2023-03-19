import datetime

class Logger:

	def __init__(self, mode="PRINT", filepath="./log.log"):
		self.mode = mode
		self.filepath = filepath
		if self.mode == "FILE":
			# Create log file
			with open(filepath, "a") as logfile:
				pass

	def info(self, msg):
		logstring = f"{datetime.datetime.now()} INFO - {msg}\n"
		self.__write_file(logstring)

	def err(self, msg):
		logstring = f"{datetime.datetime.now()} ERROR - {msg}\n"
		self.__write_file(logstring)

	def warn(self, msg):
		logstring = f"{datetime.datetime.now()} WARN - {msg}\n"
		self.__write_file(logstring)

	def fatal(self, msg):
		logstring = f"{datetime.datetime.now()} FATAL - {msg}\n"
		self.__write_file(logstring)

	def __write_file(self, line):
		if self.mode == "FILE":
			with open(self.filepath, "a") as logfile:
				logfile.write(line)
		else:
			print(line)
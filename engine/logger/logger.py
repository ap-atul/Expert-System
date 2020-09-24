"""
Class to print normal prints with strings
but with colors
"""


class Log:
	modes = dict()
	modes['DEBUG'] = '\033[92m'
	modes['ERROR'] = '\033[91m'
	modes['INFO'] = '\033[94m'
	modes['WARN'] = '\033[93m'
	printing = True

	def log(self, mode='INFO'):
		"""
		reading the mode and selecting
		colors based on that
		:param mode:
		:return:
		"""
		print(f"{Log.modes[mode]}[{mode}] {self}")

	@staticmethod
	def setPrint(mode=True):
		Log.printing = mode

	@staticmethod
	def d(message):
		Log.log(message, mode='DEBUG')

	@staticmethod
	def i(message):
		Log.log(message, mode='INFO')

	@staticmethod
	def e(message):
		Log.log(message, mode='ERROR')

	@staticmethod
	def w(message):
		Log.log(message, mode='WARN')

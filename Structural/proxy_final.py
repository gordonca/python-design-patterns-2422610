import time

class Producer:
	"""Define the 'resource-intensive' object to instantiate!"""
	def __init__(self, _num) -> None:
		self._num = _num

	def produce(self):
		print(f"Producer {self._num} is working hard!")

	def meet(self):
		print(f"Producer {self._num} has time to meet you now!")

class Proxy:
	""""Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""
	def __init__(self):  
		self.occupied = 'No'
		self.producer = None

	def produce(self, _num):
		"""Check if Producer is available"""
		print("Artist checking if Producer is available ...")

		if self.occupied == 'No':
			#If the producer is available, create a producer object!
			self.producer = Producer(_num)
			time.sleep(2)

			#Make the prodcuer meet the guest!
			self.producer.meet()
			
		else:
			#Otherwise, don't instantiate a producer 
			time.sleep(2)
			print("Producer is busy!")

#Instantiate a Proxy
p = Proxy()

#Make the proxy: Artist produce until Producer is available
p.produce(1)
p.produce(2)

#Change the state to 'occupied'
p.occupied = 'Yes'

#Make the Producer produce
p.produce(3)


class Complex:
	real=0
	img=0
	m_real=0
	m_img = 0
	def __init__(self , real , img):
		self.real= real
		self.img = img

	def display(self):
		print(self.real , f"+ i{self.img}")

	def multiply(self , o2):
		real1 ,img1 = self.real , self.img
		real2 , img2 = o2.real , o2.img
		m_real = real1*real2 - img1*img2
		m_img = real1*img2 + real2*img1
		print(m_real , f"+ i{m_img}")

obj = Complex( 5 ,4)
obj1 = Complex( 3 , 6)

obj.display()
obj1.display()
c = obj.multiply(obj1)

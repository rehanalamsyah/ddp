from Animal import *
class Badak(Animal):

    def __init__(self, nama, makanan, hidup, berkembangbiak, cula):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.cula = cula

    def hewan1(self):
        print("Nama \t\t :", self.nama,
                "\nMakanan \t :", self.makanan,
                "\nHidup \t\t :", self.hidup, 
                "\nBerkembang Biak  :", self.berkembangbiak,
                "\nCiri Khas \t :", self.cula,
                "\n-------------------------------------")


from Animal import *
class Ular(Animal):

    def __init__(self, nama, makanan, hidup, berkembangbiak, Berbisa):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.Berbisa = Berbisa

    def hewan3(self):
        print("Nama \t\t :", self.nama,
                "\nMakanan \t :", self.makanan,
                "\nHidup \t\t :", self.hidup, 
                "\nBerkembang Biak  :", self.berkembangbiak,
                "\nBerbisa \t :", self.Berbisa,
                "\n-------------------------------------")
from Animal import*
class Ikan(Animal):

    def __init__(self, nama, makanan, hidup, berkembangbiak, jenis):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.jenis = jenis

    def hewan2(self):
        print("Nama \t\t :", self.nama,
                "\nMakanan \t :", self.makanan,
                "\nHidup \t\t :", self.hidup, 
                "\nBerkembang Biak  :", self.berkembangbiak,
                "\nJenis \t\t :", self.jenis,
                "\n-------------------------------------")
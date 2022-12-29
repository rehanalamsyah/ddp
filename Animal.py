class Animal:

    def __init__(self, nama, makanan, hidup, berkembangbiak) :
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak

    def printAnimal(self):
        print(self.nama, self.makanan, self.hidup, self.berkembangbiak)

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



x = Badak("Badak", "Daging", "Darat", "Melahirkan", "Bercula")
x.hewan1()

y = Ikan("Ikan", "Cacing", "Air", "Bertelur", "clownfish")
y.hewan2()

z = Ular("Ular", "Tikus", "Darat", "Bertelur & Melahirkan","Iya")
z.hewan3()





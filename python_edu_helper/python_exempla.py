import ast

class PythonLearningTool:
    def __init__(self):
        self.examples = {
            'değişkenler': self.variable_example,
            'kontrol yapıları': self.control_structure_example,
            'fonksiyonlar': self.function_example,
            'listeler': self.list_example,
            'döngüler': self.loop_example,
            'sözlükler': self.dictionary_example,
            'hata yönetimi': self.exception_handling_example,
        }

    def show_examples(self):
        print("Örnek konular:")
        for topic in self.examples.keys():
            print(f"- {topic}")
        print("\nHangi konuyu görmek istersiniz?")

    def variable_example(self):
        return """
# Değişken Tanımlama
x = 5
y = "Merhaba"
print(x)
print(y)
"""

    def control_structure_example(self):
        return """
# Kontrol Yapıları
x = 10
if x > 5:
    print("x 5'ten büyük")
else:
    print("x 5'ten küçük veya eşit")
"""

    def function_example(self):
        return """
# Fonksiyon Tanımlama
def topla(a, b):
    return a + b

sonuc = topla(3, 4)
print(sonuc)
"""

    def list_example(self):
        return """
# Liste Kullanımı
meyveler = ["elma", "muz", "çilek"]
for meyve in meyveler:
    print(meyve)
"""

    def loop_example(self):
        return """
# Döngüler
for i in range(5):
    print(i)
"""

    def dictionary_example(self):
        return """
# Sözlük Kullanımı
sozluk = {"ad": "Ali", "yaş": 30}
print(sozluk["ad"])
"""

    def exception_handling_example(self):
        return """
# Hata Yönetimi
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Sıfıra bölme hatası!")
"""

    def get_example(self, topic):
        return self.examples.get(topic, lambda: "Bu konu bulunamadı.")()

    def compare_code(self, user_code, example_code):
        user_code_lines = user_code.strip().splitlines()
        example_code_lines = example_code.strip().splitlines()

        for i, line in enumerate(example_code_lines):
            if i < len(user_code_lines):
                if line.strip() != user_code_lines[i].strip():
                    print(f"Hata: {i + 1}. satırda beklenen: '{line.strip()}', ancak yazdığınız: '{user_code_lines[i].strip()}'")
            else:
                print(f"Hata: {i + 1}. satırda bekleniyordu, ancak siz yazmadınız.")

        if len(user_code_lines) > len(example_code_lines):
            print(f"Hata: Ekstra satır var, {len(user_code_lines) - len(example_code_lines)} fazla satır yazdınız.")

# Kullanıcı ile etkileşim
tool = PythonLearningTool()
tool.show_examples()

seçim = input("Seçiminizi yapın: ").strip().lower()
example_code = tool.get_example(seçim)

print("\nSeçilen konu örneği:\n")
print(example_code)

user_code = input("Kendi kodunuzu yazın ve ardından 'CTRL+D' (Unix) veya 'CTRL+Z' (Windows) ile bitirin:\n")
tool.compare_code(user_code, example_code)

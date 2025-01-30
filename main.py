pip install pandas fpdf

import pandas as pd
from fpdf import FPDF


# Kullanıcıdan gümrük beyannamesi için bilgi al
def get_product_info():
    gtip = input("GTIP Kodu: ")
    quantity = input("Miktar: ")
    value = input("Değer: ")

    # Verileri Pandas DataFrame içinde tutalım
    product_info = {
        'GTIP': [gtip],
        'Quantity': [quantity],
        'Value': [value]
    }
    df = pd.DataFrame(product_info)

    # Veri doğruluğu kontrolü
    if df.isnull().values.any():
        print("Lütfen tüm alanları doldurun.")
        return None

    return df


# PDF oluşturma
def generate_pdf(df):
    # PDF belgesi oluştur
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Gümrük Beyannamesi", ln=True, align='C')
    pdf.ln(10)

    # Veri tablosunu PDF'ye ekle
    for index, row in df.iterrows():
        for key, value in row.items():
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    # PDF'i kaydet
    pdf_output_name = "gumruk_beyannamesi.pdf"
    pdf.output(pdf_output_name)
    print(f"PDF oluşturuldu: {pdf_output_name}")


# Ana fonksiyon
def main():
    # Kullanıcıdan veri al
    df = get_product_info()

    if df is not None:
        # PDF oluştur
        generate_pdf(df)


if __name__ == "__main__":
    main()

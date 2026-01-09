from view import Tampilan

def main():
    app = Tampilan()
    data = app.input_data()
    app.tampilkan_hasil(data)

if __name__ == "__main__":
    main()

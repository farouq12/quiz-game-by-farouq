nama = input("ketik namamu: ")
print("selamat datang", nama, "untuk petualangan ini!")

jawaban = input(
    "Anda berada di jalan tanah, itu telah berakhir dan Anda dapat pergi ke kiri atau ke kanan. Cara mana yang ingin Anda tuju? ").lebih rendah()

if jawaban == "kiri":
    jawaban = input(
        "Anda datang ke sungai, Anda bisa berjalan di sekitarnya atau berenang menyeberang? Ketik berjalan untuk berjalan-jalan dan berenang untuk berenang menyeberang: ")

    if jawaban == "berenang":
        print("Anda berenang menyeberang dan dimakan oleh buaya")
    elif jawaban == "berjalan":
        print("Anda berjalan bermil-mil, kehabisan air dan Anda kalah dalam permainan.")
    else:
        print('Bukan pilihan yang valid. Kamu kalah.')

elif jawaban == "baik":
    jawaban = input(
        print("Anda datang ke jembatan, terlihat goyah, apakah Anda ingin menyeberang atau kembali (cross/back)?  ")

    if jawaban == "kembali":
        print("Anda kembali dan kalah.")
    elif jawaban == "menyeberang":
        jawaban = input(
            "Anda menyeberangi jembatan dan bertemu orang asing. Apakah Anda berbicara dengan mereka (ya/tidak)?  ")

        if jawaban == "ya":
            print("Anda berbicara dengan orang yang tidak dikenal dan mereka memberi Anda emas. Kamu menang!")
        elif jawaban == "tidak":
            print("Anda mengabaikan orang asing dan mereka tersinggung dan Anda kalah.")
        else:
            print('Bukan pilihan yang valid. Kamu kalah.')
    else:
        print('Bukan pilihan yang valid. Kamu kalah.')

else:
    print('Bukan pilihan yang valid. Kamu kalah.')

print("Terima kasih sudah mencoba", nama)
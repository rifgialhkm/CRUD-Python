import mysql.connector

connect = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="db_crud_python"
)

myCursor = connect.cursor()

lanjut = True
while lanjut:
    print("\nCRUD User")
    print("1. Lihat user")
    print("2. Tambah user")
    print("3. Ubah user")
    print("4. Hapus user")
    print("5. Keluar\n")

    a = input("Pilih menu : ")
    option = None
    if a != "":
        option = int(a)
    else:
        option = None

    if (option == 1):
        myCursor.execute("SELECT * FROM user")
        myResult = myCursor.fetchall()
        print("\n(id, nama, email, no hp)")
        for x in myResult:
            print(x)
    elif(option == 2):
        nama = input("Nama : ")
        email = input("Email : ")
        no_hp = input("No HP : ")
        sql = "INSERT INTO `user` (`nama`, `email`, `no_hp`) VALUES (%s, %s, %s)"
        val = (nama, email, no_hp)
        myCursor.execute(sql, val)
        connect.commit()
        print(myCursor.rowcount, "Data berhasil ditambah")
    elif(option == 3):
        id = input("\nID user : ")
        myCursor.execute("SELECT * FROM user WHERE id = "+id+" LIMIT 1")
        myResult = myCursor.fetchall()
        user = None
        for x in myResult:
            user = x
        if (user != None):
            nama = input("Nama ("+user[1]+") :") or user[1]
            email = input("Email ("+user[2]+") :") or user[2]
            no_hp = input("No HP ("+str(user[3])+") :") or user[3]
            sql = "UPDATE user SET nama=%s,email=%s,no_hp=%s WHERE id=%s"
            val = (nama, email, no_hp, id)
            myCursor.execute(sql, val)
            connect.commit()
            print(myCursor.rowcount, "Data berhasil diubah")
        else:
            print("Data tidak ditemukan")
    elif(option == 4):
        id = input("\nID user : ")
        myCursor.execute("SELECT * FROM user WHERE id ="+id+" LIMIT 1")
        myResult = myCursor.fetchall()
        user = None
        for x in myResult:
            user = x
        if (user != None):
            print("Hapus data : ", user)
            sql = "DELETE FROM user WHERE id ="+id
            myCursor.execute(sql)
            connect.commit()
            print("\nData berhasil dihapus")
        else:
            print("Data tidak ditemukan")
    elif(option == 5):
        print("\nSelamat tinggal!\n")
        lanjut = False
    else:
        print("\nMenu belum dibuat :)")

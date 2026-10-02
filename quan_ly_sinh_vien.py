danh_sach_sv = []


def nhap_diem(mon):
    while True:
        try:
            diem = float(input("Nhap diem " + mon + ": "))

            if 0 <= diem <= 10:
                return diem

            print("Diem phai tu 0 den 10.")

        except ValueError:
            print("Du lieu khong hop le, vui long nhap lai.")


def tim_sinh_vien(ma_sv):
    for sv in danh_sach_sv:
        if sv["ma_sv"] == ma_sv:
            return sv
    return None


def xep_loai(diem_tb):
    if diem_tb >= 8:
        return "Gioi"
    elif diem_tb >= 6.5:
        return "Kha"
    elif diem_tb >= 5:
        return "Trung binh"
    else:
        return "Yeu"


def hien_thi_sinh_vien():
    if len(danh_sach_sv) == 0:
        print("Chua co sinh vien.")
        return

    for sv in danh_sach_sv:
        print(
            "Ma SV:", sv["ma_sv"],
            "| Ho ten:", sv["ho_ten"],
            "| Toan:", sv["toan"],
            "| Van:", sv["van"],
            "| Anh:", sv["anh"],
            "| Diem TB:", round(sv["diem_tb"], 2),
            "| Xep loai:", sv["xep_loai"]
        )


def them_sinh_vien():
    ma_sv = input("Nhap ma sinh vien: ").strip().upper()

    if tim_sinh_vien(ma_sv) is not None:
        print("Ma sinh vien da ton tai.")
        return

    ho_ten = input("Nhap ho ten: ").strip().title()

    toan = nhap_diem("Toan")
    van = nhap_diem("Van")
    anh = nhap_diem("Anh")

    diem_tb = (toan + van + anh) / 3
    loai = xep_loai(diem_tb)

    danh_sach_sv.append({
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "toan": toan,
        "van": van,
        "anh": anh,
        "diem_tb": diem_tb,
        "xep_loai": loai
    })

    print("Them sinh vien thanh cong.")
    print("Diem trung binh:", round(diem_tb, 2))
    print("Xep loai:", loai)


def tim_sinh_vien_menu():
    ma_sv = input("Nhap ma sinh vien can tim: ").strip().upper()

    sv = tim_sinh_vien(ma_sv)

    if sv is None:
        print("Khong tim thay sinh vien.")
        return

    print("Ma sinh vien:", sv["ma_sv"])
    print("Ho ten:", sv["ho_ten"])
    print("Diem Toan:", sv["toan"])
    print("Diem Van:", sv["van"])
    print("Diem Anh:", sv["anh"])
    print("Diem trung binh:", round(sv["diem_tb"], 2))
    print("Xep loai:", sv["xep_loai"])


def xoa_sinh_vien():
    ma_sv = input("Nhap ma sinh vien can xoa: ").strip().upper()

    sv = tim_sinh_vien(ma_sv)

    if sv is None:
        print("Khong tim thay sinh vien.")
        return

    danh_sach_sv.remove(sv)
    print("Xoa sinh vien thanh cong.")


def thong_ke():
    if len(danh_sach_sv) == 0:
        print("Chua co sinh vien.")
        return

    tong = 0

    for sv in danh_sach_sv:
        tong += sv["diem_tb"]

    diem_tb_chung = tong / len(danh_sach_sv)

    print("So luong sinh vien:", len(danh_sach_sv))
    print("Diem trung binh chung:", round(diem_tb_chung, 2))

    print("So sinh vien Gioi:",
          sum(1 for sv in danh_sach_sv if sv["xep_loai"] == "Gioi"))

    print("So sinh vien Kha:",
sum(1 for sv in danh_sach_sv if sv["xep_loai"] == "Kha"))

    print("So sinh vien Trung binh:",
          sum(1 for sv in danh_sach_sv if sv["xep_loai"] == "Trung binh"))

    print("So sinh vien Yeu:",
          sum(1 for sv in danh_sach_sv if sv["xep_loai"] == "Yeu"))


def hien_thi_menu():
    print("QUAN LY SINH VIEN")
    print("1. Hien thi danh sach sinh vien")
    print("2. Them sinh vien")
    print("3. Tim sinh vien")
    print("4. Xoa sinh vien")
    print("5. Thong ke")
    print("0. Thoat")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()

        lua_chon = input("Nhap lua chon: ")

        if lua_chon == "1":
            hien_thi_sinh_vien()

        elif lua_chon == "2":
            them_sinh_vien()

        elif lua_chon == "3":
            tim_sinh_vien_menu()

        elif lua_chon == "4":
            xoa_sinh_vien()

        elif lua_chon == "5":
            thong_ke()

        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh.")
            break

        else:
            print("Lua chon khong hop le.")


if __name__ == "__main__":
    chay_chuong_trinh()
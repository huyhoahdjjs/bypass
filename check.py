import concurrent.futures
import requests
import os

os.system("color 0")
os.system("cls" if os.name == "nt" else "clear")

def kiem_tra_proxy(proxy, timeout):
    try:
        session = requests.Session()
        session.proxies = {'http': proxy, 'https': proxy}
        response = session.head('http://103.195.236.167/a.html', timeout=timeout)
        if response.status_code == 200:
            return proxy
    except:
        pass
    return None

def loc_proxy_trung(proxies):
    proxies_uniques = set(proxies)
    return list(proxies_uniques)

def tai_danh_sach_proxy(ten_file):
    if not os.path.isfile(ten_file):
        print(f"  File '{ten_file}' không tồn tại. Vui lòng nhập lại.")
        return tai_danh_sach_proxy(input("  Nhập tên file chứa danh sách proxy: "))
    with open(ten_file) as f:
        return [line.strip() for line in f.readlines()]

def luu_danh_sach_proxy(proxies, ten_file):
    with open(ten_file, 'w') as f:
        f.write('\n'.join(proxies))


banner = """
    
░██████╗░██████╗░░█████╗░██╗░░░██╗██╗████████╗██╗░░░██╗
██╔════╝░██╔══██╗██╔══██╗██║░░░██║██║╚══██╔══╝╚██╗░██╔╝
██║░░██╗░██████╔╝███████║╚██╗░██╔╝██║░░░██║░░░░╚████╔╝░
██║░░╚██╗██╔══██╗██╔══██║░╚████╔╝░██║░░░██║░░░░░╚██╔╝░░
╚██████╔╝██║░░██║██║░░██║░░╚██╔╝░░██║░░░██║░░░░░░██║░░░
░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░░░░╚═╝░░░
║➢ Admin   : Hoàng ™ 👾
║➢ The Center Of All Power😈 ™
║➣ Gravity By Hoàng Simp Gawr Gura !™
║➣ Box Zalo  : https://zalo.me/g/htejns046
 ⚠ ⚠ ⚠ ⚠ ⚠  ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ 👾 👾 👾 👾 👾
"""

def main():
    print(banner)

    ten_file = input("\n  Nhập tên file chứa danh sách proxy: ")

    proxies = tai_danh_sach_proxy(ten_file)

    print("================================================")
    print("  1. Lọc các proxy trùng nhau")
    print("  2. Kiểm tra proxy hoạt động")

    choice = input("  Nhập lựa chọn: ")

    if choice == "1":
        proxies_uniques = loc_proxy_trung(proxies)
        luu_danh_sach_proxy(proxies_uniques, ten_file)
        print("================================================")
        print("\n  Kết quả lọc proxy trùng nhau")
        print(f'  Tổng số proxy đã tìm thấy: {len(proxies)}')
        print(f'  Tổng số proxy còn lại: {len(proxies_uniques)}')
        input()
    elif choice == "2":
        timeout = int(input("  Nhập timeout (số giây): "))
        print("\n  Đang kiểm tra proxy. Vui lòng đợi...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=5000000) as executor:
            results = list(executor.map(lambda proxy: kiem_tra_proxy(proxy, timeout), proxies))

        proxies_unique = [proxy for proxy in results if proxy is not None]
        luu_danh_sach_proxy(proxies_unique, ten_file)
        print("================================================")
        print("\n  Kết quả kiểm tra proxy hoạt động")
        print(f'  Tổng số proxy đã tìm thấy: {len(proxies)}')
        print(f'  Tổng số proxy hoạt động: {len(proxies_unique)}')
        input()
    else:
        print("================================================")
        print("\n  Lựa chọn không hợp lệ. Đã thoát chương trình.")
        input()

if __name__ == "__main__":
    main()

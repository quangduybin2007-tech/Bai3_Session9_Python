# Khởi tạo danh sách mã đơn hàng ban đầu của hệ thống
order_list = ["GE001", "GE002", "GE003"]


def display_menu():
    """Hiển thị menu quản lý hệ thống giao vận"""
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")
    print("=" * 50)


# Vòng lặp chính duy trì trạng thái hoạt động của ứng dụng CLI
while True:
    display_menu()
    choice_input = input("Vui lòng nhập lựa chọn của bạn (1-4): ").strip()

    # Bẫy 3 — Xử lý trường hợp người dùng nhập ký tự chữ hoặc ký tự đặc biệt
    try:
        choice = int(choice_input)
    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    # Bẫy 3 — Xử lý trường hợp nhập số nằm ngoài phạm vi từ 1 đến 4
    if choice < 1 or choice > 4:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    # Xử lý các chức năng nghiệp vụ dựa trên lựa chọn hợp lệ
    if choice == 1:
        print("\n--- 1. DANH SÁCH ĐƠN HÀNG ---")
        # Kiểm tra nếu danh sách không có dữ liệu nào
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            # Sử dụng enumerate để tự động đánh số thứ tự tăng dần từ 1
            for index, order in enumerate(order_list, start=1):
                print(f"{index}. {order}")

    elif choice == 2:
        print("\n--- 2. THÊM ĐƠN HÀNG MỚI ---")
        raw_new_order = input("Nhập mã đơn hàng mới: ")
        
        # Bẫy 1 — Xử lý chuẩn hóa khoảng trắng hai đầu và viết hoa toàn bộ ký tự
        clean_new_order = raw_new_order.strip().upper()
        
        # Thêm mã đơn hàng đã chuẩn hóa vào cuối danh sách
        order_list.append(clean_new_order)
        print(f"[THÀNH CÔNG] Đã thêm mã đơn hàng: {clean_new_order}")

    elif choice == 3:
        print("\n--- 3. XÓA ĐƠN HÀNG THEO MÃ ---")
        raw_delete_order = input("Nhập mã đơn hàng cần xóa: ")
        
        # Bẫy 1 — Chuẩn hóa đầu vào của mã cần xóa để đối chiếu chính xác với bộ lưu trữ
        clean_delete_order = raw_delete_order.strip().upper()

        # Kiểm tra tính tồn tại của mã đơn hàng trước khi thực hiện thao tác xóa
        if clean_delete_order in order_list:
            order_list.remove(clean_delete_order)
            print(f"[THÀNH CÔNG] Đã xóa đơn hàng: {clean_delete_order}")
        else:
            # Bẫy 2 — Xóa mã đơn hàng không tồn tại trong hệ thống
            print("Không tìm thấy mã đơn hàng cần xóa!")

    elif choice == 4:
        # Kết thúc ca làm việc, thoát luồng chạy chương trình
        print("\nThoát chương trình.")
        break
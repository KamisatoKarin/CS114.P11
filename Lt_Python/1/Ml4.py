import re

def co_mua_duoc_tat_ca_san_pham(gia_san_pham, thong_bao, ngan_sach):
    tong_gia_online = 0
    tong_gia_tai_cua_hang = 0
    
    for i, gia_str in enumerate(gia_san_pham):
        gia = float(gia_str)
        thong_bao_san_pham = thong_bao[i]
        
        # Tìm thông tin giảm giá khi mua online
        match_giam_online = re.search(r"(\d+(\.\d+)?)% lower than in-store", thong_bao_san_pham)
        if match_giam_online:
            phan_tram_tiet_kiem = float(match_giam_online.group(1))
            gia_online = gia
            gia_tai_cua_hang = gia / (1 - phan_tram_tiet_kiem / 100)
        else:
            # Tìm thông tin tăng giá khi mua tại cửa hàng
            match_giam_tai_cua_hang = re.search(r"(\d+(\.\d+)?)% higher than in-store", thong_bao_san_pham)
            if match_giam_tai_cua_hang:
                phan_tram_tiet_kiem = float(match_giam_tai_cua_hang.group(1))
                gia_tai_cua_hang = gia
                gia_online = gia * (1 + phan_tram_tiet_kiem / 100)
            else:
                # Nếu không có thông tin tiết kiệm, giả sử giá online và giá tại cửa hàng là như nhau
                gia_online = gia_tai_cua_hang = gia
        
        tong_gia_online += gia_online
        tong_gia_tai_cua_hang += gia_tai_cua_hang
    
    return tong_gia_online <= ngan_sach or tong_gia_tai_cua_hang <= ngan_sach

# Đọc dữ liệu đầu vào
gia_san_pham = input().strip().split()
thong_bao = [input().strip() for _ in range(len(gia_san_pham))]
ngan_sach = float(input().strip())

# Kiểm tra và in kết quả
ket_qua = co_mua_duoc_tat_ca_san_pham(gia_san_pham, thong_bao, ngan_sach)
print(str(ket_qua).lower())

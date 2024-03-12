import sys


def read_txt_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File '{}' không tồn tại.".format(filename))
        return None

# Đọc danh sách các XSS payload từ tệp xss-payload-list.txt
  # Thay đổi đường dẫn thành tên file thực tế


# Hàm kiểm tra xem chuỗi nhập liệu có chứa các lỗi XSS từ danh sách payload hay không
def check_xss_vulnerability(content, xss_payloads):
    if xss_payloads is None:
        print("Không thể đọc danh sách các XSS payload.")
        return False
    # Tách các payload trong nội dung của file
    payloads = xss_payloads.split('\n')
    # Kiểm tra từng payload xem có tồn tại trong chuỗi nhập liệu không
    for payload in payloads:
        if payload.strip() != '' and payload in content:
            return True
    return False

# Đoạn mã kiểm tra lỗi XSS cho chuỗi nhập liệu

def checkXSS(input_string):
    xss_payload_file = "D:\\tai xuong\\xss-payload-list.txt"
    xss_payloads = read_txt_file(xss_payload_file)
    if xss_payloads is not None:
        if check_xss_vulnerability(input_string, xss_payloads):
            print("Chuỗi nhập liệu chứa lỗi XSS từ danh sách payload.")
        else:
            print("Chuỗi nhập liệu không chứa lỗi XSS từ danh sách payload.")
    else:
        print("Không thể đọc danh sách các XSS payload.")
input_string = input("Nhập chuỗi nhập liệu: ")
checkXSS(input_string)
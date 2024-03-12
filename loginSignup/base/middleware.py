# middleware.py

from django.http import HttpResponseBadRequest

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Kiểm tra lỗi XSS cho các thông tin được POST lên server
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if self.check_xss_vulnerability(username):
                return HttpResponseBadRequest("Dữ liệu nhập vào chứa lỗi XSS.")
        
        # Tiếp tục xử lý các yêu cầu khác
        response = self.get_response(request)
        return response

    def check_xss_vulnerability(self, input_string):
        # Hàm kiểm tra lỗi XSS tương tự như bạn đã triển khai trong đoạn mã Python trước đó
        xss_payload_file = "D:\\tai xuong\\xss-payload-list.txt"
        xss_payloads = self.read_txt_file(xss_payload_file)
        if xss_payloads is not None:
            if self.check_xss_vulnerability_helper(input_string, xss_payloads):
                return True
        return False

    def read_txt_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print("File '{}' không tồn tại.".format(filename))
            return None

    def check_xss_vulnerability_helper(self, content, xss_payloads):
        if xss_payloads is None:
            return False
        payloads = xss_payloads.split('\n')
        for payload in payloads:
            if payload.strip() != '' and payload in content:
                return True
        return False

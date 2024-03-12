from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if flow.request.method == "POST":
        print(f"POST request: {flow.request.url}")
        print(f"POST data: {flow.request.text}")

def response(flow: http.HTTPFlow) -> None:
    pass  # Chúng ta không cần xử lý phản hồi ở đây

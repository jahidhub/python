def http_status(status):
    match status:
        case 200:
            return "ok"
        case 400:
            return "Not found"
        case 500:
            return "Internal Server Error"
        case _:
            return "There is a another problems"


print(http_status(500))

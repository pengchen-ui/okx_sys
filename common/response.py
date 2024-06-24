from fastapi.responses import JSONResponse


class Response:
    @staticmethod
    def success(data=None):
        if data is None:
            data = []
        return JSONResponse(dict(code="1", msg="ok", data=data))

    @staticmethod
    def error(data=None, msg=None):
        if data is None:
            data = []
        return JSONResponse(dict(code="0", msg=msg, data=data))

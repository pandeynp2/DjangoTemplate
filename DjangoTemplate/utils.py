import time
import requests
from .settings import BASE_HOST
import logging

def get_user_session(request, is_debug=False):
    session = request.session.get("user_details", None)
    if session:
        session["servertime"] = int(time.time() * 1000)
        return session
    else:
        try:
            auth_url = "https://" + BASE_HOST + "/.auth/me"
            response = requests.get(
                url=auth_url, cookies=request.COOKIES, timeout=20
            ).json()
            session = {}
            for i in response:
                for j in i:
                    if j == "user_id":
                        session["email"] = i[j]
                        session["userid"] = i[j].split("@")[0]
                    elif j == "user_claims":
                        for k in i[j]:
                            if k["typ"] == "name":
                                if "," in k["val"]:
                                    k["val"] = k["val"].replace(",", " ")
                                    session["username"] = k["val"]
                                else:
                                    session["username"] = k["val"]
            if "@pg.com" not in session.get("email", ""):
                return None

            session["servertime"] = int(time.time() * 1000)
            request.session["user_details"] = session
            return session
        except Exception as e:
            logging.warning(e, exc_info=True)
            if is_debug:
                session = {
                    "username": "Dummy  User",
                    "email": "dummy@dummy.com",
                    "servertime": str(int(time.time() * 1000)),
                    "userid": "dummy"
                }
                request.session["user_details"] = session
                return session
            else:
                return None

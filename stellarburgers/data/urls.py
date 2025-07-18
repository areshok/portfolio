BASE_URL = "https://stellarburgers.nomoreparties.site"

URLS = {
    "api": {
        "register": f"{BASE_URL}/api/auth/register",
        "login": f"{BASE_URL}/api/auth/login",
        "order": f"{BASE_URL}/api/orders",
        "ingridients": f"{BASE_URL}/api/ingredients"
    },
    "ui": {
        "/": f"{BASE_URL}/",
        "register": f"{BASE_URL}/register",
        "login": f"{BASE_URL}/login",
        "fogot-password": f"{BASE_URL}/forgot-password",
        "feed": f"{BASE_URL}/feed",
        "profile": f"{BASE_URL}/account/profile",
    }
}

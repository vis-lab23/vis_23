from locust import task, run_single_user
from locust import FastHttpUser


class webshop(FastHttpUser):
    host = "http://127.0.0.1:64180"
    default_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Cookie": "JSESSIONID=2D5D339999470D00B2371687DEA7DE36",
        "Host": "127.0.0.1:55697",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }

    @task
    def t(self):
        with self.client.request(
            "POST",
            "/EShop-1.0.0/LoginAction.action;jsessionid=2D5D339999470D00B2371687DEA7DE36",
            headers={
                "Cache-Control": "max-age=0",
                "Content-Length": "52",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": self.host,
                "Referer": self.host + "/EShop-1.0.0/",
            },
            data="username=admin&password=admin&method%3Aexecute=login",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/EShop-1.0.0/InitCategorySiteAction.action?pageToGoTo=c",
            headers={
                "Referer": self.host + "/EShop-1.0.0/LoginAction.action;jsessionid=2D5D339999470D00B2371687DEA7DE36"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/EShop-1.0.0/AddCategoryAction.action",
            headers={
                "Cache-Control": "max-age=0",
                "Content-Length": "65",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": self.host,
                "Referer": self.host + "/EShop-1.0.0/InitCategorySiteAction.action?pageToGoTo=c",
            },
            data="newCatName=B%C3%BCcher&method%3Aexecute=Kategorie+hinzuf%C3%BCgen",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/EShop-1.0.0/InitCategorySiteAction.action?pageToGoTo=p",
            headers={
                "Referer": self.host + "/EShop-1.0.0/AddCategoryAction.action"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/EShop-1.0.0/AddProductAction.action",
            headers={
                "Cache-Control": "max-age=0",
                "Content-Length": "110",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": self.host,
                "Referer": self.host + "/EShop-1.0.0/InitCategorySiteAction.action?pageToGoTo=p",
            },
            data="name=Harry+Potter&price=3.50&categoryId=b%C3%BCcher&details=Er+zaubert+und+so&method%3Aexecute=Hinzuf%C3%BCgen",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/EShop-1.0.0/listAllProducts",
            headers={
                "Cache-Control": "max-age=0",
                "Referer": self.host + "/EShop-1.0.0/InitCategorySiteAction.action?pageToGoTo=p",
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(webshop)

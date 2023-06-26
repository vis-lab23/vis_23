from locust import task, run_single_user
from locust import FastHttpUser


class ProduktAnlegen(FastHttpUser):
    host = "http://127.0.0.1:64180"
    default_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Cookie": "JSESSIONID=76DD5CA09BCDB44AC6A8ED20CAC67F07",
        "Host": "127.0.0.1:64180",
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
            "GET",
            "/EShop-1.0.0/InitCategorySiteAction.action?pageToGoTo=p",
            headers={
                "Referer": self.host + "/EShop-1.0.0/listAllProducts.action"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/EShop-1.0.0/AddProductAction.action",
            headers={
                "Cache-Control": "max-age=0",
                "Content-Length": "104",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": self.host,
                "Referer": self.host + "/EShop-1.0.0/InitCategorySiteAction.action?pageToGoTo=p",
            },
            data="name=Herr+der+Ringe&price=9.50&categoryId=b%C3%BCcher&details=Klassiker&method%3Aexecute=Hinzuf%C3%BCgen",
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
        with self.client.request(
            "GET",
            "/EShop-1.0.0/InitCategorySiteAction.action?pageToGoTo=p",
            headers={"Referer": self.host + "/EShop-1.0.0/listAllProducts"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/EShop-1.0.0/AddProductAction.action",
            headers={
                "Cache-Control": "max-age=0",
                "Content-Length": "109",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": self.host,
                "Referer": self.host + "/EShop-1.0.0/InitCategorySiteAction.action?pageToGoTo=p",
            },
            data="name=Moby+Dick&price=2.50&categoryId=b%C3%BCcher&details=Ebenfalls+Klassiker&method%3Aexecute=Hinzuf%C3%BCgen",
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
    run_single_user(ProduktAnlegen)

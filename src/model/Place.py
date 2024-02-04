
class Place:
    def __init__(self, name, address, phone, url=None):
        self.url = url
        self.phone = phone
        self.address = address
        self.name = name

    @staticmethod
    def from_json(data):
        point_of_interest = data["poi"]
        name = point_of_interest["name"]
        address = data["address"]["freeformAddress"]
        phone = "" if "phone" not in point_of_interest else point_of_interest["phone"]
        url = None if "url" not in point_of_interest else point_of_interest["url"]

        return Place(
            name=name,
            phone=phone,
            address=address,
            url=url
        )

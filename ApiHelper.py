import requests

class ApiHelper:
    def __init__(self):
        self.url = "https://swapi.co/api/people/"

    def log_args(func):
        def function_wrapper(self, x):
            print("Arg passed to method :  " + str(x))
            return func(self, x)
        return function_wrapper

    @log_args
    def star_war_characters(self, page_nr):
        self.paginated_data = []
        url = self.url+"?page={0}".format(page_nr)
        #Get the response content from the API
        cont = self.get_api_contnet(url)
        if cont:
            results = cont.get('results')
            if results:
                for i in range(len(results)):
                    self.star_war_char_data = {}
                    self.star_war_char_data['name'] = results[i].get('name')
                    self.star_war_char_data['height'] = results[i].get('height')
                    self.star_war_char_data['gender'] = results[i].get('gender')
                    self.paginated_data.append(self.star_war_char_data)
            else:
                print("Data missing!")
        else:
            print("No content found from api response!")
        return self.paginated_data


    def get_api_contnet(self, url):
        resp = requests.get(url)
        if resp.status_code == 200:
            content = resp.json()
            return content
        else:
            return {}

    def append_to_file(self,filepath,name,age,gender):
        with open(filepath,"a") as f:
            f.write("{0},{1},{2}\n".format(name,age,gender))
        f.close()

    def get_data(self,data):
        self.append_to_file("output.txt","Name","Height","Gender")
        for i in range(len(data)):
            name = data[i].get('name')
            height = data[i].get('height')
            gender = data[i].get('gender')
            self.append_to_file("output.txt",name,height,gender)


a = ApiHelper()
response_content = a.star_war_characters(1)
print("Writing data to File ")
a.get_data(response_content)


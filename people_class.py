class people:
    def __init__(self, user_name, age, city):
        self.__user_name=user_name
        self.__city=city
        if int(age)>0 :
            self.__age=age
        else:
            return 0
    def get_age(self):
        return self.__age
    def get_user_name(self):
        return self.__user_name
    def get_city(self):
        return self.__city
    def set_city(self, new_city):
        self.__city=new_city
    def get_all(self):
        return self.__user_name, self.__age, self.__city

import pickle
import json
import pandas as pd
import numpy as np


class AutoCarPrice():
    def __init__(self,symboling,normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,
    engine_location,wheel_base,length,width,height,curb_weight,num_of_cylinders,engine_size,bore,
    stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,
    fuel_system):
        self.symboling = symboling
        self.normalized_losses = normalized_losses
        self.fuel_type = fuel_type
        self.aspiration = aspiration
        self.num_of_doors = num_of_doors
        self.drive_wheels = drive_wheels
        self.engine_location = engine_location
        self.wheel_base = wheel_base
        self.length = length
        self.width = width
        self.height = height
        self.curb_weight = curb_weight
        self.num_of_cylinders = num_of_cylinders
        self.engine_size = engine_size
        self.bore = bore
        self.stroke = stroke
        self.compression_ratio = compression_ratio
        self.horsepower = horsepower
        self.peak_rpm = peak_rpm
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg
        self.make = "make_" + make
        self.body_style = "body-style_" + body_style
        self.engine_type = "engine-type_" + engine_type
        self.fuel_system = "fuel-system_" + fuel_system

    def load_file(self):
        with open ('models/auto_model.pkl','rb') as f:
            self.auto_model = pickle.load(f)

        with open ('models/json_auto_data.json','r') as f:
            self.json_auto_data = json.load(f)

    def get_predicted_car_price(self):
        self.load_file()  
        
        make_index = self.json_auto_data['columns'].index(self.make)
        body_style_index = self.json_auto_data['columns'].index(self.body_style)
        engine_type_index = self.json_auto_data['columns'].index(self.engine_type)
        fuel_system_index = self.json_auto_data['columns'].index(self.fuel_system)
        


        array = np.zeros(len(self.json_auto_data["columns"]))
        array[0] = self.symboling
        array[1] = self.normalized_losses
        array[2] = self.json_auto_data["fuel_type_value"][self.fuel_type]
        array[3] = self.json_auto_data["aspiration_value"][self.aspiration]
        array[4] = self.json_auto_data["num_doors_value"][self.num_of_doors]
        array[5] = self.json_auto_data["drive_wheels_value"][self.drive_wheels]
        array[6] = self.json_auto_data["engine_loc_value"][self.engine_location]
        array[7] = self.wheel_base
        array[8] = self.length
        array[9] = self.width
        array[10] = self.height
        array[11] = self.curb_weight
        array[12] = self.json_auto_data["num_cyli_value"][self.num_of_cylinders]
        array[13] = self.engine_size
        array[14] = self.bore
        array[15] = self.stroke
        array[16] = self.compression_ratio
        array[17] = self.horsepower
        array[18] = self.peak_rpm
        array[19] = self.city_mpg
        array[20] = self.highway_mpg
        array[make_index] = 1
        array[body_style_index] = 1
        array[engine_type_index] = 1
        array[fuel_system_index] = 1
        
        
        print("Array -->",array)
        predicted_price = self.auto_model.predict([array])[0]
        return np.around(predicted_price, 2)


if __name__ == "__main__":
    symboling = 3.0
    normalized_losses = 115.0
    fuel_type = 'gas'
    aspiration= 'turbo'
    num_of_doors= 'two'
    drive_wheels= '4wd'
    engine_location= 'front'
    wheel_base=88.60
    length=168.80
    width=64.10
    height=48.80
    curb_weight=2548.00
    num_of_cylinders= 'two'
    engine_size=130.00
    bore=3.47
    stroke=2.68
    compression_ratio=9.00
    horsepower=111.00
    peak_rpm=5000.00
    city_mpg=21.00
    highway_mpg=27.00 
    make = "audi"
    body_style = "convertible"
    engine_type = "dohc"
    fuel_system = "spfi"

    adp = AutoCarPrice(symboling,normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,
    engine_location,wheel_base,length,width,height,curb_weight,num_of_cylinders,engine_size,bore,
    stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,
    fuel_system)
    price = adp.get_predicted_car_price()
    print(f"predicted price of car is {price} RS only")

from flask import Flask, jsonify, render_template, request
from models.utils import AutoCarPrice
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("hello flask")
   
    return render_template("index.html")

@app.route('/predict_car_price', methods = ["GET","POST"])

def get_predicted_price_of_car():
    if request.method == "GET":
        print("We are using GET Method")
        # data = request.form
        # print('Data-->',data)

    # symboling = eval(data['symboling'])
    # normalized_losses = eval(data['normalized_losses'])
    # fuel_type = data['fuel_type']
    # aspiration= data['aspiration']
    # num_of_doors= data['num_of_doors']
    # drive_wheels= data['drive_wheels']
    # engine_location= data['engine_location']
    # wheel_base=eval(data['wheel_base'])
    # length=eval(data['length'])
    # width=eval(data['width'])
    # height=eval(data['height'])
    # curb_weight=eval(data['curb_weight'])
    # num_of_cylinders= data['num_of_cylinders']
    # engine_size=eval(data['engine_size'])
    # bore=eval(data['bore'])
    # stroke=eval(data['stroke'])
    # compression_ratio=eval(data['compression_ratio'])
    # horsepower=eval(data['horsepower'])
    # peak_rpm=eval(data['peak_rpm'])
    # city_mpg=eval(data['city_mpg'])
    # highway_mpg=eval(data['highway_mpg'])
    # make = data['make']
    # body_style = data['body_style']
    # engine_type = data['engine_type']
    # fuel_system = data['fuel_system']
        symboling = eval(request.args.get("symboling"))
        normalized_losses = eval(request.args.get("normalized_losses"))
        fuel_type = request.args.get("fuel_type")
        aspiration= request.args.get("aspiration")
        num_of_doors= request.args.get("num_of_doors")
        drive_wheels= request.args.get("drive_wheels")
        engine_location= request.args.get("engine_location")
        wheel_base=eval(request.args.get("wheel_base"))
        length=eval(request.args.get("length"))
        width=eval(request.args.get("width"))
        height = eval(request.args.get("height"))
        curb_weight=eval(request.args.get("curb_weight"))
        num_of_cylinders= request.args.get("num_of_cylinders")
        engine_size=eval(request.args.get("engine_size"))
        bore=eval(request.args.get("bore"))
        stroke=eval(request.args.get("stroke"))
        compression_ratio=eval(request.args.get("compression_ratio"))
        horsepower=eval(request.args.get("horsepower"))
        peak_rpm=eval(request.args.get("peak_rpm"))
        city_mpg=eval(request.args.get("city_mpg"))
        highway_mpg=eval(request.args.get("highway_mpg"))
        make = request.args.get("make")
        body_style = request.args.get("body_style")
        engine_type = request.args.get("engine_type")
        fuel_system = request.args.get("fuel_system")

        adp = AutoCarPrice(symboling,normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,num_of_cylinders,engine_size,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,fuel_system)
        price = adp.get_predicted_car_price()
        # return jsonify({"Result": f"predicted price of car is {price} RS only"})
        return render_template("index.html", prediction = price)

    else:
        print("We are using POST Method")

        symboling = eval(request.form.get("symboling"))
        normalized_losses = eval(request.form.get("normalized_losses"))
        fuel_type = request.form.get("fuel_type")
        aspiration= request.form.get("aspiration")
        num_of_doors= request.form.get("num_of_doors")
        drive_wheels= request.form.get("drive_wheels")
        engine_location= request.form.get("engine_location")
        wheel_base=eval(request.form.get("wheel_base"))
        length=eval(request.form.get("length"))
        width=eval(request.form.get("width"))
        height=eval(request.form.get("height"))
        curb_weight=eval(request.form.get("curb_weight"))
        num_of_cylinders= request.form.get("num_of_cylinders")
        engine_size=eval(request.form.get("engine_size"))
        bore=eval(request.form.get("bore"))
        stroke=eval(request.form.get("stroke"))
        compression_ratio=eval(request.form.get("compression_ratio"))
        horsepower=eval(request.form.get("horsepower"))
        peak_rpm=eval(request.form.get("peak_rpm"))
        city_mpg=eval(request.form.get("city_mpg"))
        highway_mpg=eval(request.form.get("highway_mpg"))
        make = request.form.get("make")
        body_style = request.form.get("body_style")
        engine_type = request.form.get("engine_type")
        fuel_system = request.form.get("fuel_system")

        adp = AutoCarPrice(symboling,normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,num_of_cylinders,engine_size,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,fuel_system)
        price = adp.get_predicted_car_price()
        return render_template("index.html", prediction = price)
        # return jsonify({"Result": f"predicted price of car is {price} RS only"})

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = config.PORT_NUMBER,debug = True)
# Libraries

from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)
app.config["DEBUG"] = True

price = []

@app.route('/', methods = ['GET', 'POST'])
def home():

    if request.method == 'GET':
        return render_template("index.html", price_list=price)

    try :
        house_type = request.form['house_type']
        sq_mt_built = request.form['square_meters']
        n_rooms = request.form['n_rooms']
        n_bathrooms = request.form['n_bathrooms']
        is_renewal_needed = request.form['renewal']
        has_parking = request.form['parking']

        if house_type == "Piso":
            model = pickle.load(open('./model/pisos_Rand_For.model', 'rb'))
            print('piso')
            prediction = model.predict([[sq_mt_built, n_rooms, n_bathrooms, is_renewal_needed, has_parking]])
            print(prediction)
            pred = ["Precio: " + str(round(prediction[0], 2))+" €"]
        
        elif house_type == "Chalet":
            model = pickle.load(open('./model/chalets_Rand_For.model', 'rb'))
            print('chale')
            prediction = model.predict([[sq_mt_built, n_rooms, n_bathrooms, is_renewal_needed, has_parking]])
            pred = ["Precio: " + str(round(prediction[0], 2))+" €"]

    except:
        pred =  ["Valores erróneos o falta alguno de ellos."]
    
    try:
        price.pop()
    except:
        pass

    price.append(pred)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
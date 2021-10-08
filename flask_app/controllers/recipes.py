from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User


@app.route('/new/recipe')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_recipe.html',user=User.get_by_id(data))


@app.route('/create/recipe',methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        print(5)
        return redirect('/logout')

    if not Recipe.validate_recipe(request.form):
        print (10)
        return redirect('/new/recipe')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30": int(request.form["under30"]),
        "users_id": session["user_id"],
        "date_made": request.form["date_made"]
    }
    print(15)
    Recipe.save(data)
    print(20)
    return redirect('/welcome')                                                         

@app.route ('/edit/recipe/<int:id>')
def editcar(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_recipe.html",edit=Recipe.get_one(data),user=User.get_by_id(user_data))

@app.route ('/update/recipe',methods=['POST'])
def update():
    Recipe.update(request.form)
    return redirect('/welcome')

@app.route('/recipe/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    Recipe.delete(data)
    return redirect('/welcome')

@app.route('/recipe/show/<int:id>')
def show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    print(30)
    return render_template("show_recipe.html",recipe=Recipe.get_one(data),user=User.get_one(user_data))